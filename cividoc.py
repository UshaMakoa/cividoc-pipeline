#!/usr/bin/env python3
"""Build a unified, source-faithful CiviCRM documentation site.

The pipeline synchronises the official User, Installation, and System
Administrator guides, optionally rewrites pages with an AI provider, enriches
front matter, builds task-oriented navigation, generates category and audience
views, audits the documentation, and runs MkDocs.
"""

from __future__ import annotations

import traceback
import argparse
import csv
import hashlib
import json
import os
import posixpath
import re
import shutil
import stat
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import yaml

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args: Any, **kwargs: Any) -> bool:
        return False


PIPELINE_VERSION = "2026.10-navigation-v7"
NAVIGATION_PROMPT_VERSION = "shallow-ai-navigation-v7"
REWRITE_PROMPT_VERSION = "source-faithful-taxonomy-v6"
DEFAULT_WORKSPACE = ".cividoc"
DEFAULT_OUTPUT = "generated-civicrm-docs"
DEFAULT_GUIDES = "user-en,installation,sysadmin"
BROWSE_DIR = "_browse"
MAX_NAV_CHOICES = 18
MAX_MAIN_ROOT_CHOICES = 6
MAX_NAV_DEPTH = 3
DEFAULT_FIDELITY_ATTEMPTS = 3

ALLOWED_CATEGORIES = {"tutorial", "how-to", "reference", "explanation"}
ALLOWED_LEVELS = {"basic", "intermediate", "advanced"}
ALLOWED_JOURNEY_STAGES = {
    "overview",
    "plan-and-configure",
    "everyday-tasks",
    "manage-and-automate",
    "reports-and-review",
    "reference-and-troubleshooting",
    "extensions-and-integrations",
}
STAGE_LABELS = {
    "overview": "Overview",
    "plan-and-configure": "Plan and configure",
    "everyday-tasks": "Everyday tasks",
    "manage-and-automate": "Manage and automate",
    "reports-and-review": "Reports and review",
    "reference-and-troubleshooting": "Reference and troubleshooting",
    "extensions-and-integrations": "Extensions and integrations",
}
STAGE_ORDER = {stage: index for index, stage in enumerate(STAGE_LABELS)}
CATEGORY_LABELS = {
    "tutorial": "Tutorials",
    "how-to": "How-to guides",
    "reference": "Reference",
    "explanation": "Explanation",
}
TOPIC_LABELS = {
    "contacts": "Contacts",
    "activities": "Activities",
    "groups-and-tags": "Groups and tags",
    "data-management": "Data management",
    "communication": "Communication",
    "mailings": "Mailings",
    "campaigns": "Campaigns",
    "contributions": "Contributions",
    "events": "Events",
    "memberships": "Memberships",
    "cases": "Cases",
    "grants": "Grants",
    "pledges": "Pledges",
    "search": "Search",
    "reporting": "Reporting",
    "searchkit": "SearchKit",
    "forms": "Forms",
    "configuration": "Configuration",
    "permissions": "Permissions",
    "custom-data": "Custom data",
    "installation": "Installation",
    "system-administration": "System administration",
    "extensions": "Extensions",
    "troubleshooting": "Troubleshooting",
    "general": "General",
}

ALLOWED_TOPICS = frozenset(TOPIC_LABELS)

TOPIC_ALIASES: Dict[str, str] = {
    "civicrm": "general",
    "core": "general",
    "civicrm-core": "general",
    "civimail": "mailings",
    "mailing": "mailings",
    "email": "mailings",
    "civievent": "events",
    "civicontribute": "contributions",
    "donations": "contributions",
    "payments": "contributions",
    "civimember": "memberships",
    "civicase": "cases",
    "civigrant": "grants",
    "civicampaign": "campaigns",
    "reports": "reporting",
    "form-builder": "forms",
    "formbuilder": "forms",
    "custom-fields": "custom-data",
    "administration": "system-administration",
    "sysadmin": "system-administration",
}

COMPONENT_BY_TOPIC = {
    "contacts": "CiviCRM Core",
    "activities": "CiviCRM Core",
    "groups-and-tags": "CiviCRM Core",
    "data-management": "CiviCRM Core",
    "communication": "CiviCRM Core",
    "mailings": "CiviMail",
    "campaigns": "CiviCampaign",
    "contributions": "CiviContribute",
    "events": "CiviEvent",
    "memberships": "CiviMember",
    "cases": "CiviCase",
    "grants": "CiviGrant",
    "pledges": "CiviContribute",
    "search": "CiviCRM Core",
    "reporting": "CiviReport",
    "searchkit": "SearchKit",
    "forms": "FormBuilder",
    "installation": "CiviCRM Core",
    "system-administration": "CiviCRM Core",
    "extensions": "CiviCRM Extensions",
}

CURATED_EXTENSIONS_START = "<!-- curated-extensions:start -->"
CURATED_EXTENSIONS_END = "<!-- curated-extensions:end -->"

CURATED_EXTENSIONS_REVIEWED_ON = "2026-10-09"

CURATED_EXTENSIONS: Dict[str, Dict[str, Any]] = {
    "memberships": {
        "label": "Membership",
        "category_id": 97,
        "extensions": [
            {
                "name": "Membership Extras",
                "url": "https://civicrm.org/extensions/membership-extras",
                "summary": (
                    "Adds instalment payments, order management, "
                    "offline renewals, and advanced membership changes."
                ),
            },
            {
                "name": "Membership Renewal Link",
                "url": "https://civicrm.org/extensions/membership-renewal-link",
                "summary": (
                    "Provides online membership renewal links, tokens, "
                    "and checksum validation."
                ),
            },
            {
                "name": "Membership Renewal Report",
                "url": "https://civicrm.org/extensions/membership-renewal-report",
                "summary": (
                    "Provides membership joining and renewal statistics "
                    "from historical CiviCRM data."
                ),
            },
            {
                "name": "CiviDiscount",
                "url": "https://civicrm.org/extensions/cividiscount",
                "summary": (
                    "Adds discount codes for membership and event pages."
                ),
            },
        ],
    },
    "events": {
        "label": "Events",
        "category_id": 98,
        "extensions": [
            {
                "name": "Advanced Events",
                "url": "https://civicrm.org/extensions/advanced-events",
                "summary": (
                    "Adds improved event templates, repeat-event tools, "
                    "search actions, and event administration features."
                ),
            },
            {
                "name": "CiviDiscount",
                "url": "https://civicrm.org/extensions/cividiscount",
                "summary": (
                    "Adds discount codes for event and membership pages."
                ),
            },
            {
                "name": "Event ICS",
                "url": "https://civicrm.org/extensions/event-ics",
                "summary": (
                    "Attaches calendar files to event confirmation emails."
                ),
            },
            {
                "name": "Custom Event Communication",
                "url": (
                    "https://civicrm.org/extensions/"
                    "custom-event-communication"
                ),
                "summary": (
                    "Sends event messages according to participant status, "
                    "role, language, and other conditions."
                ),
            },
            {
                "name": "Event Checkin",
                "url": "https://civicrm.org/extensions/event-checkin",
                "summary": (
                    "Provides event check-in links, QR codes, "
                    "and a remote check-in API."
                ),
            },
        ],
    },
    "contributions": {
        "label": "Contributions",
        "category_id": 94,
        "extensions": [
            {
                "name": "CiviContribute Recur Extra",
                "url": (
                    "https://civicrm.org/extensions/"
                    "civicontribute-recur-extra"
                ),
                "summary": (
                    "Adds tools and reports for recurring contributions."
                ),
            },
            {
                "name": "Invoice Helper",
                "url": "https://civicrm.org/extensions/invoice-helper",
                "summary": (
                    "Improves invoice emails and provides payment links "
                    "for pending contributions."
                ),
            },
            {
                "name": "Move Contribution",
                "url": (
                    "https://civicrm.org/extensions"
                    "?search=Move%20Contribution&category=94"
                ),
                "summary": (
                    "Moves an existing contribution from one contact "
                    "to another."
                ),
            },
            {
                "name": "Clone Contribution",
                "url": (
                    "https://civicrm.org/extensions"
                    "?search=Clone%20Contribution&category=94"
                ),
                "summary": (
                    "Creates a new contribution from an existing one."
                ),
            },
        ],
    },
}

DOMAIN_ORDER = [
    "Contacts and data",
    "Communication",
    "Fundraising and engagement",
    "Search and reporting",
    "Configure, automate and extend",
]
TOPIC_DOMAIN = {
    "contacts": "Contacts and data",
    "activities": "Contacts and data",
    "groups-and-tags": "Contacts and data",
    "data-management": "Contacts and data",
    "communication": "Communication",
    "mailings": "Communication",
    "campaigns": "Communication",
    "contributions": "Fundraising and engagement",
    "events": "Fundraising and engagement",
    "memberships": "Fundraising and engagement",
    "cases": "Fundraising and engagement",
    "grants": "Fundraising and engagement",
    "pledges": "Fundraising and engagement",
    "search": "Search and reporting",
    "reporting": "Search and reporting",
    "searchkit": "Search and reporting",
    "forms": "Search and reporting",
    "configuration": "Configure, automate and extend",
    "permissions": "Configure, automate and extend",
    "custom-data": "Configure, automate and extend",
    "installation": "Configure, automate and extend",
    "system-administration": "Configure, automate and extend",
    "extensions": "Configure, automate and extend",
    "troubleshooting": "Configure, automate and extend",
    "general": "Configure, automate and extend",
}

AUDIENCE_LABELS: Dict[str, str] = {
    "decision-maker": "Decision makers",
    "civicrm-user": "CiviCRM users",
    "functional-administrator": "Functional administrators",
    "data-and-reporting-specialist": "Data and reporting specialists",
    "system-administrator": "System administrators",
    "implementer": "Implementers and site builders",
    "developer": "Developers",
    "documentation-contributor": "Documentation contributors",
}

# Audience is a small, controlled reader taxonomy. Functional jobs such as
# event manager, fundraiser, or mailing author belong in topic/subtopic, not in
# a new audience branch.
AUDIENCE_ALIASES: Dict[str, str] = {
    "decision-maker": "decision-maker",
    "decision-makers": "decision-maker",
    "organisation-decision-maker": "decision-maker",
    "organisation-decision-makers": "decision-maker",
    "organizational-decision-maker": "decision-maker",
    "organizational-decision-makers": "decision-maker",
    "organisations-planning-to-use-civicrm": "decision-maker",
    "prospective-user": "decision-maker",
    "prospective-users": "decision-maker",

    "civicrm-user": "civicrm-user",
    "civicrm-users": "civicrm-user",
    "user": "civicrm-user",
    "users": "civicrm-user",
    "staff": "civicrm-user",
    "internal-user": "civicrm-user",
    "internal-users": "civicrm-user",
    "office-staff": "civicrm-user",
    "nonprofit-staff": "civicrm-user",
    "non-profit-staff": "civicrm-user",
    "volunteer": "civicrm-user",
    "volunteers": "civicrm-user",

    "functional-administrator": "functional-administrator",
    "functional-administrators": "functional-administrator",
    "power-user": "functional-administrator",
    "power-users": "functional-administrator",
    "form-builder": "functional-administrator",
    "form-builders": "functional-administrator",

    "data-and-reporting-specialist": "data-and-reporting-specialist",
    "data-importer": "data-and-reporting-specialist",
    "data-importers": "data-and-reporting-specialist",
    "report-user": "data-and-reporting-specialist",
    "report-users": "data-and-reporting-specialist",
    "report-builder": "data-and-reporting-specialist",
    "report-builders": "data-and-reporting-specialist",
    "search-builder": "data-and-reporting-specialist",
    "search-builders": "data-and-reporting-specialist",
    "searchkit-user": "data-and-reporting-specialist",
    "searchkit-users": "data-and-reporting-specialist",
    "search-kit-user": "data-and-reporting-specialist",
    "search-kit-users": "data-and-reporting-specialist",

    "system-administrator": "system-administrator",
    "system-administrators": "system-administrator",
    "site-administrator": "system-administrator",
    "site-administrators": "system-administrator",
    "website-administrator": "system-administrator",
    "website-administrators": "system-administrator",
    "technical-user": "system-administrator",
    "technical-users": "system-administrator",
    "technician": "system-administrator",
    "technicians": "system-administrator",
    "people-installing-civicrm": "system-administrator",

    "implementer": "implementer",
    "implementers": "implementer",
    "site-builder": "implementer",
    "site-builders": "implementer",
    "civicrm-site-builder": "implementer",
    "civicrm-site-builders": "implementer",
    "project-manager": "implementer",
    "project-managers": "implementer",

    "developer": "developer",
    "developers": "developer",
    "civicrm-developer": "developer",
    "civicrm-developers": "developer",

    "documentation-contributor": "documentation-contributor",
    "documentation-contributors": "documentation-contributor",
    "community-contributor": "documentation-contributor",
    "community-contributors": "documentation-contributor",
}

AUDIENCE_KEYWORDS: List[Tuple[str, Tuple[str, ...]]] = [
    ("developer", ("developer", "development", "api", "programmer", "code")),
    ("documentation-contributor", ("documentation", "manual", "contributor")),
    ("system-administrator", ("system administrator", "site administrator", "website administrator", "technical", "technician", "install")),
    ("data-and-reporting-specialist", ("report", "search", "searchkit", "data import", "data export", "analyst")),
    ("implementer", ("implementer", "site builder", "project manager", "configure profiles", "planning data")),
    ("functional-administrator", ("administrator", "manager", "organizer", "organiser", "builder", "power user")),
    ("decision-maker", ("decision maker", "planning to use", "prospective")),
    ("civicrm-user", ("user", "staff", "volunteer", "author", "worker")),
]


