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
from cividoc_translation import install_translator

import yaml

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args: Any, **kwargs: Any) -> bool:
        return False













# Audience is a small, controlled reader taxonomy. Functional jobs such as
# event manager, fundraiser, or mailing author belong in topic/subtopic, not in
# a new audience branch.















from cividoc_content import (
    ALLOWED_CATEGORIES, ALLOWED_JOURNEY_STAGES, ALLOWED_TOPICS,
    BROWSE_DIR, CURATED_EXTENSIONS_END, CURATED_EXTENSIONS_REVIEWED_ON, CURATED_EXTENSIONS_START,
    DEFAULT_FIDELITY_ATTEMPTS, DEFAULT_GUIDES, DEFAULT_OUTPUT, DEFAULT_WORKSPACE,
    EXTENSION_CATALOG_BY_COMPONENT, FIDELITY_CORRECTION_PROMPT, GUIDES,
    PIPELINE_VERSION, REWRITE_PROMPT,
    REWRITE_PROMPT_VERSION, GuideConfig,
)
from cividoc_metadata import (
    build_markdown_with_front_matter, detect_civicrm_versions, git_value, git_page_revision, load_civicrm_versions, normalise_list,
    normalise_metadata, official_legacy_url, review_priority_from_notes, split_front_matter,
)
from cividoc_nav import (
    build_global_navigation, collect_nav_paths, export_navigation_plan,
    generate_browse_indexes, page_inventory, topic_label, topic_sort_key,
    validate_nav_files,
)
from cividoc_translation import install_translator

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

















# === CIVIDOC V8 GENERATED OVERRIDES: START ===
# Snapshot of the official CiviCRM extensions directory, ordered by reported
# Current Usage within each official category. Deprecated, temporary hotfix,
# and dependency-only packages are excluded from editorial recommendations.



def remove_curated_extensions_section(body: str) -> str:
    patterns = [
        re.compile(
            rf"\n*{re.escape(CURATED_EXTENSIONS_START)}.*?{re.escape(CURATED_EXTENSIONS_END)}\n*",
            flags=re.DOTALL,
        ),
        re.compile(
            r"\n*<!--\s*curated-extensions(?::start|_start| start)?\s*-->.*?"
            r"<!--\s*curated-extensions(?::end|_end| end)?\s*-->\n*",
            flags=re.DOTALL | re.IGNORECASE,
        ),
    ]
    cleaned = body
    for pattern in patterns:
        cleaned = pattern.sub("\n\n", cleaned)
    return cleaned.strip()


def render_curated_extensions_section(component: str) -> str:
    configuration = EXTENSION_CATALOG_BY_COMPONENT.get(component)
    if not configuration:
        return ""
    category_id = int(configuration["category_id"])
    unique: List[Tuple[str, str, int]] = []
    seen: set[str] = set()
    for name, slug, usage in configuration.get("items", []):
        folded = str(name).strip().casefold()
        if folded in seen:
            continue
        seen.add(folded)
        unique.append((str(name).strip(), str(slug).strip(), int(usage)))
        if len(unique) == 5:
            break
    if len(unique) < 3:
        return ""
    lines = [
        CURATED_EXTENSIONS_START,
        "## Popular extensions",
        "",
        (
            "These are widely used extensions in the relevant category of the "
            "official CiviCRM Extensions Directory. Usage is a popularity signal, "
            "not a compatibility or suitability guarantee."
        ),
        "",
    ]
    for name, slug, usage in unique:
        if slug.startswith("../"):
            url = "https://civicrm.org/" + slug[3:]
        else:
            url = "https://civicrm.org/extensions/" + slug
        lines.append(f"- [{name}]({url}) — reported usage: {usage:,}")
    directory = f"https://civicrm.org/extensions?category={category_id}"
    lines.extend([
        "",
        f"[All extensions for this component]({directory})",
        "",
        (
            "Check development status, current CiviCRM compatibility, CMS "
            "requirements, and release notes before installation."
        ),
        "",
        f"Usage snapshot reviewed: {CURATED_EXTENSIONS_REVIEWED_ON}.",
        CURATED_EXTENSIONS_END,
    ])
    return "\n".join(lines)


def insert_curated_extensions_section(body: str, section: str) -> str:
    clean = remove_curated_extensions_section(body)
    if not section:
        return clean
    source = re.search(r"(?im)^\s*<!--\s*Source:.*?-->\s*$", clean)
    if not source:
        return f"{clean.rstrip()}\n\n{section.strip()}\n"
    before = clean[:source.start()].rstrip()
    comment = clean[source.start():].strip()
    return f"{before}\n\n{section.strip()}\n\n{comment}\n"


