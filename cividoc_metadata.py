"""Métadonnées CiviDoc: front matter, dates Git, versions et inférences."""
from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional, Tuple

import yaml

from cividoc_content import (
    ALLOWED_JOURNEY_STAGES, ALLOWED_LEVELS, ALLOWED_TOPICS, AUDIENCE_ALIASES,
    AUDIENCE_KEYWORDS, CATEGORY_ALIASES, COMPONENT_BY_TOPIC, AUDIENCE_DEFINITIONS,
    JOURNEY_STAGE_ALIASES, JOURNEY_STAGE_KEYWORDS, TOPIC_ALIASES, TOPIC_KEYWORDS, COMPONENT_BY_TOPIC,
    GuideConfig,
)

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

AUDIENCE_ALIASES = {
    "new-user": "newcomer",
    "beginner": "newcomer",
    "user": "operations-user",
    "staff": "operations-user",
    "editor": "operations-user",
    "fundraiser": "fundraising-manager",
    "membership": "membership-manager",
    "event": "event-manager",
    "communications": "communications-manager",
    "communication": "communications-manager",
    "admin": "administrator",
    "civicrm-admin": "administrator",
    "system-administrator": "technical",
    "sysadmin": "technical",
    "developer": "technical",
    "implementer": "technical",
}


def normalise_audiences(
    value: Any,
    guide: Optional[GuideConfig] = None,
) -> List[str]:
    """Normalise explicit and guide-level audience values."""

    selected: List[str] = []

    raw_values = normalise_list(value)

    for raw_value in raw_values:
        audience = str(raw_value).strip().casefold()

        audience = AUDIENCE_ALIASES.get(
            audience,
            audience,
        )

        if audience in AUDIENCE_DEFINITIONS:
            selected.append(audience)

    guide_audience: Any = None

    if guide is not None:
        if isinstance(guide, dict):
            guide_audience = guide.get("audience")
        else:
            guide_audience = getattr(
                guide,
                "audience",
                None,
            )

    if guide_audience:
        for raw_value in normalise_list(
            guide_audience
        ):
            audience = (
                str(raw_value)
                .strip()
                .casefold()
            )

            audience = AUDIENCE_ALIASES.get(
                audience,
                audience,
            )

            if (
                audience in AUDIENCE_DEFINITIONS
                and audience not in selected
            ):
                selected.append(audience)

    return list(dict.fromkeys(selected))

TOPIC_AUDIENCES = {
    "introduction": (
        "newcomer",
        "operations-user",
    ),
    "contacts": (
        "operations-user",
        "administrator",
    ),
    "contributions": (
        "fundraising-manager",
        "operations-user",
        "administrator",
    ),
    "pledges": (
        "fundraising-manager",
        "operations-user",
    ),
    "membership": (
        "membership-manager",
        "operations-user",
        "administrator",
    ),
    "events": (
        "event-manager",
        "operations-user",
        "administrator",
    ),
    "email": (
        "communications-manager",
        "operations-user",
        "administrator",
    ),
    "sms": (
        "communications-manager",
        "operations-user",
        "administrator",
    ),
    "campaign": (
        "communications-manager",
        "operations-user",
    ),
    "survey": (
        "communications-manager",
        "operations-user",
    ),
    "petition": (
        "communications-manager",
        "operations-user",
    ),
    "case-management": (
        "operations-user",
        "administrator",
    ),
    "grants": (
        "operations-user",
        "administrator",
    ),
    "searching": (
        "operations-user",
        "administrator",
    ),
    "reporting": (
        "operations-user",
        "administrator",
    ),
    "installation": (
        "technical",
        "administrator",
    ),
    "sysadmin": (
        "technical",
        "administrator",
    ),
    "development": (
        "technical",
        "administrator",
    ),
    "extensions": (
        "technical",
        "administrator",
    ),
}