def canonical_audience(value: Any) -> str:
    candidate = slugify(str(value or ""))
    if not candidate:
        return ""
    direct = AUDIENCE_ALIASES.get(candidate)
    if direct:
        return direct
    words = candidate.replace("-", " ")
    for audience, terms in AUDIENCE_KEYWORDS:
        if any(term in words for term in terms):
            return audience
    return ""


def normalise_audiences(value: Any, guide: "GuideConfig") -> List[str]:
    result: List[str] = []
    for raw in normalise_list(value):
        audience = canonical_audience(raw)
        if audience and audience not in result:
            result.append(audience)
    if not result:
        result = ["system-administrator"] if guide.key in {"installation", "sysadmin"} else ["civicrm-user"]
    # One primary and, where useful, one secondary audience per page. The
    # global Browse section can therefore expose at most eight stable roles.
    return result[:2]


CATEGORY_ALIASES: Dict[str, str] = {
    "tutorial": "tutorial",
    "tutorials": "tutorial",
    "learning": "tutorial",

    "how-to": "how-to",
    "howto": "how-to",
    "how-to-guide": "how-to",
    "how-to-guides": "how-to",

    "explanation": "explanation",
    "explanations": "explanation",
    "concept": "explanation",
    "concepts": "explanation",

    "reference": "reference",
    "references": "reference",
}


def canonical_category(value: Any) -> str:
    """Return one canonical Diátaxis category."""

    candidate = slugify(
        str(value or "")
    )

    return CATEGORY_ALIASES.get(
        candidate,
        "",
    )

@dataclass(frozen=True)
class GuideConfig:
    key: str
    repository: str
    public_slug: str
    destination_prefix: str
    label: str


GUIDES: Dict[str, GuideConfig] = {
    "user-en": GuideConfig(
        "user-en",
        "https://lab.civicrm.org/documentation/docs/user-en.git",
        "user",
        "",
        "User guide",
    ),
    "installation": GuideConfig(
        "installation",
        "https://lab.civicrm.org/documentation/docs/installation.git",
        "installation",
        "installation",
        "Installation guide",
    ),
    "sysadmin": GuideConfig(
        "sysadmin",
        "https://lab.civicrm.org/documentation/docs/sysadmin.git",
        "sysadmin",
        "sysadmin",
        "System administrator guide",
    ),
}


@dataclass(frozen=True)
class Paths:
    root: Path
    upstream: Path
    rewritten: Path
    state: Path
    reports: Path
    site: Path

    def upstream_for(self, guide: GuideConfig) -> Path:
        return self.upstream / guide.key

    def rewritten_for(self, guide: GuideConfig) -> Path:
        return self.rewritten / guide.key


def make_paths(workspace: Path, output: Path) -> Paths:
    return Paths(
        root=workspace,
        upstream=workspace / "upstream",
        rewritten=workspace / "rewritten",
        state=workspace / "state",
        reports=output / "reports",
        site=output,
    )


def destination_path(guide: GuideConfig, relative_path: str) -> str:
    relative_path = relative_path.replace("\\", "/").lstrip("/")
    return (
        f"{guide.destination_prefix}/{relative_path}"
        if guide.destination_prefix
        else relative_path
    )