def curated_extensions_candidate_score(metadata: Dict[str, Any]) -> int:
    title = str(metadata.get("title", "")).strip().casefold()
    stage = str(metadata.get("journey_stage", "")).strip()
    if title.startswith("what is "):
        return 0
    if stage == "overview":
        return 1
    if stage == "extensions-and-integrations":
        return 2
    if str(metadata.get("category", "")) == "explanation":
        return 3
    return 100


def add_curated_extensions_to_site(docs_root: Path) -> None:
    """Add one idempotent popular-extension section to each documented component."""
    candidates: Dict[str, List[Tuple[int, int, Path, Dict[str, Any], str]]] = defaultdict(list)
    cleaned: List[Tuple[Path, Dict[str, Any], str]] = []
    sequence = 0
    for page in iter_markdown(docs_root):
        if BROWSE_DIR in page.parts:
            continue
        metadata, body = split_front_matter(page.read_text(encoding="utf-8-sig"))
        clean = remove_curated_extensions_section(body)
        cleaned.append((page, metadata, clean))
        component = str(metadata.get("component", "")).strip()
        if component not in EXTENSION_CATALOG_BY_COMPONENT:
            continue
        score = curated_extensions_candidate_score(metadata)
        if score < 100:
            candidates[component].append((score, sequence, page, metadata, clean))
        sequence += 1

    for page, metadata, clean in cleaned:
        page.write_text(build_markdown_with_front_matter(metadata, clean), encoding="utf-8")

    for component, options in candidates.items():
        options.sort(key=lambda item: (item[0], item[1]))
        _, _, page, metadata, body = options[0]
        enriched = insert_curated_extensions_section(
            body,
            render_curated_extensions_section(component),
        )
        page.write_text(build_markdown_with_front_matter(metadata, enriched), encoding="utf-8")
        print(f"Added popular extensions: {component} -> {page}")