def infer_audiences(
    metadata: Dict[str, Any],
    body: str,
    guide: Optional[Dict[str, Any]] = None,
) -> List[str]:
    selected = normalise_audiences(
        metadata.get(
            "audiences",
            metadata.get("audience"),
        ),
        guide,
    )

    if metadata.get("audiences_locked") is True:
        return selected

    topic = slugify(
        str(metadata.get("topic", ""))
    )

    component = str(
        metadata.get("component", "")
    ).casefold()

    source_path = str(
        metadata.get("source_path", "")
    ).casefold()

    category = str(
        metadata.get("category", "")
    ).casefold()

    title = str(
        metadata.get("title", "")
    )

    haystack = " ".join(
        (
            title,
            topic,
            component,
            source_path,
            body[:16000],
        )
    ).casefold()

    for audience in TOPIC_AUDIENCES.get(
        topic,
        (),
    ):
        if audience not in selected:
            selected.append(audience)

    path_topic_rules = {
        "contribution": "fundraising-manager",
        "pledge": "fundraising-manager",
        "membership": "membership-manager",
        "event": "event-manager",
        "email": "communications-manager",
        "mail": "communications-manager",
        "sms": "communications-manager",
        "campaign": "communications-manager",
        "install": "technical",
        "sysadmin": "technical",
        "developer": "technical",
        "integration": "technical",
    }

    for needle, audience in path_topic_rules.items():
        if (
            needle in topic
            or needle in component
            or needle in source_path
        ):
            if audience not in selected:
                selected.append(audience)

    scores: Dict[str, int] = {}

    for audience, definition in (
        AUDIENCE_DEFINITIONS.items()
    ):
        score = sum(
            1
            for keyword in definition["keywords"]
            if keyword.casefold() in haystack
        )

        if score:
            scores[audience] = score

    for audience, score in sorted(
        scores.items(),
        key=lambda item: (-item[1], item[0]),
    ):
        if (
            score >= 2
            and audience not in selected
        ):
            selected.append(audience)

    if (
        category == "tutorial"
        and topic in {
            "introduction",
            "getting-started",
        }
        and "newcomer" not in selected
    ):
        selected.insert(0, "newcomer")

    if not selected:
        selected.append("operations-user")

    return selected[:4]

def canonical_category(value: Any) -> str:
    """Return one canonical Diátaxis category."""

    candidate = slugify(
        str(value or "")
    )

    return CATEGORY_ALIASES.get(
        candidate,
        "",
    )