def run_command(
    command: Sequence[str],
    cwd: Optional[Path] = None,
    check: bool = True,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    print("$", " ".join(str(part) for part in command))
    return subprocess.run(
        [str(part) for part in command],
        cwd=str(cwd) if cwd else None,
        check=check,
        text=True,
        capture_output=capture_output,
    )


def require_program(name: str) -> None:
    if shutil.which(name) is None:
        raise RuntimeError(f"Required program is not available in PATH: {name}")


def _remove_readonly(function: Callable[..., Any], path: str, _: Any) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def safe_rmtree(path: Path, retries: int = 8, delay: float = 1.0) -> None:
    """Remove a directory with retries for transient Windows file locks."""
    if not path.exists():
        return
    last_error: Optional[BaseException] = None
    for attempt in range(1, retries + 1):
        try:
            shutil.rmtree(path, onerror=_remove_readonly)
            return
        except (PermissionError, OSError) as exc:
            last_error = exc
            if attempt == retries:
                break
            print(
                f"Warning: cannot remove {path} (attempt {attempt}/{retries}). "
                "Close MkDocs, Explorer previews, editors, and file watchers."
            )
            time.sleep(delay * attempt)
    raise RuntimeError(
        f"Could not remove {path}. Another process may still be using it: {last_error}"
    ) from last_error


def sync_repository(url: str, destination: Path, ref: Optional[str] = None) -> None:
    require_program("git")
    destination.parent.mkdir(parents=True, exist_ok=True)
    if (destination / ".git").is_dir():
        run_command(["git", "fetch", "--prune", "origin"], cwd=destination)
        if ref:
            run_command(["git", "checkout", ref], cwd=destination)
            run_command(["git", "pull", "--ff-only", "origin", ref], cwd=destination)
        else:
            run_command(["git", "pull", "--ff-only"], cwd=destination)
    elif destination.exists():
        raise RuntimeError(f"{destination} exists but is not a Git repository.")
    else:
        command = ["git", "clone", "--depth", "1"]
        if ref:
            command.extend(["--branch", ref])
        command.extend([url, str(destination)])
        run_command(command)


def iter_markdown(folder: Path) -> Iterable[Path]:
    if folder.exists():
        yield from sorted(folder.rglob("*.md"))


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_json(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()

def install_translator(
    site: Path,
    config: Dict[str, Any],
    endpoint: str,
    target_languages: List[str],
    source_language: str = "en",
) -> None:
    """Install a runtime LibreTranslate language switcher."""

    base_url = endpoint.strip().rstrip("/")

    if base_url.endswith("/translate"):
        base_url = base_url[: -len("/translate")]

    translator_config = {
        "baseUrl": base_url,
        "sourceLanguage": source_language,
        "targetLanguages": target_languages,
        "batchSize": 20,
    }

    js_directory = site / "docs" / "js"
    css_directory = site / "docs" / "css"

    js_directory.mkdir(parents=True, exist_ok=True)
    css_directory.mkdir(parents=True, exist_ok=True)

    javascript = r"""
(() => {
  "use strict";

  const config = __TRANSLATOR_CONFIG__;
  const translateEndpoint = `${config.baseUrl}/translate`;
  const languagesEndpoint = `${config.baseUrl}/languages`;
  const storageKey = "cividoc-language";

  const originalText = new WeakMap();
  const translationCache = new Map();

  const excludedSelector = [
    "script",
    "style",
    "pre",
    "code",
    "kbd",
    "samp",
    "textarea",
    "svg",
    "[data-no-translate]",
    ".no-translate",
    ".cividoc-language-switcher"
  ].join(",");

  let activeRequest = 0;
  let supportedLanguages = [];

  function storedLanguage() {
    try {
      return window.localStorage.getItem(storageKey) || config.sourceLanguage;
    } catch (_) {
      return config.sourceLanguage;
    }
  }

  function storeLanguage(language) {
    try {
      window.localStorage.setItem(storageKey, language);
    } catch (_) {
      // The switcher still works when storage is unavailable.
    }
  }

  async function loadSupportedLanguages() {
    try {
      const response = await fetch(languagesEndpoint, {
        headers: {
          "Accept": "application/json"
        }
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const payload = await response.json();

      if (!Array.isArray(payload)) {
        throw new Error("Invalid languages response");
      }

      const allowed = new Set([
        config.sourceLanguage,
        ...config.targetLanguages
      ]);

      supportedLanguages = payload
        .filter(item => item && allowed.has(item.code))
        .map(item => ({
          code: item.code,
          name: item.name || item.code,
          targets: Array.isArray(item.targets) ? item.targets : []
        }));

    } catch (error) {
      console.warn(
        "Could not load LibreTranslate languages:",
        error
      );

      supportedLanguages = [
        {
          code: config.sourceLanguage,
          name: "English",
          targets: config.targetLanguages
        },
        ...config.targetLanguages.map(code => ({
          code,
          name: code.toUpperCase(),
          targets: []
        }))
      ];
    }

    if (
      !supportedLanguages.some(
        language => language.code === config.sourceLanguage
      )
    ) {
      supportedLanguages.unshift({
        code: config.sourceLanguage,
        name: "English",
        targets: config.targetLanguages
      });
    }
  }

  function translatableTextNodes() {
    const roots = document.querySelectorAll(
      ".md-content, .md-nav, .md-header__topic"
    );

    const nodes = [];

    for (const root of roots) {
      const walker = document.createTreeWalker(
        root,
        NodeFilter.SHOW_TEXT,
        {
          acceptNode(node) {
            if (!node.nodeValue || !node.nodeValue.trim()) {
              return NodeFilter.FILTER_REJECT;
            }

            const parent = node.parentElement;

            if (!parent || parent.closest(excludedSelector)) {
              return NodeFilter.FILTER_REJECT;
            }

            return NodeFilter.FILTER_ACCEPT;
          }
        }
      );

      while (walker.nextNode()) {
        const node = walker.currentNode;

        if (!originalText.has(node)) {
          originalText.set(node, node.nodeValue);
        }

        nodes.push(node);
      }
    }

    return nodes;
  }

  function splitWhitespace(value) {
    const match = value.match(/^(\s*)([\s\S]*?)(\s*)$/);

    return {
      prefix: match ? match[1] : "",
      text: match ? match[2] : value,
      suffix: match ? match[3] : ""
    };
  }

  function restoreEnglish(nodes) {
    for (const node of nodes) {
      const original = originalText.get(node);

      if (typeof original === "string") {
        node.nodeValue = original;
      }
    }

    document.documentElement.lang = config.sourceLanguage;
  }

  async function requestTranslations(texts, targetLanguage) {
    const response = await fetch(translateEndpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify({
        q: texts,
        source: config.sourceLanguage,
        target: targetLanguage,
        format: "text"
      })
    });

    if (!response.ok) {
      const details = await response.text();

      throw new Error(
        `LibreTranslate returned HTTP ${response.status}: ${details}`
      );
    }

    const payload = await response.json();
    const translated = payload.translatedText;

    if (Array.isArray(translated)) {
      return translated;
    }

    if (typeof translated === "string" && texts.length === 1) {
      return [translated];
    }

    throw new Error("LibreTranslate returned an invalid response");
  }

  async function translatePage(targetLanguage) {
    const requestId = ++activeRequest;
    const nodes = translatableTextNodes();

    if (targetLanguage === config.sourceLanguage) {
      restoreEnglish(nodes);
      return;
    }

    const pending = [];

    for (const node of nodes) {
      const original = originalText.get(node);

      if (typeof original !== "string") {
        continue;
      }

      const parts = splitWhitespace(original);

      if (!parts.text.trim()) {
        continue;
      }

      pending.push({
        node,
        original,
        ...parts
      });
    }

    for (
      let start = 0;
      start < pending.length;
      start += config.batchSize
    ) {
      if (requestId !== activeRequest) {
        return;
      }

      const batch = pending.slice(
        start,
        start + config.batchSize
      );

      const missingTexts = [];
      const missingIndexes = [];

      batch.forEach((item, index) => {
        const cacheKey = `${targetLanguage}\u0000${item.text}`;

        if (!translationCache.has(cacheKey)) {
          missingTexts.push(item.text);
          missingIndexes.push(index);
        }
      });

      if (missingTexts.length) {
        const translations = await requestTranslations(
          missingTexts,
          targetLanguage
        );

        translations.forEach((translation, index) => {
          const batchIndex = missingIndexes[index];
          const sourceText = batch[batchIndex].text;
          const cacheKey = `${targetLanguage}\u0000${sourceText}`;

          translationCache.set(cacheKey, translation);
        });
      }

      if (requestId !== activeRequest) {
        return;
      }

      for (const item of batch) {
        const cacheKey = `${targetLanguage}\u0000${item.text}`;
        const translation = translationCache.get(cacheKey);

        if (typeof translation === "string") {
          item.node.nodeValue =
            item.prefix + translation + item.suffix;
        }
      }
    }

    document.documentElement.lang = targetLanguage;
  }

  function createLanguageSwitcher() {
    let wrapper = document.getElementById(
      "cividoc-language-switcher"
    );

    if (wrapper) {
      return wrapper.querySelector("select");
    }

    wrapper = document.createElement("div");
    wrapper.id = "cividoc-language-switcher";
    wrapper.className = "cividoc-language-switcher";
    wrapper.setAttribute("data-no-translate", "true");

    const label = document.createElement("label");
    label.className = "cividoc-language-label";
    label.setAttribute("for", "cividoc-language-select");
    label.textContent = "Language";

    const select = document.createElement("select");
    select.id = "cividoc-language-select";
    select.className = "cividoc-language-select";
    select.setAttribute("aria-label", "Select documentation language");

    for (const language of supportedLanguages) {
      select.add(
        new Option(
          language.name,
          language.code
        )
      );
    }

    const status = document.createElement("span");
    status.className = "cividoc-language-status";
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");

    select.value = storedLanguage();

    select.addEventListener("change", async () => {
      const targetLanguage = select.value;

      storeLanguage(targetLanguage);
      select.disabled = true;
      status.textContent = "Translating…";

      try {
        await translatePage(targetLanguage);
        status.textContent = "";
      } catch (error) {
        console.error(
          "LibreTranslate translation failed:",
          error
        );

        status.textContent =
          error instanceof Error
            ? `Translation failed: ${error.message}`
            : "Translation failed";

        select.value = config.sourceLanguage;
        storeLanguage(config.sourceLanguage);
        restoreEnglish(translatableTextNodes());
      } finally {
            select.disabled = false;
      }
    });

    wrapper.append(label, select, status);

    const header =
      document.querySelector(".md-header__inner") ||
      document.body;

    header.appendChild(wrapper);

    return select;
  }

  async function initialiseTranslator() {
    if (!supportedLanguages.length) {
      await loadSupportedLanguages();
    }

    const select = createLanguageSwitcher();
    const language = storedLanguage();

    if (
      !supportedLanguages.some(
        item => item.code === language
      )
    ) {
      storeLanguage(config.sourceLanguage);
      select.value = config.sourceLanguage;
      restoreEnglish(translatableTextNodes());
      return;
    }

    select.value = language;

    if (language !== config.sourceLanguage) {
      try {
        await translatePage(language);
      } catch (error) {
        console.error(
          "LibreTranslate translation failed:",
          error
        );

        select.value = config.sourceLanguage;
        storeLanguage(config.sourceLanguage);
        restoreEnglish(translatableTextNodes());
          }
  }

  function startTranslator() {
    initialiseTranslator().catch(error => {
      console.error(
        "LibreTranslate initialisation failed:",
        error
      );
    });
  }

  if (
    typeof document$ !== "undefined" &&
    document$ &&
    typeof document$.subscribe === "function"
  ) {
    document$.subscribe(startTranslator);
  } else if (
    document.readyState === "loading"
  ) {
    document.addEventListener(
      "DOMContentLoaded",
      startTranslator,
      { once: true }
    );
  } else {
    startTranslator();
  }
})();
""".replace(
        "__TRANSLATOR_CONFIG__",
        json.dumps(
            translator_config,
            ensure_ascii=False,
        ),
    )

    stylesheet = """
.cividoc-language-switcher {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  margin-left: auto;
  padding: 0 0.5rem;
  color: var(--md-primary-bg-color);
  font-size: 0.7rem;
}

.cividoc-language-label {
  white-space: nowrap;
}

.cividoc-language-select {
  min-height: 2rem;
  max-width: 10rem;
  padding: 0.2rem 1.7rem 0.2rem 0.5rem;
  border: 1px solid currentColor;
  border-radius: 0.2rem;
  color: var(--md-default-fg-color);
  background: var(--md-default-bg-color);
}

.cividoc-language-select:focus-visible {
  outline: 2px solid var(--md-accent-fg-color);
  outline-offset: 2px;
}

.cividoc-language-status {
  min-width: 1rem;
  white-space: nowrap;
  font-size: 0.65rem;
}

@media screen and (max-width: 44.984375em) {
  .cividoc-language-label,
  .cividoc-language-status {
    display: none;
  }

  .cividoc-language-switcher {
    padding: 0;
  }

  .cividoc-language-select {
    max-width: 7rem;
  }
}
""".strip()

    javascript_path = (
        js_directory
        / "libretranslate-language-switcher.js"
    )

    stylesheet_path = (
        css_directory
        / "libretranslate-language-switcher.css"
    )

    javascript_path.write_text(
        javascript + "\n",
        encoding="utf-8",
    )

    stylesheet_path.write_text(
        stylesheet + "\n",
        encoding="utf-8",
    )

    extra_javascript = config.setdefault(
        "extra_javascript",
        [],
    )

    script_name = (
        "js/libretranslate-language-switcher.js"
    )

    if script_name not in extra_javascript:
        extra_javascript.append(script_name)

    extra_css = config.setdefault(
        "extra_css",
        [],
    )

    stylesheet_name = (
        "css/libretranslate-language-switcher.css"
    )

    if stylesheet_name not in extra_css:
        extra_css.append(stylesheet_name)

def effective_page_source(
    paths: Paths,
    guide: GuideConfig,
    relative_path: str,
) -> Path:
    """Return the rewritten page when available, otherwise the official page."""

    rewritten = (
        paths.rewritten_for(guide)
        / Path(relative_path)
    )

    if rewritten.exists():
        return rewritten

    return (
        paths.upstream_for(guide)
        / "docs"
        / Path(relative_path)
    )

def split_front_matter(text: str) -> Tuple[Dict[str, Any], str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    if not text.startswith("---\n"):
        return {}, text.lstrip()
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text.lstrip()
    try:
        loaded = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}, text.lstrip()
    if not isinstance(loaded, dict):
        return {}, text.lstrip()
    return dict(loaded), text[end + 5:].lstrip("\n")


def build_markdown_with_front_matter(metadata: Dict[str, Any], body: str) -> str:
    front = yaml.safe_dump(
        metadata,
        sort_keys=False,
        allow_unicode=True,
        width=120,
    ).strip()
    return f"---\n{front}\n---\n\n{body.strip()}\n"

def remove_curated_extensions_section(body: str) -> str:
    """Remove a previously generated curated extensions section."""

    pattern = re.compile(
        rf"\n*{re.escape(CURATED_EXTENSIONS_START)}"
        rf".*?"
        rf"{re.escape(CURATED_EXTENSIONS_END)}\n*",
        flags=re.DOTALL,
    )

    return pattern.sub("\n\n", body).strip()


def curated_extensions_directory_url(
    category_id: int,
) -> str:
    """Return the official filtered CiviCRM extensions directory URL."""

    return (
        "https://civicrm.org/extensions"
        f"?search=&category={category_id}"
    )


def render_curated_extensions_section(
    topic: str,
) -> str:
    """Render the curated extensions section for a functional topic."""

    configuration = CURATED_EXTENSIONS.get(topic)

    if not configuration:
        return ""

    label = str(configuration["label"])
    category_id = int(configuration["category_id"])
    extensions = list(configuration.get("extensions", []))[:5]

    if not extensions:
        return ""

    lines = [
        CURATED_EXTENSIONS_START,
        "## Common extensions",
        "",
        (
            f"The following commonly used {label.lower()} extensions "
            "may be useful when the corresponding functionality is "
            "not available in CiviCRM core."
        ),
        "",
    ]

    for extension in extensions:
        name = str(extension["name"]).strip()
        url = str(extension["url"]).strip()
        summary = str(extension["summary"]).strip()

        lines.append(
            f"- [{name}]({url}) — {summary}"
        )

    directory_url = curated_extensions_directory_url(
        category_id
    )

    lines.extend(
        [
            "",
            (
                f"[Browse all {label.lower()} extensions]"
                f"({directory_url})"
            ),
            "",
            (
                "Check the extension's development status, current "
                "CiviCRM compatibility, CMS requirements, and release "
                "notes before installing it."
            ),
            "",
            (
                "Editorial selection last reviewed: "
                f"{CURATED_EXTENSIONS_REVIEWED_ON}."
            ),
            CURATED_EXTENSIONS_END,
        ]
    )

    return "\n".join(lines)


def insert_curated_extensions_section(
    body: str,
    section: str,
) -> str:
    """Insert a generated extensions section before the source comment."""

    clean_body = remove_curated_extensions_section(body)

    if not section:
        return clean_body

    source_pattern = re.compile(
        r"(?im)^\s*<!--\s*Source:.*?-->\s*$"
    )

    match = source_pattern.search(clean_body)

    if not match:
        return (
            f"{clean_body.rstrip()}\n\n"
            f"{section.strip()}\n"
        )

    before = clean_body[:match.start()].rstrip()
    source_comment = clean_body[match.start():].strip()

    return (
        f"{before}\n\n"
        f"{section.strip()}\n\n"
        f"{source_comment}\n"
    )


def curated_extensions_candidate_score(
    metadata: Dict[str, Any],
) -> int:
    """
    Rank rewritten pages for receiving a curated extensions section.

    Prefer a dedicated extensions page, then a component entry page,
    then another overview page. Ordinary task pages are not eligible.
    """

    stage = str(
        metadata.get("journey_stage", "")
    ).strip()

    title = str(
        metadata.get("title", "")
    ).strip().casefold()

    if stage == "extensions-and-integrations":
        return 0

    if title.startswith("what is "):
        return 1

    if stage == "overview":
        return 2

    return 100


def add_curated_extensions_to_rewritten_pages(
    paths: Paths,
    guides: List[GuideConfig],
) -> None:
    """
    Add one curated extensions section per eligible functional topic.

    Only AI-rewritten files are considered. Official source files are
    never modified. Existing generated sections are removed first so
    the operation remains idempotent.
    """

    pages_by_topic: Dict[
        str,
        List[
            Tuple[
                int,
                int,
                Path,
                Dict[str, Any],
                str,
            ]
        ],
    ] = defaultdict(list)

    cleaned_pages: List[
        Tuple[
            Path,
            Dict[str, Any],
            str,
        ]
    ] = []

    sequence = 0

    for guide in guides:
        rewritten_root = paths.rewritten_for(guide)

        if not rewritten_root.exists():
            continue

        for page in iter_markdown(rewritten_root):
            raw = page.read_text(
                encoding="utf-8-sig"
            )

            metadata, body = split_front_matter(raw)
            clean_body = remove_curated_extensions_section(body)

            cleaned_pages.append(
                (
                    page,
                    metadata,
                    clean_body,
                )
            )

            topic = str(
                metadata.get("topic", "")
            ).strip()

            if topic not in CURATED_EXTENSIONS:
                continue

            score = curated_extensions_candidate_score(
                metadata
            )

            if score >= 100:
                continue

            pages_by_topic[topic].append(
                (
                    score,
                    sequence,
                    page,
                    metadata,
                    clean_body,
                )
            )

            sequence += 1

    # Remove stale generated sections before selecting new target pages.
    for page, metadata, clean_body in cleaned_pages:
        page.write_text(
            build_markdown_with_front_matter(
                metadata,
                clean_body,
            ),
            encoding="utf-8",
        )

    for topic, candidates in pages_by_topic.items():
        candidates.sort(
            key=lambda item: (
                item[0],
                item[1],
            )
        )

        _, _, page, metadata, body = candidates[0]

        section = render_curated_extensions_section(
            topic
        )

        enriched_body = insert_curated_extensions_section(
            body,
            section,
        )

        page.write_text(
            build_markdown_with_front_matter(
                metadata,
                enriched_body,
            ),
            encoding="utf-8",
        )

        print(
            "Added curated extensions section: "
            f"{topic} -> {page}"
        )

def collapse_single_child_sections(nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Remove every section that merely hides one child."""
    compacted: List[Dict[str, Any]] = []
    for node in nodes:
        if not isinstance(node, dict):
            continue
        if set(node) == {"page_id"}:
            compacted.append({"page_id": str(node["page_id"])})
            continue
        if set(node) != {"title", "children"}:
            compacted.append(node)
            continue
        children = collapse_single_child_sections(list(node.get("children", [])))
        if not children:
            continue
        if len(children) == 1:
            compacted.extend(children)
            continue
        compacted.append({"title": str(node.get("title", "")).strip(), "children": children})
    return compacted

def navigation_depth(
    nodes: List[Dict[str, Any]],
    depth: int = 1,
) -> int:
    """Return the maximum depth of a navigation tree."""

    maximum = depth

    for node in nodes:
        children = node.get("children", [])

        if isinstance(children, list) and children:
            maximum = max(
                maximum,
                navigation_depth(children, depth + 1),
            )

    return maximum


def enforce_navigation_depth_limit(
    nodes: List[Dict[str, Any]],
    max_depth: int = 5,
) -> List[Dict[str, Any]]:
    """Collapse nested single-child branches until the tree fits."""

    current = nodes

    for _ in range(10):
        if navigation_depth(current) <= max_depth:
            return current

        updated = collapse_single_child_sections(current)

        if updated == current:
            break

        current = updated

    if navigation_depth(current) > max_depth:
        raise RuntimeError(
            "Invalid navigation plan: more than five navigation levels "
            "even after compaction."
        )

    return current

def markdown_title(body: str, fallback: str) -> str:
    match = re.search(r"(?m)^#\s+(.+?)\s*#*\s*$", body)
    if not match:
        return fallback
    title = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", match.group(1))
    return re.sub(r"[*_`]", "", title).strip()


def infer_summary(body: str) -> str:
    for block in re.split(r"\n\s*\n", body):
        candidate = block.strip()
        if not candidate or candidate.startswith(("#", "<!--", "```", "!!!")):
            continue
        candidate = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", candidate)
        candidate = re.sub(r"[*_`]", "", candidate)
        candidate = re.sub(r"\s+", " ", candidate).strip()
        if candidate:
            suffix = "" if candidate.endswith((".", "!", "?")) else "."
            return candidate[:240].rstrip(" ,;:") + suffix
    return "CiviCRM documentation page."


def slugify(value: str) -> str:
    value = value.casefold().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "general"


def normalise_list(value: Any) -> List[str]:
    if value is None:
        return []
    values = [value] if isinstance(value, str) else list(value) if isinstance(value, (list, tuple, set)) else [str(value)]
    result: List[str] = []
    for item in values:
        text = str(item).strip()
        if text and text not in result:
            result.append(text)
    return result


def official_legacy_url(
    guide: GuideConfig,
    relative_path: str,
    language: str = "en",
    version: str = "latest",
) -> str:
    path = PurePosixPath(relative_path)
    page = path.parent.as_posix() if path.name.casefold() == "index.md" else path.with_suffix("").as_posix()
    page = page.strip("./")
    base = f"https://docs.civicrm.org/{guide.public_slug}/{language}/{version}/"
    return base if not page else f"{base}{page}/"


def git_value(repository: Path, relative_path: str, format_value: str) -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--follow", f"--format={format_value}", "--", relative_path],
        cwd=str(repository),
        check=False,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def selected_path(
    guide_key: str,
    relative_path: str,
    includes: List[str],
    excludes: List[str],
) -> bool:
    candidates = [relative_path, f"{guide_key}:{relative_path}", f"{guide_key}/{relative_path}"]

    def matches(rule: str) -> bool:
        rule = rule.replace("\\", "/").strip("/")
        return any(value == rule or value.startswith(rule.rstrip("/") + "/") for value in candidates)

    if includes and not any(matches(rule) for rule in includes):
        return False
    return not any(matches(rule) for rule in excludes)


REWRITE_PROMPT = r"""
You are editing official CiviCRM documentation. Rewrite the supplied Markdown
only when doing so improves structure, clarity, and findability.

SOURCE AUTHORITY
- The supplied source page is your only authority on how CiviCRM works.
- Do not add steps, options, facts, prerequisites, warnings, interface behaviour,
  or links that are not in the source.
- Do not leave out any source step, option, limitation, warning, example, code
  block, table, image, anchor, or meaningful link.
- Keep menu paths, field names, button labels, command names, configuration keys,
  placeholders, code literals, link targets, image targets, and URLs exactly as
  written.
- If something is unclear, contradictory, or appears out of date, leave the
  content unchanged and describe the problem in review_notes. Do not correct it.
- Never infer current product behaviour from general knowledge.

PAGE PURPOSE
Classify each output page as exactly one of:
- tutorial: a guided learning experience;
- how-to: directions for completing a real task;
- reference: accurate lookup information about the product;
- explanation: concepts, relationships, context, or trade-offs.

CLASSIFICATION EVIDENCE
- tutorial: a learning-oriented walkthrough, worked example, quick start, or
  guided first experience. Examples and end-to-end demonstrations are normally
  tutorials even when they contain steps.
- how-to: directions that help an already oriented reader complete one concrete
  real-world task. Imperative procedures are normally how-to guides.
- reference: lookup material such as fields, options, settings, permissions,
  tokens, requirements, commands, statuses, APIs, tables, or exhaustive lists.
- explanation: concepts, architecture, background, relationships, rationale,
  lifecycle, planning, or trade-offs. "What is ...?" pages are normally explanations.
- Never default to reference merely because a page is not numbered.
- Classify every split output independently. When a long source contains
  substantial self-contained material with genuinely different purposes, split
  it; do not split short fragments or create placeholder pages.

Split a source page only when it contains substantial material serving different
reader needs. Use exactly this marker between complete pages:

=== NEW PAGE ===

The first output page keeps the source path and official URL. Additional pages
receive generated sibling paths. Do not use Part 1 or Part 2 in titles.

FRONT MATTER
Start every page at its first character with this YAML schema:
---
title: Clear page title
category: tutorial|how-to|reference|explanation
topic: stable functional topic
subtopic: semantic subgroup
component: CiviCRM component or feature
audiences:
  - primary-reader
level: basic|intermediate|advanced
journey_stage: overview|plan-and-configure|everyday-tasks|manage-and-automate|reports-and-review|reference-and-troubleshooting|extensions-and-integrations
summary: One clear sentence describing the page benefit.
extensions: []
related: []
review_priority: low|medium|high
review_notes: []
---

Metadata guidance:
- Use a stable task or feature topic, not a book name.
- Use subtopic for the semantic group inside the topic.
- Use audiences as metadata, never as the page's exclusive location.
- Use only these audience ids: decision-maker, civicrm-user,
  functional-administrator, data-and-reporting-specialist, system-administrator,
  implementer, developer, documentation-contributor.
- Assign one primary audience and at most one secondary audience. Product jobs
  such as event manager, fundraiser, campaign organiser, or mailing author are
  topics/subtopics, not new audience ids.
- Use extensions only when the source explicitly identifies an extension.
- Use related only for source paths or valid links explicitly supported by the
  source; never invent a target.
- A page titled "What is CiviX?" normally has journey_stage: overview. Preserve
  that title and keep it as the component entry page.

REVIEW PRIORITY
Set review_priority only from review_notes:
- high: a reader could be misled or unable to complete a task. Examples include
  a required image that cannot be replaced with words, a contradiction, or an
  interface or feature that looks obsolete.
- medium: the page remains usable but has signs of age or gaps, such as a
  version number, a feature described as new, or an unclear passage.
- low: review_notes is empty or contains only minor wording points.

WRITING
- Write in clear, inclusive, professional English.
- Preserve one H1 and use sentence case for headings.
- Preserve old explicit heading IDs. If a heading is renamed, place
  <a id="old-anchor"></a> immediately before the new heading.
- Keep paragraphs short. Use numbered lists only when order matters.
- Do not add filler, marketing claims, or a repetitive conclusion.
- End each output with exactly one comment: <!-- Source: SOURCE_PATH -->
- Return Markdown only, without an outer code fence.
""".strip()

FIDELITY_CORRECTION_PROMPT = r"""
CORRECTION REQUIRED

Your previous response failed source-fidelity validation:

{error}

Generate the complete page again. Restore every missing source element exactly,
especially Markdown link targets, image references, warnings, limitations, code
blocks, inline code, anchors, menu paths, field names, button labels,
configuration values, placeholders, and technical literals.

Do not explain the correction. Return only the complete rewritten Markdown.
""".strip()


def strip_outer_fence(text: str, language: str = "") -> str:
    text = text.strip().lstrip("\ufeff")
    match = re.fullmatch(
        rf"```(?:{language}|markdown|md|json)?\s*\n([\s\S]*?)\n```",
        text,
        flags=re.IGNORECASE,
    )
    return match.group(1).strip() if match else text


def ai_request(
    prompt: str,
    provider: str,
    model: str,
    preset: str,
    retries: int,
    json_response: bool = False,
) -> str:
    for attempt in range(1, retries + 1):
        try:
            if provider == "perplexity":
                try:
                    from perplexity import Perplexity
                except ImportError as exc:
                    raise RuntimeError(
                        "The official 'perplexityai' package is required. "
                        "Run: pip install --upgrade perplexityai"
                    ) from exc
                key = os.getenv("PERPLEXITY_API_KEY", "").strip()
                if not key:
                    raise RuntimeError("PERPLEXITY_API_KEY is missing.")
                client = Perplexity(api_key=key, timeout=900.0, max_retries=0)
                response = client.responses.create(preset=preset, input=prompt)
                if response.status != "completed":
                    raise RuntimeError(f"Perplexity response status: {response.status}")
                result = response.output_text or ""
            elif provider == "openai":
                try:
                    from openai import OpenAI
                except ImportError as exc:
                    raise RuntimeError("The 'openai' package is required.") from exc
                key = os.getenv("OPENAI_API_KEY", "").strip()
                if not key:
                    raise RuntimeError("OPENAI_API_KEY is missing.")
                if not model:
                    raise RuntimeError("--model or CIVIDOC_MODEL is required with OpenAI.")
                kwargs: Dict[str, Any] = {"api_key": key, "timeout": 900.0}
                base_url = os.getenv("OPENAI_BASE_URL", "").strip()
                if base_url:
                    kwargs["base_url"] = base_url
                request: Dict[str, Any] = {
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                }
                if json_response:
                    request["response_format"] = {"type": "json_object"}
                response = OpenAI(**kwargs).chat.completions.create(**request)
                result = response.choices[0].message.content or ""
            else:
                raise RuntimeError(f"Unknown AI provider: {provider}")
            if not result.strip():
                raise RuntimeError("The AI returned an empty response.")
            return strip_outer_fence(result, "json" if json_response else "markdown")
        except Exception as exc:
            if attempt >= retries:
                raise RuntimeError(f"AI request failed after {retries} attempts: {exc}") from exc
            wait = min(60, 2 ** attempt)
            print(f"AI request failed ({attempt}/{retries}); retrying in {wait}s: {exc}")
            time.sleep(wait)
    raise AssertionError("unreachable")


def markdown_link_targets(text: str) -> List[str]:
    targets: List[str] = []
    for target in re.findall(r"!?\[[^]]*]\(([^)\s]+)", text):
        targets.append(target.strip("<>"))
    for target in re.findall(r"(?m)^\s*\[[^]]+]:\s*(\S+)", text):
        targets.append(target.strip("<>"))
    return targets


def image_targets(text: str) -> List[str]:
    return [target.strip("<>") for target in re.findall(r"!\[[^]]*]\(([^)\s]+)", text)]


def fenced_blocks(text: str) -> List[str]:
    return [match.group(0).strip() for match in re.finditer(r"(?ms)^```.*?^```\s*$", text)]


def inline_literals(text: str) -> List[str]:
    return [value for value in re.findall(r"`([^`\n]+)`", text) if value.strip()]


def explicit_anchors(text: str) -> List[str]:
    html_ids = re.findall(r"(?i)<a\s+[^>]*id=[\"']([^\"']+)[\"'][^>]*>", text)
    attr_ids = re.findall(r"(?m)^#{1,6}\s+.*?\s+\{#([^}]+)\}\s*$", text)
    return html_ids + attr_ids


def validate_source_fidelity(source: str, outputs: List[str], source_path: str) -> None:
    combined = "\n\n".join(outputs)
    problems: List[str] = []
    checks: List[Tuple[str, List[str], Callable[[str], List[str]]]] = [
        ("image targets", image_targets(source), image_targets),
        ("link targets", markdown_link_targets(source), markdown_link_targets),
        ("fenced code blocks", fenced_blocks(source), fenced_blocks),
        ("inline technical literals", inline_literals(source), inline_literals),
        ("explicit anchors", explicit_anchors(source), explicit_anchors),
    ]
    for label, values, extractor in checks:
        source_counts = Counter(values)
        output_counts = Counter(extractor(combined))
        missing = [value for value, count in source_counts.items() if output_counts[value] < count]
        if missing:
            sample = ", ".join(repr(value[:100]) for value in missing[:5])
            problems.append(f"missing {label}: {sample}")
    if problems:
        raise RuntimeError(
            f"Source fidelity validation failed for {source_path}: " + "; ".join(problems)
        )


def review_priority_from_notes(notes: List[str]) -> str:
    if not notes:
        return "low"
    text = " ".join(notes).casefold()
    high_terms = (
        "contradict", "obsolete", "mislead", "cannot complete", "unable to complete",
        "missing step", "required image", "key step", "broken procedure",
    )
    medium_terms = (
        "version", "described as new", "unclear", "ambiguous", "dated", "old interface",
        "sign of age", "incomplete context",
    )
    if any(term in text for term in high_terms):
        return "high"
    if any(term in text for term in medium_terms):
        return "medium"
    return "low"


def infer_topic(guide: GuideConfig, relative_path: str, title: str, metadata: Dict[str, Any]) -> str:
    supplied = slugify(
        str(metadata.get("topic", ""))
        if metadata.get("topic")
        else ""
    )

    supplied = TOPIC_ALIASES.get(
        supplied,
        supplied,
    )

    # Accept only canonical topics. An AI-generated free-form topic must not
    # become a new primary navigation branch.
    if supplied in ALLOWED_TOPICS:
        return supplied
    haystack = f"{relative_path} {title}".casefold()
    patterns = [
        ("events", ("event", "participant", "civievent")),
        ("contributions", ("contribution", "payment", "civicontribute", "financial")),
        ("memberships", ("membership", "civimember")),
        ("mailings", ("mailing", "civimail", "email")),
        ("campaigns", ("campaign", "civicampaign", "survey", "petition")),
        ("cases", ("case", "civicase")),
        ("grants", ("grant", "civigrant")),
        ("pledges", ("pledge",)),
        ("searchkit", ("searchkit", "formbuilder", "form builder")),
        ("reporting", ("report", "dashboard")),
        ("search", ("search", "find ")),
        ("custom-data", ("custom field", "custom data", "profile")),
        ("permissions", ("permission", "access control", "acl")),
        ("extensions", ("extension",)),
        ("activities", ("activity", "activities")),
        ("groups-and-tags", ("group", "tag")),
        ("data-management", ("import", "export", "dedup", "merge", "undelete", "trash")),
        ("contacts", ("contact", "individual", "household", "organization")),
        ("forms", ("form",)),
        ("configuration", ("configuration", "configure", "setting")),
        ("troubleshooting", ("troubleshoot", "error", "debug")),
    ]
    if guide.key == "installation":
        return "installation"
    if guide.key == "sysadmin":
        return "extensions" if "extension" in haystack else "system-administration"
    for topic, terms in patterns:
        if any(term in haystack for term in terms):
            return topic
    return "general"


def infer_category(metadata: Dict[str, Any], body: str) -> str:
    """Infer one Diátaxis category from purpose, title and page structure."""
    explicit = canonical_category(metadata.get("category"))
    if not explicit:
        values = normalise_list(metadata.get("categories"))
        explicit = canonical_category(values[0]) if values else ""
    if explicit:
        return explicit

    title = str(metadata.get("title", "")).strip()
    if not title:
        title = markdown_title(body, "")
    title_text = title.casefold()
    text = f"{title}\n{body[:12000]}".casefold()

    if re.search(r"\b(tutorial|walkthrough|worked example|quick start|getting started|first steps)\b", title_text):
        return "tutorial"
    if title_text.startswith(("example ", "create your first ", "build your first ")):
        return "tutorial"

    if title_text.startswith(("what is ", "why ", "understanding ")):
        return "explanation"
    if re.search(r"\b(concepts?|architecture|overview|background|how .+ works?|planning|lifecycle|trade-offs?)\b", title_text):
        return "explanation"

    task_verbs = (
        "add", "allow", "archive", "backup", "build", "cancel", "change",
        "configure", "connect", "create", "customize", "define", "delete",
        "display", "edit", "enable", "export", "find", "handle", "import",
        "install", "integrate", "manage", "migrate", "move", "optimize",
        "override", "plan", "publish", "record", "renew", "run", "send",
        "set up", "switch", "sync", "translate", "troubleshoot", "update",
        "upgrade", "use", "view",
    )
    ordered_steps = len(re.findall(r"(?m)^\s*\d+[.)]\s+", body))
    procedural_headings = len(re.findall(
        r"(?mi)^#{2,6}\s+(before you begin|prerequisites?|procedure|steps?|to .+|how to .+)",
        body,
    ))
    if title_text.startswith(task_verbs) or ordered_steps >= 2 or procedural_headings:
        return "how-to"

    if re.search(r"\b(reference|glossary|requirements?|permissions?|fields?|options?|settings?|tokens?|commands?|api|schema|status|statuses)\b", title_text):
        return "reference"
    if len(re.findall(r"(?m)^\|.+\|\s*$", body)) >= 3:
        return "reference"
    if re.search(r"(?mi)^#{2,6}\s+(available|supported|values?|parameters?|configuration options|reference)", body):
        return "reference"

    if re.search(r"\b(example|scenario|exercise|learn to|follow along)\b", text):
        return "tutorial"
    if re.search(r"\b(because|concept|means that|in contrast|relationship between)\b", text):
        return "explanation"
    return "reference"

def infer_journey_stage(title: str, category: str, relative_path: str, metadata: Dict[str, Any]) -> str:
    supplied = slugify(str(metadata.get("journey_stage", metadata.get("journey", ""))))
    supplied = {
        "discover": "overview", "understand": "overview", "prepare": "plan-and-configure",
        "configure": "plan-and-configure", "use": "everyday-tasks", "operate": "everyday-tasks",
        "manage": "manage-and-automate", "automate": "manage-and-automate",
        "review": "reports-and-review", "report": "reports-and-review",
        "resolve": "reference-and-troubleshooting", "troubleshoot": "reference-and-troubleshooting",
        "integrate": "extensions-and-integrations",
    }.get(supplied, supplied)
    if supplied in ALLOWED_JOURNEY_STAGES:
        return supplied
    haystack = f"{title} {relative_path}".casefold()
    if title.casefold().startswith("what is "):
        return "overview"
    if any(term in haystack for term in ("extension", "integration", "integrate")):
        return "extensions-and-integrations"
    if any(term in haystack for term in ("report", "search", "review", "find ", "dashboard")):
        return "reports-and-review"
    if any(term in haystack for term in ("troubleshoot", "error", "status", "permission", "reference")):
        return "reference-and-troubleshooting"
    if any(term in haystack for term in ("bulk", "batch", "automate", "scheduled", "workflow", "manage")):
        return "manage-and-automate"
    if any(term in haystack for term in ("configure", "configuration", "setup", "set up", "plan", "template", "option")):
        return "plan-and-configure"
    if category in {"reference", "explanation"}:
        return "reference-and-troubleshooting"
    return "everyday-tasks"


def normalise_metadata(
    metadata: Dict[str, Any],
    body: str,
    destination: str,
    guide: GuideConfig,
    source_path: str,
    source_repository: str,
    source_commit: str = "",
    last_modified: str = "",
    civicrm_versions: Optional[List[str]] = None,
    legacy_urls: Optional[List[str]] = None,
) -> Dict[str, Any]:
    fallback = PurePosixPath(destination).stem.replace("-", " ").replace("_", " ").strip().capitalize()
    title = resolve_page_title(
    metadata,
    body,
    source_path,
) or markdown_title(
    body,
    fallback,
)
    category = canonical_category(
        metadata.get("category")
    )

    if not category:
        category = canonical_category(
            infer_category(
                metadata,
                body,
            )
        )

    if not category:
        category = "how-to"

    metadata["category"] = category
    topic = infer_topic(guide, source_path, title, metadata)
    subtopic = slugify(str(metadata.get("subtopic", ""))) if metadata.get("subtopic") else ""
    if not subtopic or subtopic == "general":
        parent = PurePosixPath(source_path).parent.name
        subtopic = slugify(parent) if parent and parent != "." else topic
    component = str(metadata.get("component", "")).strip() or COMPONENT_BY_TOPIC.get(topic, "CiviCRM Core")
    audiences = normalise_audiences(
        metadata.get("audiences", metadata.get("audience")),
        guide,
    )
    level = str(metadata.get("level", "basic")).strip().casefold()
    if level not in ALLOWED_LEVELS:
        level = "basic"
    notes = normalise_list(metadata.get("review_notes"))
    result: Dict[str, Any] = {
        "title": title,
        "category": category,
        "topic": topic,
        "subtopic": subtopic,
        "component": component,
        "audiences": audiences,
        "level": level,
        "journey_stage": infer_journey_stage(title, category, source_path, metadata),
        "summary": str(metadata.get("summary", "")).strip() or infer_summary(body),
        "extensions": normalise_list(metadata.get("extensions")),
        "related": normalise_list(metadata.get("related")),
        "review_priority": review_priority_from_notes(notes),
        "review_notes": notes,
        "guide": guide.key,
        "source_repository": source_repository,
        "source_path": source_path,
        "destination_path": destination,
        "legacy_urls": list(dict.fromkeys(legacy_urls or [official_legacy_url(guide, source_path)])),
        "civicrm_version": civicrm_versions or normalise_list(metadata.get("civicrm_version")) or ["latest"],
    }
    if source_commit:
        result["source_commit"] = source_commit
    if last_modified:
        result["last_modified"] = last_modified
    return result


def load_civicrm_versions(csv_path: Optional[Path]) -> List[Dict[str, str]]:
    if not csv_path or not csv_path.exists():
        return []
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def detect_civicrm_versions(rows: List[Dict[str, str]], source: str) -> List[str]:
    haystack = source.casefold()
    matches: List[str] = []
    for row in rows:
        for key in ("version", "series", "label", "name"):
            value = str(row.get(key, "")).strip()
            if value and value.casefold() in haystack and value not in matches:
                matches.append(value)
    return matches or ["latest"]


def split_rewrite_pages(answer: str, source_key: str) -> List[str]:
    chunks = [
        item.strip()
        for item in re.split(r"(?m)^=== NEW PAGE ===\s*$", answer)
        if item.strip()
    ]
    if not chunks:
        raise RuntimeError(f"The AI produced no page for {source_key}.")
    return chunks


def rewrite_documents(
    paths: Paths,
    guides: List[GuideConfig],
    provider: str,
    model: str,
    preset: str,
    retries: int,
    fidelity_attempts: int,
    includes: List[str],
    excludes: List[str],
    limit: int,
    skip_existing: bool,
    versions_csv: Optional[Path],
) -> None:
    """Rewrite selected pages, retry fidelity failures, and preserve rejected sources."""
    manifest_path = paths.state / "rewrite-manifest.json"
    manifest = load_json(manifest_path)
    manifest["pipeline_version"] = PIPELINE_VERSION
    entries = manifest.setdefault("files", {})
    version_rows = load_civicrm_versions(versions_csv)
    processed = 0

    for guide in guides:
        repository = paths.upstream_for(guide)
        docs_root = repository / "docs"
        output_root = paths.rewritten_for(guide)
        output_root.mkdir(parents=True, exist_ok=True)

        for source in iter_markdown(docs_root):
            relative = source.relative_to(docs_root).as_posix()
            if not selected_path(guide.key, relative, includes, excludes):
                continue
            if limit and processed >= limit:
                save_json(manifest_path, manifest)
                return

            raw = source.read_text(encoding="utf-8-sig")
            source_repo_path = (Path("docs") / Path(relative)).as_posix()
            source_commit = git_value(repository, source_repo_path, "%H")
            last_modified = git_value(repository, source_repo_path, "%cs")
            versions = detect_civicrm_versions(version_rows, raw)
            legacy_urls = [official_legacy_url(guide, relative)]
            key = f"{guide.key}:{relative}"
            digest = sha256_json({
                "prompt_version": REWRITE_PROMPT_VERSION,
                "prompt": REWRITE_PROMPT,
                "provider": provider,
                "model": model,
                "preset": preset,
                "guide": guide.key,
                "source": raw,
                "source_commit": source_commit,
            })
            previous = entries.get(key, {}) if isinstance(entries, dict) else {}
            previous_outputs = normalise_list(previous.get("outputs"))
            outputs_exist = bool(previous_outputs) and all(
                (output_root / Path(item)).exists() for item in previous_outputs
            )
            previous_status = str(
                previous.get(
                    "status",
                    "accepted",
                )
            )

            previous_was_accepted = (
                previous_status == "accepted"
            )

            unchanged_accepted_rewrite = (
                previous_was_accepted
                and previous.get("sha256") == digest
                and outputs_exist
            )

            skip_existing_accepted_rewrite = (
                previous_was_accepted
                and skip_existing
                and outputs_exist
            )

            if (
                unchanged_accepted_rewrite
                or skip_existing_accepted_rewrite
            ):
                print(
                    f"Skipping accepted rewrite {key}"
                )
                continue

            base_prompt = (
                REWRITE_PROMPT.replace("SOURCE_PATH", relative)
                + f"\n\nGUIDE: {guide.key}\nSOURCE PATH: {relative}"
                + f"\nOFFICIAL URL: {legacy_urls[0]}"
                + f"\nSOURCE COMMIT: {source_commit or 'unknown'}"
                + f"\nLAST MODIFIED: {last_modified or 'unknown'}"
                + "\n\nSOURCE MARKDOWN:\n"
                + raw
            )
            print(f"Rewriting {key} with {provider}")

            accepted_chunks: Optional[List[str]] = None
            last_fidelity_error = ""
            for fidelity_attempt in range(1, fidelity_attempts + 1):
                attempt_prompt = base_prompt
                if last_fidelity_error:
                    attempt_prompt += "\n\n" + FIDELITY_CORRECTION_PROMPT.format(
                        error=last_fidelity_error
                    )
                answer = ai_request(attempt_prompt, provider, model, preset, retries)
                candidate_chunks = split_rewrite_pages(answer, key)
                try:
                    validate_source_fidelity(raw, candidate_chunks, key)
                    accepted_chunks = candidate_chunks
                    break
                except RuntimeError as exc:
                    last_fidelity_error = str(exc)
                    print(
                        f"  Fidelity attempt {fidelity_attempt}/{fidelity_attempts} "
                        f"failed: {last_fidelity_error}"
                    )

            if accepted_chunks is None:
                print(
                    f"  Rewrite rejected after {fidelity_attempts} fidelity attempts; "
                    "keeping the official source page and continuing."
                )
                for stale in previous_outputs:
                    stale_path = output_root / Path(stale)
                    if stale_path.exists():
                        stale_path.unlink()
                entries[key] = {
                    "sha256": digest,
                    "status": "fidelity-rejected",
                    "fidelity_error": last_fidelity_error,
                    "guide": guide.key,
                    "source_path": relative,
                    "source_repository": guide.repository,
                    "source_commit": source_commit,
                    "last_modified": last_modified,
                    "civicrm_versions": versions,
                    "legacy_urls": legacy_urls,
                    "outputs": [],
                }
                save_json(manifest_path, manifest)
                processed += 1
                continue

            relative_path = PurePosixPath(relative)
            new_outputs: List[str] = []
            for index, chunk in enumerate(accepted_chunks, 1):
                output_relative = relative if index == 1 else str(
                    relative_path.with_name(f"{relative_path.stem}-part{index}.md")
                )
                metadata, body = split_front_matter(chunk)
                if not body.strip():
                    raise RuntimeError(f"Rewritten page has no body: {key} output {index}")
                destination = destination_path(guide, output_relative)
                page_legacy_urls = legacy_urls if index == 1 else []
                metadata = normalise_metadata(
                    metadata,
                    body,
                    destination,
                    guide,
                    relative,
                    guide.repository,
                    source_commit,
                    last_modified,
                    versions,
                    page_legacy_urls,
                )
                source_comment = f"<!-- Source: {relative} -->"
                body = re.sub(r"(?im)^\s*<!--\s*Source:.*?-->\s*$", "", body).strip()
                body = f"{body}\n\n{source_comment}"
                target = output_root / Path(output_relative)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    build_markdown_with_front_matter(metadata, body),
                    encoding="utf-8",
                )
                new_outputs.append(output_relative)
                print(f"  wrote {guide.key}:{output_relative}")

            for stale in set(previous_outputs) - set(new_outputs):
                stale_path = output_root / Path(stale)
                if stale_path.exists():
                    stale_path.unlink()
            entries[key] = {
                "sha256": digest,
                "status": "accepted",
                "guide": guide.key,
                "source_path": relative,
                "source_repository": guide.repository,
                "source_commit": source_commit,
                "last_modified": last_modified,
                "civicrm_versions": versions,
                "legacy_urls": legacy_urls,
                "outputs": new_outputs,
            }
            save_json(manifest_path, manifest)
            processed += 1


def load_yaml(path: Path) -> Dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return {}
    return value if isinstance(value, dict) else {}


def copy_guide_content(paths: Paths, guide: GuideConfig) -> None:
    source_root = paths.upstream_for(guide) / "docs"
    if not source_root.exists():
        raise RuntimeError(f"The source docs directory does not exist: {source_root}")
    target_root = paths.site / "docs"
    if guide.destination_prefix:
        target_root /= guide.destination_prefix
    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_root, target_root, dirs_exist_ok=True)

def first_heading(body: str) -> str:
    """Return the first Markdown heading found in the body."""

    for line in body.splitlines():
        stripped = line.strip()

        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()

            if title:
                return title

    return ""

def resolve_page_title(
    metadata: Dict[str, Any],
    body: str,
    relative_path: str,
) -> str:
    """Return a non-empty page title."""

    candidates = [
        str(metadata.get("title", "")).strip(),
        str(metadata.get("link_title", "")).strip(),
        first_heading(body).strip(),
        Path(relative_path).stem.replace("-", " ").strip().title(),
    ]

    for candidate in candidates:
        if candidate:
            return candidate

    return relative_path

def copy_non_doc_assets(paths: Paths, primary: GuideConfig) -> None:
    source = paths.upstream_for(primary)
    for item in source.iterdir():
        if item.name in {".git", "docs", "site", "mkdocs.yml"}:
            continue
        target = paths.site / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def prepare_site(paths: Paths, guides: List[GuideConfig], include_rewrites: bool = True,) -> None:
    safe_rmtree(paths.site)
    (paths.site / "docs").mkdir(parents=True, exist_ok=True)
    primary = next((guide for guide in guides if guide.key == "user-en"), guides[0])
    copy_non_doc_assets(paths, primary)
    for guide in guides:
        copy_guide_content(paths, guide)

        if not include_rewrites:
            continue

        rewritten_root = paths.rewritten_for(guide)

        if rewritten_root.exists():
            destination_root = paths.site / "docs"

            if guide.destination_prefix:
                destination_root /= guide.destination_prefix

            shutil.copytree(
                rewritten_root,
                destination_root,
                dirs_exist_ok=True,
            )

def restore_official_fallback_pages(
    paths: Paths,
) -> None:
    """
    Restore official source pages for every rejected or unavailable
    AI rewrite recorded in the rewrite manifest.
    """

    manifest = load_json(
        paths.state / "rewrite-manifest.json"
    )

    entries = manifest.get("files", {})

    if not isinstance(entries, dict):
        return

    restored = 0

    for entry in entries.values():
        if not isinstance(entry, dict):
            continue

        status = str(
            entry.get("status", "")
        )

        if status == "accepted":
            continue

        guide_key = str(
            entry.get("guide", "")
        )

        source_relative = str(
            entry.get("source_path", "")
        ).replace("\\", "/").lstrip("/")

        guide = GUIDES.get(guide_key)

        if not guide or not source_relative:
            continue

        source = (
            paths.upstream_for(guide)
            / "docs"
            / Path(source_relative)
        )

        destination_relative = destination_path(
            guide,
            source_relative,
        )

        destination = (
            paths.site
            / "docs"
            / Path(destination_relative)
        )

        if not source.exists():
            print(
                "Warning: official fallback source "
                f"does not exist: {source}"
            )
            continue

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(
            source,
            destination,
        )

        restored += 1

    if restored:
        print(
            "Restored "
            f"{restored} official source fallback "
            "page(s)."
        )

def clean_body(body: str, source_path: str) -> str:
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    body = re.sub(r"\[¶]\([^)]+\)", "", body)
    body = re.sub(r"(?m)[ \t]+$", "", body)
    body = re.sub(r"(?im)^\s*<!--\s*Source:.*?-->\s*$", "", body).strip()
    body = re.sub(r"\n{3,}", "\n\n", body)
    return f"{body}\n\n<!-- Source: {source_path} -->"


def metadata_for_source(
    paths: Paths,
    guide: GuideConfig,
    source_relative: str,
    destination: str,
    metadata: Dict[str, Any],
    body: str,
) -> Dict[str, Any]:
    repository = paths.upstream_for(guide)
    source_repo_path = (Path("docs") / Path(source_relative)).as_posix()
    return normalise_metadata(
        metadata,
        body,
        destination,
        guide,
        source_relative,
        guide.repository,
        git_value(repository, source_repo_path, "%H"),
        git_value(repository, source_repo_path, "%cs"),
        normalise_list(metadata.get("civicrm_version")) or ["latest"],
        [official_legacy_url(guide, source_relative)],
    )


def clean_all_markdown(paths: Paths, guides: List[GuideConfig]) -> None:
    docs_root = paths.site / "docs"
    guide_by_prefix = sorted(guides, key=lambda item: len(item.destination_prefix), reverse=True)
    default_guide = next((item for item in guides if not item.destination_prefix), guides[0])
    for page in iter_markdown(docs_root):
        destination = page.relative_to(docs_root).as_posix()
        if destination.startswith(BROWSE_DIR + "/"):
            continue
        guide = next(
            (
                item for item in guide_by_prefix
                if item.destination_prefix and destination.startswith(item.destination_prefix + "/")
            ),
            default_guide,
        )
        source_relative = destination
        if guide.destination_prefix and destination.startswith(guide.destination_prefix + "/"):
            source_relative = destination[len(guide.destination_prefix) + 1:]
        metadata, body = split_front_matter(page.read_text(encoding="utf-8-sig"))
        body = clean_body(body, source_relative)
        metadata = metadata_for_source(paths, guide, source_relative, destination, metadata, body)
        page.write_text(build_markdown_with_front_matter(metadata, body), encoding="utf-8")


MARKDOWN_TARGET_RE = re.compile(
    r'(?P<prefix>!?\[[^\]]*]\()(?P<target>[^)\s]+)(?P<suffix>(?:\s+["\'][^"\']*["\'])?\))'
)


def repair_markdown_targets(docs_root: Path) -> None:
    repaired = 0
    for document in iter_markdown(docs_root):
        relative = document.relative_to(docs_root).as_posix()
        directory = posixpath.dirname(relative) or "."
        original = document.read_text(encoding="utf-8-sig")

        def replace(match: re.Match[str]) -> str:
            nonlocal repaired
            raw = match.group("target")
            target = raw.strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#")):
                return match.group(0)
            path, separator, fragment = target.partition("#")
            path = path.replace("\\", "/")
            resolved = posixpath.normpath(posixpath.join(directory, path))
            replacement = path
            if not resolved.startswith("../") and not PurePosixPath(resolved).suffix:
                for candidate in (resolved + ".md", posixpath.join(resolved, "index.md")):
                    if (docs_root / Path(candidate)).exists():
                        replacement = posixpath.relpath(candidate, directory)
                        break
            if separator:
                replacement += "#" + fragment
            if raw.startswith("<") and raw.endswith(">"):
                replacement = f"<{replacement}>"
            if replacement != raw:
                repaired += 1
            return match.group("prefix") + replacement + match.group("suffix")

        corrected = MARKDOWN_TARGET_RE.sub(replace, original)
        if corrected != original:
            document.write_text(corrected, encoding="utf-8")
    print(f"Repaired {repaired} Markdown target(s).")


def nav_entries(nav: Any, breadcrumbs: Optional[List[str]] = None) -> List[Tuple[str, List[str]]]:
    breadcrumbs = breadcrumbs or []
    result: List[Tuple[str, List[str]]] = []
    if isinstance(nav, list):
        for item in nav:
            result.extend(nav_entries(item, breadcrumbs))
    elif isinstance(nav, dict):
        for title, value in nav.items():
            if isinstance(value, str) and value.endswith(".md"):
                result.append((value.replace("\\", "/"), breadcrumbs + [str(title)]))
            elif isinstance(value, list):
                result.extend(nav_entries(value, breadcrumbs + [str(title)]))
    elif isinstance(nav, str) and nav.endswith(".md"):
        result.append((nav.replace("\\", "/"), breadcrumbs))
    return result


def collect_nav_paths(nav: Any) -> List[str]:
    return [path for path, _ in nav_entries(nav)]


def page_inventory(docs_root: Path, official_navs: Dict[str, Any]) -> List[Dict[str, Any]]:
    positions: Dict[str, Tuple[int, List[str]]] = {}
    order = 0
    for guide_key, nav in official_navs.items():
        guide = GUIDES[guide_key]
        for path, breadcrumbs in nav_entries(nav):
            positions.setdefault(destination_path(guide, path), (order, breadcrumbs))
            order += 1
    inventory: List[Dict[str, Any]] = []
    next_order = order
    for page in iter_markdown(docs_root):
        relative = page.relative_to(docs_root)
        path = relative.as_posix()
        if relative.parts and relative.parts[0] == BROWSE_DIR:
            continue
        metadata, body = split_front_matter(page.read_text(encoding="utf-8-sig"))
        if metadata.get("generated_index"):
            continue
        title = resolve_page_title(
            metadata,
            body,
            path,
        ) or markdown_title(body, page.stem)
        current_order, breadcrumbs = positions.get(path, (next_order, []))
        if path not in positions:
            next_order += 1
        inventory.append({
            "id": "",
            "destination_path": path,
            "title": title,
            "summary": str(metadata.get("summary", "")).strip(),
            "topic": str(metadata.get("topic", "general")).strip(),
            "subtopic": str(metadata.get("subtopic", "general")).strip(),
            "component": str(metadata.get("component", "CiviCRM Core")).strip(),
            "category": str(metadata.get("category", "reference")).strip(),
            "audiences": normalise_list(metadata.get("audiences")),
            "level": str(metadata.get("level", "basic")).strip(),
            "journey_stage": str(metadata.get("journey_stage", "everyday-tasks")).strip(),
            "guide": str(metadata.get("guide", "user-en")).strip(),
            "current_order": current_order,
            "current_breadcrumbs": breadcrumbs,
        })
    inventory.sort(key=lambda item: (item["current_order"], item["destination_path"]))
    for index, item in enumerate(inventory, 1):
        item["id"] = f"p{index:05d}"
    return inventory


NAVIGATION_PROMPT = r"""
You are the information architect for a unified CiviCRM documentation site.
You receive a complete page inventory. Each page has an immutable opaque id and
an informational destination_path.

OUTPUT
Return JSON only as {"nav": [...]}. Use only:
- section: {"title": "...", "children": [...]}
- page: {"page_id": "p00001"}

NON-NEGOTIABLE INTEGRITY
- Use every page_id exactly once.
- Copy page_id exactly; never emit paths and never invent, omit or duplicate ids.
- Navigation placement does not change files or URLs.

SHALLOW INFORMATION ARCHITECTURE
- Use at most six root choices; Browse is added later.
- Use no more than eighteen direct choices in a section.
- Prefer root -> functional topic -> page.
- Add one semantic subgroup only when a topic has enough pages to justify it.
- Never create a section for one page. Every section must have at least two children.
- Never require opening more than three section levels before reaching a page.
- Do not create wrapper levels named User guide, More, Start and use, Review and
  extend, Plan and configure 2, or similar mechanical buckets.
- Do not use alphabetical buckets.

EDITORIAL STRUCTURE
- Organise first by reader intent and functional feature: contacts and data,
  communication, fundraising and engagement, search and reporting, and
  administration/extension.
- Within a large topic, derive precise task-oriented labels from the actual
  pages, for example Set up events, Registration and participants, Payments,
  Reports, or Troubleshooting.
- Use journey_stage only as evidence for ordering; do not force all journey
  stages into the navigation.
- Use category (tutorial, how-to, reference, explanation) as a secondary signal,
  not as a primary navigation branch.
- Audiences are metadata and must never create primary navigation branches.
- Put a component entry page such as "What is CiviEvent?" first in its topic,
  directly if possible; do not wrap it in a one-page Overview section.
- Preserve a practical order: orientation, setup, common tasks, management,
  reporting, reference/troubleshooting, extensions.

QUALITY CHECK BEFORE OUTPUT
- Flatten every section with a single child.
- Check that each page is reachable without opening empty or redundant levels.
- Check all page ids exactly once, then return JSON only.
""".strip()
def plan_id_entries(plan: Any) -> List[str]:
    found: List[str] = []
    if isinstance(plan, list):
        for item in plan:
            found.extend(plan_id_entries(item))
    elif isinstance(plan, dict):
        if set(plan) == {"page_id"} and isinstance(plan.get("page_id"), str):
            found.append(plan["page_id"])
        elif set(plan) == {"title", "children"}:
            found.extend(plan_id_entries(plan.get("children")))
    return found


def normalise_navigation_titles(node: Any, fallback_title: str = "Other pages") -> Any:
    """Normalise section titles without adding keys to page_id nodes."""
    if isinstance(node, list):
        return [normalise_navigation_titles(item, fallback_title) for item in node if item is not None]
    if not isinstance(node, dict):
        return node
    if set(node) == {"page_id"}:
        return {"page_id": str(node.get("page_id", "")).strip()}
    children = node.get("children", [])
    title = str(node.get("title", "")).strip() or fallback_title
    return {
        "title": title,
        "children": normalise_navigation_titles(children, fallback_title),
    }

def validate_navigation_plan(plan: Any, expected_ids: List[str], depth: int = 0) -> None:
    if depth > MAX_NAV_DEPTH:
        raise RuntimeError(
            f"Invalid navigation plan: more than {MAX_NAV_DEPTH} section levels before a page."
        )
    if not isinstance(plan, list):
        raise RuntimeError("Invalid navigation plan: nav must be an array.")
    for node in plan:
        if not isinstance(node, dict):
            raise RuntimeError("Invalid navigation plan: every node must be an object.")
        keys = set(node)
        if keys == {"page_id"}:
            if not isinstance(node["page_id"], str):
                raise RuntimeError("Invalid navigation plan: page_id must be a string.")
        elif keys == {"title", "children"}:
            title = str(node["title"]).strip()
            children = node["children"]
            if not title:
                raise RuntimeError("Invalid navigation plan: section title is empty.")
            if not isinstance(children, list) or len(children) < 2:
                raise RuntimeError(
                    f"Invalid navigation plan: section {title!r} must contain at least two choices."
                )
            if len(children) > MAX_NAV_CHOICES:
                raise RuntimeError(
                    f"Invalid navigation plan: section {title!r} has {len(children)} direct choices; "
                    f"the maximum is {MAX_NAV_CHOICES}."
                )
            validate_navigation_plan(children, expected_ids, depth + 1)
        else:
            raise RuntimeError(
                "Invalid navigation plan: nodes may contain only page_id, or title and children."
            )
    if depth == 0:
        actual = plan_id_entries(plan)
        duplicates = sorted(page_id for page_id, count in Counter(actual).items() if count > 1)
        missing = sorted(set(expected_ids) - set(actual))
        invented = sorted(set(actual) - set(expected_ids))
        messages: List[str] = []
        if duplicates:
            messages.append("duplicate page IDs: " + ", ".join(duplicates))
        if missing:
            messages.append("missing page IDs: " + ", ".join(missing))
        if invented:
            messages.append("invented page IDs: " + ", ".join(invented))
        if messages:
            raise RuntimeError("Invalid navigation plan: " + "; ".join(messages))
        if len(plan) > MAX_MAIN_ROOT_CHOICES:
            raise RuntimeError(
                f"Invalid navigation plan: root has {len(plan)} choices; "
                f"the maximum is {MAX_MAIN_ROOT_CHOICES} before Browse is added."
            )

def resolve_navigation_plan(plan: List[Any], inventory: List[Dict[str, Any]]) -> List[Any]:
    by_id = {item["id"]: item for item in inventory}
    result: List[Any] = []
    for node in plan:
        if "page_id" in node:
            page = by_id[node["page_id"]]
            label = "Home" if page["destination_path"] == "index.md" else page["title"]
            result.append({label: page["destination_path"]})
        else:
            result.append({str(node["title"]): resolve_navigation_plan(node["children"], inventory)})
    return result


def topic_label(topic: str) -> str:
    return TOPIC_LABELS.get(topic, topic.replace("-", " ").title())


def topic_sort_key(topic: str) -> Tuple[int, str]:
    preferred = list(TOPIC_LABELS)
    return (preferred.index(topic) if topic in preferred else 999, topic)


def split_page_nodes(pages: List[Dict[str, Any]], title: str) -> List[Any]:
    nodes = [{"page_id": page["id"]} for page in sorted(pages, key=lambda item: item["current_order"])]
    if len(nodes) <= MAX_NAV_CHOICES:
        return [{"title": title, "children": nodes}]
    grouped: Dict[str, List[Any]] = defaultdict(list)
    for page in sorted(pages, key=lambda item: item["current_order"]):
        grouped[str(page.get("subtopic", "general"))].append({"page_id": page["id"]})
    subgroups: List[Any] = []
    for subtopic, children in grouped.items():
        label = subtopic.replace("-", " ").title()
        for index in range(0, len(children), MAX_NAV_CHOICES):
            suffix = "" if index == 0 else f" {index // MAX_NAV_CHOICES + 1}"
            subgroups.append({"title": label + suffix, "children": children[index:index + MAX_NAV_CHOICES]})
    if len(subgroups) <= MAX_NAV_CHOICES:
        return [{"title": title, "children": subgroups}]
    sections: List[Any] = []
    for index in range(0, len(subgroups), MAX_NAV_CHOICES):
        suffix = "" if index == 0 else f" {index // MAX_NAV_CHOICES + 1}"
        sections.append({"title": title + suffix, "children": subgroups[index:index + MAX_NAV_CHOICES]})
    return sections


def navigation_choice_title(node: Any) -> str:
    """Return a readable title for a navigation node."""

    if isinstance(node, dict):
        if "title" in node:
            title = str(node.get("title", "")).strip()

            if title:
                return title

            raise RuntimeError(
                "Invalid navigation plan: section title is empty."
            )

        if "page_id" in node:
            return str(node["page_id"]).strip() or "Page"

    return "Pages"


def bounded_navigation_children(
    nodes: List[Any],
    label: str,
) -> List[Any]:
    """
    Recursively group navigation nodes so that no section contains more
    than MAX_NAV_CHOICES direct choices.
    """

    if len(nodes) <= MAX_NAV_CHOICES:
        return nodes

    group_size = max(
        2,
        (
            len(nodes)
            + MAX_NAV_CHOICES
            - 1
        )
        // MAX_NAV_CHOICES,
    )

    groups: List[Any] = []

    for offset in range(
        0,
        len(nodes),
        group_size,
    ):
        chunk = nodes[
            offset:offset + group_size
        ]

        first_title = navigation_choice_title(
            chunk[0]
        )

        last_title = navigation_choice_title(
            chunk[-1]
        )

        if first_title == last_title:
            group_title = (
                f"{label}: {first_title}"
            )
        else:
            group_title = f"More {label.lower()}"
        groups.append(
            {
                "title": group_title,
                "children": (
                    bounded_navigation_children(
                        chunk,
                        label,
                    )
                ),
            }
        )

    if len(groups) > MAX_NAV_CHOICES:
        return bounded_navigation_children(
            groups,
            label,
        )

    return groups

def deterministic_navigation_plan(inventory: List[Dict[str, Any]]) -> List[Any]:
    """Build a shallow fallback: domain -> topic -> optional stage -> page."""
    by_domain: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for page in inventory:
        if page["destination_path"] == "index.md":
            continue
        topic = str(page.get("topic", "general"))
        domain = TOPIC_DOMAIN.get(topic, "Configure, automate and extend")
        by_domain[domain][topic].append(page)

    roots: List[Any] = []
    home = next((page for page in inventory if page["destination_path"] == "index.md"), None)
    if home:
        roots.append({"page_id": home["id"]})

    for domain in DOMAIN_ORDER:
        topics = by_domain.get(domain, {})
        if not topics:
            continue
        topic_nodes: List[Any] = []
        for topic in sorted(topics, key=topic_sort_key):
            pages = sorted(
                topics[topic],
                key=lambda item: (
                    STAGE_ORDER.get(str(item.get("journey_stage", "")), 99),
                    item["current_order"],
                ),
            )
            if len(pages) <= MAX_NAV_CHOICES:
                children: List[Any] = [{"page_id": page["id"]} for page in pages]
            else:
                children = []
                by_stage: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
                for page in pages:
                    by_stage[str(page.get("journey_stage", "everyday-tasks"))].append(page)
                for stage, label in STAGE_LABELS.items():
                    stage_pages = by_stage.get(stage, [])
                    if not stage_pages:
                        continue
                    if len(stage_pages) == 1:
                        children.append({"page_id": stage_pages[0]["id"]})
                        continue
                    for offset in range(0, len(stage_pages), MAX_NAV_CHOICES):
                        chunk = stage_pages[offset:offset + MAX_NAV_CHOICES]
                        chunk_label = label if offset == 0 else f"{label} — continued"
                        children.append({
                            "title": chunk_label,
                            "children": [{"page_id": page["id"]} for page in chunk],
                        })
            topic_nodes.append({"title": topic_label(topic), "children": children})
        roots.append({"title": domain, "children": topic_nodes})

    roots = normalise_navigation_titles(roots)
    roots = collapse_single_child_sections(roots)
    return roots

def build_global_navigation(
    paths: Paths,
    inventory: List[Dict[str, Any]],
    provider: str,
    model: str,
    preset: str,
    retries: int,
    request_ai: bool,
    refresh: bool,
) -> List[Any]:
    expected_ids = [item["id"] for item in inventory]
    digest = sha256_json({
        "version": NAVIGATION_PROMPT_VERSION,
        "prompt": NAVIGATION_PROMPT,
        "provider": provider,
        "model": model,
        "preset": preset,
        "inventory": inventory,
    })
    cache_path = paths.state / "navigation-manifest.json"
    cache = load_json(cache_path)
    cached_plan = cache.get("plan") if cache.get("sha256") == digest else None
    if isinstance(cached_plan, list) and not refresh:
        try:
            cached_plan = normalise_navigation_titles(cached_plan)
            cached_plan = collapse_single_child_sections(cached_plan)
            validate_navigation_plan(cached_plan, expected_ids)
            print("Reusing the validated navigation plan from navigation-manifest.json.")
            return resolve_navigation_plan(cached_plan, inventory)
        except RuntimeError as exc:
            print(f"Ignoring an invalid cached navigation plan: {exc}")

    fallback_plan = deterministic_navigation_plan(inventory)
    fallback_plan = collapse_single_child_sections(fallback_plan)
    validate_navigation_plan(fallback_plan, expected_ids)
    plan = fallback_plan
    source = "deterministic"

    if request_ai:
        base_prompt = (
            NAVIGATION_PROMPT
            + "\n\nPAGE INVENTORY:\n"
            + json.dumps(inventory, ensure_ascii=False, indent=2)
        )
        correction = ""
        for attempt in range(1, 4):
            try:
                raw = ai_request(
                    base_prompt + correction,
                    provider,
                    model,
                    preset,
                    retries,
                    json_response=True,
                )
                payload = json.loads(raw)
                proposed = normalise_navigation_titles(payload.get("nav"))
                proposed = collapse_single_child_sections(proposed)
                validate_navigation_plan(proposed, expected_ids)
                plan = proposed
                source = "ai"
                break
            except (RuntimeError, json.JSONDecodeError) as exc:
                print(f"AI navigation attempt {attempt}/3 rejected: {exc}")
                correction = (
                    "\n\nCORRECTION REQUIRED\n"
                    f"The previous plan failed validation: {exc}\n"
                    "Return the complete corrected JSON plan. Keep every page id exactly once, "
                    "flatten singleton sections, and respect the depth and choice limits."
                )
        else:
            print("AI navigation was rejected after 3 attempts; using the shallow deterministic fallback.")
            source = "deterministic-fallback"

    plan = normalise_navigation_titles(plan)
    plan = collapse_single_child_sections(plan)
    validate_navigation_plan(plan, expected_ids)
    save_json(cache_path, {
        "sha256": digest,
        "plan": plan,
        "source": source,
        "id_to_path": {item["id"]: item["destination_path"] for item in inventory},
    })
    return resolve_navigation_plan(plan, inventory)

def relative_link(from_path: str, to_path: str) -> str:
    directory = posixpath.dirname(from_path) or "."
    return posixpath.relpath(to_path, directory)


def write_generated_index(
    docs_root: Path,
    relative_path: str,
    title: str,
    intro: str,
    groups: List[Tuple[str, List[Dict[str, Any]]]],
) -> None:
    lines = [
        "---", f"title: {json.dumps(title)}", "generated_index: true", "hide:", "- toc", "---",
        "", f"# {title}", "", intro, "",
    ]
    for heading, pages in groups:
        if not pages:
            continue
        lines.extend([f"## {heading}", ""])
        for page in pages:
            target = relative_link(relative_path, page["destination_path"])
            lines.append(f"- [{page['title']}]({target})")
            summary = page.get("summary", "").strip()
            if summary:
                lines.append(f"  {summary}")
        lines.append("")
    target_path = docs_root / Path(relative_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def generate_browse_indexes(
    docs_root: Path,
    inventory: List[Dict[str, Any]],
) -> Tuple[List[Any], List[Any]]:
    browse_root = docs_root / BROWSE_DIR
    safe_rmtree(browse_root)
    browse_root.mkdir(parents=True, exist_ok=True)

    category_nav: List[Any] = []
    for category, label in CATEGORY_LABELS.items():
        pages = [page for page in inventory if page.get("category") == category]
        groups: List[Tuple[str, List[Dict[str, Any]]]] = []
        if category == "tutorial":
            for level in ("basic", "intermediate", "advanced"):
                group = [page for page in pages if page.get("level") == level]
                if group:
                    groups.append((level.title(), sorted(group, key=lambda item: item["current_order"])))
        else:
            for topic in sorted({page["topic"] for page in pages}, key=topic_sort_key):
                group = [page for page in pages if page["topic"] == topic]
                groups.append((topic_label(topic), sorted(
                    group,
                    key=lambda item: (
                        STAGE_ORDER.get(str(item.get("journey_stage", "")), 99),
                        item["current_order"],
                    ),
                )))
        relative = f"{BROWSE_DIR}/categories/{category}.md"
        write_generated_index(
            docs_root,
            relative,
            label,
            "Browse pages organised for this type of documentation need.",
            groups,
        )
        category_nav.append({label: relative})

    audience_nav: List[Any] = []
    for audience, label in AUDIENCE_LABELS.items():
        pages = [page for page in inventory if audience in page.get("audiences", [])]
        if not pages:
            continue
        groups: List[Tuple[str, List[Dict[str, Any]]]] = []
        for topic in sorted({page["topic"] for page in pages}, key=topic_sort_key):
            group = [page for page in pages if page["topic"] == topic]
            groups.append((topic_label(topic), sorted(group, key=lambda item: item["current_order"])))
        relative = f"{BROWSE_DIR}/audiences/{audience}.md"
        write_generated_index(
            docs_root,
            relative,
            label,
            "Pages relevant to this audience, grouped by functional topic.",
            groups,
        )
        audience_nav.append({label: relative})
    return category_nav, audience_nav

def navigation_markdown_lines(
    nav: Any,
    depth: int = 0,
) -> List[str]:
    """Render a resolved MkDocs navigation tree as readable Markdown."""

    lines: List[str] = []
    indent = "  " * depth

    if isinstance(nav, list):
        for item in nav:
            lines.extend(
                navigation_markdown_lines(
                    item,
                    depth,
                )
            )

    elif isinstance(nav, dict):
        for title, value in nav.items():
            if isinstance(value, str):
                lines.append(
                    f"{indent}- **{title}** — `{value}`"
                )

            elif isinstance(value, list):
                lines.append(
                    f"{indent}- **{title}**"
                )

                lines.extend(
                    navigation_markdown_lines(
                        value,
                        depth + 1,
                    )
                )

    return lines


def export_navigation_plan(
    paths: Paths,
    config: Dict[str, Any],
) -> None:
    """Export the resolved navigation to human-readable YAML and Markdown."""

    paths.reports.mkdir(
        parents=True,
        exist_ok=True,
    )

    navigation = config.get("nav", [])

    navigation_manifest = load_json(
        paths.state / "navigation-manifest.json"
    )

    navigation_source = str(
        navigation_manifest.get(
            "source",
            "unknown",
        )
    )

    yaml_payload = {
        "navigation_source": navigation_source,
        "nav": navigation,
    }

    yaml_path = (
        paths.reports
        / "navigation-plan.yaml"
    )

    yaml_path.write_text(
        yaml.safe_dump(
            yaml_payload,
            sort_keys=False,
            allow_unicode=True,
            width=140,
        ),
        encoding="utf-8",
    )

    markdown_lines = [
        "# Proposed CiviCRM documentation navigation",
        "",
        f"Navigation source: **{navigation_source}**",
        "",
        "This document shows the resolved navigation paths.",
        "Generating this preview does not rewrite documentation pages.",
        "",
        "## Navigation tree",
        "",
    ]

    markdown_lines.extend(
        navigation_markdown_lines(navigation)
    )

    markdown_path = (
        paths.reports
        / "navigation-plan.md"
    )

    markdown_path.write_text(
        "\n".join(markdown_lines).rstrip()
        + "\n",
        encoding="utf-8",
    )

    print(
        "Navigation previews written to:"
    )
    print(f"  {markdown_path}")
    print(f"  {yaml_path}")

def configure_mkdocs(
    paths: Paths,
    guides: List[GuideConfig],
    provider: str,
    model: str,
    preset: str,
    retries: int,
    ai_navigation: bool,
    refresh_navigation: bool,
    translator_url: Optional[str] = None,
    translator_languages: Optional[List[str]] = None,
    translator_source_language: str = "en",
) -> Dict[str, Any]:
    primary = next((guide for guide in guides if guide.key == "user-en"), guides[0])
    config = load_yaml(paths.upstream_for(primary) / "mkdocs.yml")
    if not config:
        config = {
            "site_name": "CiviCRM Documentation",
            "theme": {"name": "material"},
            "plugins": ["search"],
            "markdown_extensions": ["admonition", "toc"],
        }
    config.update({
        "site_name": "CiviCRM Documentation",
        "docs_dir": "docs",
        "site_dir": "site",
        "use_directory_urls": True,
    })
    official_navs: Dict[str, Any] = {}
    for guide in guides:
        source_config = load_yaml(paths.upstream_for(guide) / "mkdocs.yml")
        official_navs[guide.key] = source_config.get("nav", [])
    docs_root = paths.site / "docs"
    inventory = page_inventory(docs_root, official_navs)
    main_nav = build_global_navigation(
        paths, inventory, provider, model, preset, retries, ai_navigation, refresh_navigation
    )
    category_nav, audience_nav = generate_browse_indexes(docs_root, inventory)
    main_nav.append({
        "Browse": [
            {"By content category": category_nav},
            {"By audience": audience_nav},
        ]
    })
    config["nav"] = main_nav
    plugins = config.get("plugins", ["search"])
    if not isinstance(plugins, list):
        plugins = ["search"]
    filtered: List[Any] = []
    has_search = False
    for plugin in plugins:
        name = plugin if isinstance(plugin, str) else next(iter(plugin), "") if isinstance(plugin, dict) else ""
        if name == "categories":
            continue
        has_search = has_search or name == "search"
        filtered.append(plugin)
    if not has_search:
        filtered.insert(0, "search")
    config["plugins"] = filtered
    if translator_url:
        source_language = (
            translator_source_language.strip()
            or "en"
        )

        target_languages = [
            language.strip()
            for language in (
                translator_languages or []
            )
            if language.strip()
            and language.strip() != source_language
        ]

        if target_languages:
            install_translator(
                site=paths.site,
                config=config,
                endpoint=translator_url,
                target_languages=target_languages,
                source_language=source_language,
            )

            print(
                "Installed LibreTranslate switcher: "
                f"{source_language} -> "
                f"{', '.join(target_languages)}"
            )    
    (paths.site / "mkdocs.yml").write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True, width=140),
        encoding="utf-8",
    )
    return config


def validate_nav_files(config: Dict[str, Any], docs_root: Path) -> None:
    paths = collect_nav_paths(config.get("nav", []))
    missing = sorted({path for path in paths if not (docs_root / Path(path)).exists()})
    duplicates = sorted(path for path, count in Counter(paths).items() if count > 1)
    messages = []
    if missing:
        messages.append("missing files: " + ", ".join(missing))
    if duplicates:
        messages.append("duplicate navigation paths: " + ", ".join(duplicates))
    if messages:
        raise RuntimeError("Navigation validation failed: " + "; ".join(messages))


def audit_documentation(paths: Paths, config: Dict[str, Any]) -> None:
    docs_root = paths.site / "docs"
    nav_paths = set(collect_nav_paths(config.get("nav", [])))
    rows: List[Dict[str, Any]] = []
    topic_counts: Counter[str] = Counter()
    topic_overviews: Counter[str] = Counter()
    rejected = load_json(paths.state / "rewrite-manifest.json").get("files", {})
    rejected_count = sum(
        1 for entry in rejected.values()
        if isinstance(entry, dict) and entry.get("status") == "fidelity-rejected"
    ) if isinstance(rejected, dict) else 0

    for page in iter_markdown(docs_root):
        relative = page.relative_to(docs_root).as_posix()
        metadata, _ = split_front_matter(page.read_text(encoding="utf-8-sig"))
        if metadata.get("generated_index"):
            continue
        required = (
            "title", "category", "topic", "subtopic", "component", "audiences",
            "level", "journey_stage", "summary", "extensions", "related",
            "review_priority", "review_notes", "source_repository", "source_path",
            "destination_path", "legacy_urls",
        )
        issues = [f"missing {key}" for key in required if key not in metadata]
        notes = normalise_list(metadata.get("review_notes"))
        expected_priority = review_priority_from_notes(notes)
        if metadata.get("review_priority") != expected_priority:
            issues.append(f"review_priority should be {expected_priority!r}")
        if metadata.get("category") not in ALLOWED_CATEGORIES:
            issues.append("invalid category")
        if metadata.get("journey_stage") not in ALLOWED_JOURNEY_STAGES:
            issues.append("invalid journey_stage")
        if relative not in nav_paths:
            issues.append("not present in primary navigation")
        topic = str(metadata.get("topic", "general"))
        if topic not in ALLOWED_TOPICS:
            issues.append(
                f"invalid non-canonical topic: {topic}"
            )
        topic_counts[topic] += 1
        if metadata.get("journey_stage") == "overview" or str(metadata.get("title", "")).casefold().startswith("what is "):
            topic_overviews[topic] += 1
        rows.append({
            "path": relative,
            "title": metadata.get("title", ""),
            "topic": topic,
            "category": metadata.get("category", ""),
            "audiences": ", ".join(normalise_list(metadata.get("audiences"))),
            "review_priority": metadata.get("review_priority", ""),
            "issues": "; ".join(issues),
        })

    paths.reports.mkdir(parents=True, exist_ok=True)
    csv_path = paths.reports / "documentation-audit.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["path", "issues"])
        writer.writeheader()
        writer.writerows(rows)
    report = [
        "# Documentation audit", "", f"Pages audited: {len(rows)}", "",
        f"AI rewrites rejected for fidelity: {rejected_count}", "", "## Topic compliance", "",
    ]
    for topic, count in sorted(topic_counts.items(), key=lambda item: topic_sort_key(item[0])):
        status = "OK" if topic_overviews[topic] else "Review: no overview page"
        report.append(f"- **{topic_label(topic)}**: {count} pages — {status}")
    report.extend(["", "## Pages needing review", ""])
    flagged = [row for row in rows if row["issues"] or row["review_priority"] != "low"]
    if flagged:
        for row in flagged:
            detail = row["issues"] or f"review priority: {row['review_priority']}"
            report.append(f"- `{row['path']}` — {detail}")
    else:
        report.append("No review issue was detected.")
    (paths.reports / "documentation-audit.md").write_text(
        "\n".join(report).rstrip() + "\n", encoding="utf-8"
    )
    print(f"Audited {len(rows)} documentation page(s).")


def build_site(site: Path, strict: bool = True) -> None:
    command = [sys.executable, "-m", "mkdocs", "build", "--clean"]
    if strict:
        command.append("--strict")
    result = subprocess.run(command, cwd=str(site), check=False)
    if result.returncode:
        raise RuntimeError(
            "MkDocs build failed. Review the messages above or use --no-strict temporarily."
        )


def serve_site(site: Path, address: str) -> None:
    print(f"Serving documentation at http://{address}")
    run_command([sys.executable, "-m", "mkdocs", "serve", "--dev-addr", address], cwd=site)


def parse_csv_paths(value: str) -> List[str]:
    return [item.strip().strip("/\\") for item in value.split(",") if item.strip()]


def selected_guides(value: str) -> List[GuideConfig]:
    names = parse_csv_paths(value)
    unknown = [name for name in names if name not in GUIDES]
    if unknown:
        raise RuntimeError("Unknown guide(s): " + ", ".join(unknown))
    if not names:
        raise RuntimeError("Select at least one guide.")
    return [GUIDES[name] for name in names]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a unified, source-faithful CiviCRM documentation site."
    )
    parser.add_argument(
        "command", nargs="?", choices=["run", "sync", "prepare", "plan", "build", "serve"], default="run"
    )
    parser.add_argument("--guides", default=DEFAULT_GUIDES, help="Comma-separated guide keys.")
    parser.add_argument("--list-guides", action="store_true", help="List configured guides and exit.")
    parser.add_argument("--workspace", default=DEFAULT_WORKSPACE)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--ref", help="Git branch or tag to use for every selected guide.")
    parser.add_argument("--fresh", action="store_true", help="Remove workspace and output before running.")
    parser.add_argument("--ai", action="store_true", help="Rewrite selected pages with AI.")
    parser.add_argument("--ai-nav", action="store_true", help="Ask AI to propose the global navigation plan.")
    parser.add_argument("--refresh-nav", action="store_true", help="Ignore the cached navigation plan.")
    parser.add_argument(
        "--provider", choices=["perplexity", "openai"],
        default=os.getenv("CIVIDOC_PROVIDER", "perplexity"),
    )
    parser.add_argument("--model", default=os.getenv("CIVIDOC_MODEL", ""))
    parser.add_argument(
        "--preset", choices=["fast", "low", "medium", "high", "xhigh"],
        default=os.getenv("CIVIDOC_PRESET", "high"),
    )
    parser.add_argument("--include", default=os.getenv("INCLUDE_SECTIONS", ""))
    parser.add_argument("--exclude", default=os.getenv("EXCLUDE_SECTIONS", ""))
    parser.add_argument("--limit", type=int, default=0, help="Limit AI page rewrites for testing.")
    parser.add_argument("--retries", type=int, default=5, help="Retries for each network AI request.")
    parser.add_argument(
        "--fidelity-attempts", type=int, default=DEFAULT_FIDELITY_ATTEMPTS,
        help="Complete rewrite attempts after source-fidelity failures.",
    )
    parser.add_argument("--skip-existing-rewrites", action="store_true")
    parser.add_argument("--versions-csv", default="civicrm_versions.csv")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--no-strict", action="store_true")
    parser.add_argument("--serve-after", action="store_true")
    parser.add_argument("--address", default="127.0.0.1:8000")
    parser.add_argument(
        "--translator-languages",
        default=os.getenv(
            "CIVIDOC_TRANSLATOR_LANGUAGES",
            "fr,es,de,it,nl,ca",
        ),
        help=(
            "Comma-separated LibreTranslate target languages. "
            "Example: fr,es,de,it,nl,ca"
        ),
    )

    parser.add_argument(
        "--translator-source-language",
        default=os.getenv(
            "CIVIDOC_TRANSLATOR_SOURCE",
            "en",
        ),
        help="Source documentation language. Default: en",
    )
    parser.add_argument(
    "--translator-url",
    default=os.getenv(
        "CIVIDOC_TRANSLATOR_URL",
        "",
    ),
    help=(
        "LibreTranslate base URL. "
        "Example: http://127.0.0.1:5000"
    ),
)
    return parser.parse_args()


def run_pipeline(args: argparse.Namespace) -> int:
    guides = selected_guides(args.guides)
    paths = make_paths(Path(args.workspace).resolve(), Path(args.output).resolve())
    if args.fidelity_attempts < 1:
        raise RuntimeError("--fidelity-attempts must be at least 1.")
    if args.fresh:
        safe_rmtree(paths.root)
        safe_rmtree(paths.site)

    if args.command in {"run", "sync", "plan"}:
            for guide in guides:
                print(f"Synchronising {guide.label}")
                sync_repository(guide.repository, paths.upstream_for(guide), args.ref)
    if args.command == "sync":
            return 0
    if args.command == "build":
        build_site(paths.site, strict=not args.no_strict)
        return 0
    if args.command == "serve":
        serve_site(paths.site, args.address)
        return 0

    if args.command == "plan":
        print(
            "Preparing the official merged documentation "
            "without AI page rewrites."
        )

        prepare_site(
            paths,
            guides,
            include_rewrites=False,
        )

        restore_official_fallback_pages(paths)

        clean_all_markdown(
            paths,
            guides,
        )

        repair_markdown_targets(
            paths.site / "docs"
        )

        print(
            "Generating the global navigation plan."
        )

        config = configure_mkdocs(
            paths,
            guides,
            args.provider,
            args.model,
            args.preset,
            args.retries,
            args.ai_nav,
            args.refresh_nav,
        )

        validate_nav_files(
            config,
            paths.site / "docs",
        )

        export_navigation_plan(
            paths,
            config,
        )

        print(
            "Navigation planning completed. "
            "No documentation page was rewritten."
        )

        return 0
    
    if args.ai:
        versions_csv = Path(args.versions_csv).resolve()
        rewrite_documents(
            paths,
            guides,
            args.provider,
            args.model,
            args.preset,
            args.retries,
            args.fidelity_attempts,
            parse_csv_paths(args.include),
            parse_csv_paths(args.exclude),
            args.limit,
            args.skip_existing_rewrites,
            versions_csv if versions_csv.exists() else None,
        )
        add_curated_extensions_to_rewritten_pages(
        paths,
        guides,
        )

    prepare_site(paths, guides)
    clean_all_markdown(paths, guides)
    repair_markdown_targets(paths.site / "docs")
    config = configure_mkdocs(
        paths,
        guides,
        args.provider,
        args.model,
        args.preset,
        args.retries,
        args.ai_nav,
        args.refresh_nav,
    )
    validate_nav_files(config, paths.site / "docs")
    audit_documentation(paths, config)
    if not args.skip_build and args.command != "prepare":
        build_site(paths.site, strict=not args.no_strict)
    if args.serve_after:
        serve_site(paths.site, args.address)
    print(f"Documentation is ready in {paths.site}")
    return 0


def main() -> int:
    load_dotenv()
    args = parse_args()
    if args.list_guides:
        for guide in GUIDES.values():
            print(f"{guide.key}: {guide.repository}")
        return 0
    try:
        return run_pipeline(args)
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130
    except subprocess.CalledProcessError as exc:
        print(f"External command failed with exit code {exc.returncode}.", file=sys.stderr)
        return exc.returncode or 1
    except Exception as exc:
        traceback.print_exc()

        print(
            f"Unexpected error: "
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