# === CIVIDOC V8 GENERATED OVERRIDES: END ===

















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
    """Build metadata using the source page and its Git history."""

    repository = paths.upstream_for(guide)

    repository_relative_path = (
        PurePosixPath("docs")
        / PurePosixPath(source_relative)
    ).as_posix()

    source_commit, last_modified = (
        git_page_revision(
            repository,
            repository_relative_path,
        )
    )

    versions = normalise_list(
        metadata.get("civicrm_versions")
        or metadata.get("civicrm_version")
    )

    if not versions:
        versions = ["latest"]

    legacy_url = official_legacy_url(
        guide,
        source_relative,
    )

    legacy_urls = (
        [legacy_url]
        if legacy_url
        else []
    )

    return normalise_metadata(
        metadata=metadata,
        body=body,
        destination=destination,
        guide=guide,
        source_path=source_relative,
        source_repository=guide.repository,
        source_commit=source_commit,
        last_modified=last_modified,
        civicrm_versions=versions,
        legacy_urls=legacy_urls,
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
    translator_languages: Optional[
        List[str]
    ] = None,
    translator_source_language: str = "en",
) -> Dict[str, Any]:
    """Create the unified MkDocs configuration."""

    primary = next(
        (
            guide
            for guide in guides
            if guide.key == "user-en"
        ),
        guides[0],
    )

    config = load_yaml(
        paths.upstream_for(primary)
        / "mkdocs.yml"
    )

    if not isinstance(config, dict):
        config = {}

    if not config:
        config = {
            "site_name": (
                "CiviCRM Documentation"
            ),
            "theme": {
                "name": "material",
                "language": "en",
            },
            "plugins": [
                "search",
            ],
            "markdown_extensions": [
                "admonition",
                "toc",
            ],
        }

    config.update({
        "site_name": (
            "CiviCRM Documentation"
        ),
        "docs_dir": "docs",
        "site_dir": "site",
        "use_directory_urls": True,
    })

    theme = config.get("theme")

    if isinstance(theme, str):
        theme = {
            "name": theme,
        }
    elif not isinstance(theme, dict):
        theme = {
            "name": "material",
        }

    theme.setdefault(
        "name",
        "material",
    )

    theme.setdefault(
        "language",
        "en",
    )

    config["theme"] = theme

    extra = config.get("extra")

    if not isinstance(extra, dict):
        extra = {}

    version_config = extra.get("version")

    if not isinstance(version_config, dict):
        version_config = {}

    version_config.setdefault(
        "provider",
        "mike",
    )

    extra["version"] = version_config
    config["extra"] = extra

    official_navs: Dict[str, Any] = {}

    for guide in guides:
        source_config = load_yaml(
            paths.upstream_for(guide)
            / "mkdocs.yml"
        )

        if not isinstance(
            source_config,
            dict,
        ):
            source_config = {}

        official_navs[guide.key] = (
            source_config.get(
                "nav",
                [],
            )
        )

    docs_root = (
        paths.site
        / "docs"
    )

    add_curated_extensions_to_site(
        docs_root
    )

    inventory = page_inventory(
        docs_root,
        official_navs,
    )

    main_nav = build_global_navigation(
        paths,
        inventory,
        provider,
        model,
        preset,
        retries,
        ai_navigation,
        refresh_navigation,
        ai_request,
    )

    category_nav, audience_nav = (
        generate_browse_indexes(
            docs_root,
            inventory,
        )
    )

    browse_navigation: List[Any] = []

    if category_nav:
        browse_navigation.append({
            "By content category":
                category_nav,
        })

    if audience_nav:
        browse_navigation.append({
            "By audience":
                audience_nav,
        })

    if browse_navigation:
        main_nav.append({
            "Browse":
                browse_navigation,
        })

    config["nav"] = main_nav

    plugins = config.get(
        "plugins",
        ["search"],
    )

    if not isinstance(plugins, list):
        plugins = ["search"]

    filtered_plugins: List[Any] = []
    has_search = False

    for plugin in plugins:
        if isinstance(plugin, str):
            plugin_name = plugin
        elif isinstance(plugin, dict):
            plugin_name = next(
                iter(plugin),
                "",
            )
        else:
            plugin_name = ""

        if plugin_name == "categories":
            continue

        if plugin_name == "search":
            has_search = True

        filtered_plugins.append(plugin)

    if not has_search:
        filtered_plugins.insert(
            0,
            "search",
        )

    config["plugins"] = filtered_plugins

    raw_extra_css = config.get(
        "extra_css",
        [],
    )

    if isinstance(raw_extra_css, str):
        extra_css: List[Any] = [
            raw_extra_css,
        ]
    elif isinstance(
        raw_extra_css,
        list,
    ):
        extra_css = list(
            raw_extra_css
        )
    else:
        extra_css = []

    required_stylesheets = (
        "css/cividoc-index-pages.css",
    )

    for stylesheet in required_stylesheets:
        if stylesheet not in extra_css:
            extra_css.append(
                stylesheet
            )

    config["extra_css"] = extra_css

    if translator_url:
        source_language = (
            translator_source_language
            .strip()
            or "en"
        )

        target_languages = list(
            dict.fromkeys(
                language.strip()
                for language in (
                    translator_languages
                    or []
                )
                if language.strip()
                and language.strip()
                != source_language
            )
        )

        if target_languages:
            install_translator(
                site=paths.site,
                config=config,
                endpoint=translator_url,
                target_languages=(
                    target_languages
                ),
                source_language=(
                    source_language
                ),
            )

            print(
                "Installed LibreTranslate "
                "switcher: "
                f"{source_language} -> "
                f"{', '.join(target_languages)}"
            )

    raw_extra_css = config.get(
        "extra_css",
        [],
    )

    if isinstance(raw_extra_css, str):
        final_extra_css: List[Any] = [
            raw_extra_css,
        ]
    elif isinstance(
        raw_extra_css,
        list,
    ):
        final_extra_css = list(
            raw_extra_css
        )
    else:
        final_extra_css = []

    for stylesheet in (
        "css/cividoc-index-pages.css",
    ):
        if stylesheet not in final_extra_css:
            final_extra_css.append(
                stylesheet
            )

    config["extra_css"] = (
        final_extra_css
    )

    config_path = (
        paths.site
        / "mkdocs.yml"
    )

    config_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    config_path.write_text(
        yaml.safe_dump(
            config,
            sort_keys=False,
            allow_unicode=True,
            width=140,
        ),
        encoding="utf-8",
    )

    return config



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
            args.translator_url or None,
            parse_csv_paths(args.translator_languages),
            args.translator_source_language,
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
        args.translator_url or None,
        parse_csv_paths(args.translator_languages),
        args.translator_source_language,
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