def git_page_revision(
    repository: Path,
    source_path: str,
) -> Tuple[str, str]:
    repository = repository.resolve()

    candidate = Path(source_path)

    if candidate.is_absolute():
        try:
            candidate = candidate.resolve().relative_to(
                repository
            )
        except ValueError:
            return "", ""

    relative_path = candidate.as_posix()

    command = [
        "git",
        "-C",
        str(repository),
        "log",
        "-1",
        "--follow",
        "--format=%H%x09%cI",
        "--",
        relative_path,
    ]

    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    output = completed.stdout.strip()

    if (
        completed.returncode != 0
        or not output
        or "\t" not in output
    ):
        return "", ""

    commit, commit_date = output.split(
        "\t",
        1,
    )

    try:
        parsed_date = datetime.fromisoformat(
            commit_date.replace("Z", "+00:00")
        )

        last_modified = (
            parsed_date.date().isoformat()
        )
    except ValueError:
        last_modified = commit_date[:10]

    return commit.strip(), last_modified

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
    raw_topic = str(metadata.get("topic", "")).strip()
    supplied = slugify(raw_topic) if raw_topic else ""

    supplied = TOPIC_ALIASES.get(
        supplied,
        supplied,
    )

    # Accept only canonical topics. An AI-generated free-form topic must not
    # become a new primary navigation branch.
    if supplied in ALLOWED_TOPICS:
        return supplied
    haystack = f"{relative_path} {title}".casefold()
    # Taxonomie centralisée dans cividoc_content.py.
    if guide.key == "installation":
        return "installation"
    if guide.key == "sysadmin":
        return "extensions" if "extension" in haystack else "system-administration"
    for topic, terms in TOPIC_KEYWORDS.items():
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
    supplied = JOURNEY_STAGE_ALIASES.get(supplied, supplied)
    if supplied in ALLOWED_JOURNEY_STAGES:
        return supplied
    haystack = f"{title} {relative_path}".casefold()
    if title.casefold().startswith("what is "):
        return "overview"
    if any(term in haystack for term in JOURNEY_STAGE_KEYWORDS["extensions-and-integrations"]):
        return "extensions-and-integrations"
    if any(term in haystack for term in JOURNEY_STAGE_KEYWORDS["reports-and-review"]):
        return "reports-and-review"
    if any(term in haystack for term in JOURNEY_STAGE_KEYWORDS["reference-and-troubleshooting"]):
        return "reference-and-troubleshooting"
    if any(term in haystack for term in JOURNEY_STAGE_KEYWORDS["manage-and-automate"]):
        return "manage-and-automate"
    if any(term in haystack for term in JOURNEY_STAGE_KEYWORDS["plan-and-configure"]):
        return "plan-and-configure"
    if category in {"reference", "explanation"}:
        return "reference-and-troubleshooting"
    return "everyday-tasks"

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
    """Build normalised metadata for one documentation page."""

    working_metadata = dict(metadata)

    fallback = (
        PurePosixPath(destination)
        .stem
        .replace("-", " ")
        .replace("_", " ")
        .strip()
        .capitalize()
    )

    title = (
        resolve_page_title(
            working_metadata,
            body,
            source_path,
        )
        or markdown_title(
            body,
            fallback,
        )
    )

    category = canonical_category(
        working_metadata.get("category")
    )

    if not category:
        category = canonical_category(
            infer_category(
                working_metadata,
                body,
            )
        )

    if not category:
        category = "how-to"

    working_metadata["title"] = title
    working_metadata["category"] = category

    topic = infer_topic(
        guide,
        source_path,
        title,
        working_metadata,
    )

    working_metadata["topic"] = topic

    raw_subtopic = str(
        working_metadata.get(
            "subtopic",
            "",
        )
    ).strip()

    subtopic = (
        slugify(raw_subtopic)
        if raw_subtopic
        else ""
    )

    if not subtopic or subtopic == "general":
        parent = PurePosixPath(
            source_path
        ).parent.name

        subtopic = (
            slugify(parent)
            if parent and parent != "."
            else topic
        )

    working_metadata["subtopic"] = subtopic

    component = (
        str(
            working_metadata.get(
                "component",
                "",
            )
        ).strip()
        or COMPONENT_BY_TOPIC.get(
            topic,
            "CiviCRM Core",
        )
    )

    working_metadata["component"] = component

    # infer_audiences() normalise d'abord les audiences explicites,
    # tient compte du guide, puis complète par inférence.
    audiences = infer_audiences(
        working_metadata,
        body,
        guide,
    )

    if not audiences:
        audiences = ["operations-user"]

    audiences = list(
        dict.fromkeys(audiences)
    )

    working_metadata["audiences"] = audiences
    working_metadata.pop(
        "audience",
        None,
    )

    level = str(
        working_metadata.get(
            "level",
            "basic",
        )
    ).strip().casefold()

    if level not in ALLOWED_LEVELS:
        level = "basic"

    working_metadata["level"] = level

    journey_stage = infer_journey_stage(
        title,
        category,
        source_path,
        working_metadata,
    )

    notes = normalise_list(
        working_metadata.get(
            "review_notes"
        )
    )

    supplied_versions = (
        civicrm_versions
        or normalise_list(
            working_metadata.get(
                "civicrm_versions"
            )
        )
        or normalise_list(
            working_metadata.get(
                "civicrm_version"
            )
        )
        or ["latest"]
    )

    supplied_versions = list(
        dict.fromkeys(
            str(version).strip()
            for version in supplied_versions
            if str(version).strip()
        )
    )

    if not supplied_versions:
        supplied_versions = ["latest"]

    supplied_legacy_urls = (
        legacy_urls
        or normalise_list(
            working_metadata.get(
                "legacy_urls"
            )
        )
    )

    if not supplied_legacy_urls:
        default_legacy_url = official_legacy_url(
            guide,
            source_path,
        )

        supplied_legacy_urls = (
            [default_legacy_url]
            if default_legacy_url
            else []
        )

    supplied_legacy_urls = list(
        dict.fromkeys(
            str(url).strip()
            for url in supplied_legacy_urls
            if str(url).strip()
        )
    )

    result: Dict[str, Any] = {
        "title": title,
        "category": category,
        "topic": topic,
        "subtopic": subtopic,
        "component": component,
        "audiences": audiences,
        "level": level,
        "journey_stage": journey_stage,
        "summary": (
            str(
                working_metadata.get(
                    "summary",
                    "",
                )
            ).strip()
            or infer_summary(body)
        ),
        "extensions": normalise_list(
            working_metadata.get(
                "extensions"
            )
        ),
        "related": normalise_list(
            working_metadata.get(
                "related"
            )
        ),
        "review_priority": (
            review_priority_from_notes(
                notes
            )
        ),
        "review_notes": notes,
        "guide": guide.key,
        "source_repository": (
            source_repository
        ),
        "source_path": source_path,
        "destination_path": destination,
        "legacy_urls": supplied_legacy_urls,
        # On conserve ce nom pour compatibilité avec le code actuel.
        "civicrm_version": supplied_versions,
    }

    if source_commit:
        result["source_commit"] = (
            source_commit.strip()
        )

    effective_last_modified = (
        str(last_modified).strip()
        or str(
            working_metadata.get(
                "last_modified",
                "",
            )
        ).strip()
    )

    if effective_last_modified:
        result["last_modified"] = (
            effective_last_modified
        )
        
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
