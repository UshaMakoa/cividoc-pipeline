"""Navigation CiviDoc: plans, validation, catégories et index de consultation."""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple
from html import escape

import yaml

from cividoc_content import (
    AUDIENCE_LABELS,
    BROWSE_DIR,
    CATEGORY_LABELS,
    DOMAIN_ORDER,
    GUIDES,
    MAX_MAIN_ROOT_CHOICES,
    MAX_NAV_CHOICES,
    MAX_NAV_DEPTH,
    NAVIGATION_PROMPT,
    NAVIGATION_PROMPT_VERSION,
    STAGE_LABELS,
    STAGE_ORDER,
    TOPIC_DOMAIN,
    TOPIC_LABELS,
    INDEX_PAGES_CSS,
)
from cividoc_metadata import (
    markdown_title,
    normalise_list,
    resolve_page_title,
    split_front_matter,
)

Paths = Any

# Libellés de secours. Les valeurs définies dans cividoc_content.py restent
# prioritaires, mais ces huit audiences garantissent une navigation complète.
DEFAULT_AUDIENCE_LABELS: Dict[str, str] = {
    "newcomer": "Newcomers",
    "day-to-day-user": "Day-to-day users",
    "fundraising-manager": "Fundraising teams",
    "membership-manager": "Membership teams",
    "event-manager": "Event teams",
    "communications-manager": "Communications teams",
    "administrator": "CiviCRM administrators",
    "technical": "System administrators and developers",
}

AUDIENCE_ALIASES: Dict[str, str] = {
    "new-user": "newcomer",
    "new-users": "newcomer",
    "operations-user": "day-to-day-user",
    "operational-user": "day-to-day-user",
    "user": "day-to-day-user",
    "users": "day-to-day-user",
    "fundraiser": "fundraising-manager",
    "fundraising": "fundraising-manager",
    "membership": "membership-manager",
    "event": "event-manager",
    "events": "event-manager",
    "communications": "communications-manager",
    "communication-manager": "communications-manager",
    "admin": "administrator",
    "civicrm-administrator": "administrator",
    "system-administrator": "technical",
    "developer": "technical",
    "developers": "technical",
}

AUDIENCE_INTROS: Dict[str, str] = {
    "newcomer": "Discover CiviCRM and learn its essential concepts and first steps.",
    "day-to-day-user": "Manage contacts, activities, searches and routine records.",
    "fundraising-manager": "Manage fundraising, donations, payments and pledges.",
    "membership-manager": "Manage members, renewals and membership programmes.",
    "event-manager": "Create events and manage registrations and participants.",
    "communications-manager": "Manage email, SMS, campaigns and supporter communications.",
    "administrator": "Configure CiviCRM, permissions, forms and workflows.",
    "technical": "Install, maintain, integrate and extend CiviCRM.",
}

# Renommage uniquement des sections de navigation, jamais des titres de pages.
ACCESSIBLE_SECTION_LABELS: Dict[str, str] = {
    "contributions and pledges": "Fundraising, donations and pledges",
    "contributions and payments": "Fundraising forms and payments",
    "contacts and activities": "People, organisations and activities",
    "mailings and communications": "Email, SMS and communications",
    "search and reports": "Search, lists and reports",
}


def effective_audience_labels() -> Dict[str, str]:
    """Return the canonical eight labels, overridden by project configuration."""
    labels = dict(DEFAULT_AUDIENCE_LABELS)
    for raw_key, raw_label in AUDIENCE_LABELS.items():
        key = canonical_audience(str(raw_key))
        label = str(raw_label).strip()
        if key and label:
            labels[key] = label
    return labels


def canonical_audience(value: str) -> str:
    """Normalise current and legacy audience identifiers."""
    slug = re.sub(r"[^a-z0-9]+", "-", str(value).strip().casefold()).strip("-")
    return AUDIENCE_ALIASES.get(slug, slug)


def page_audiences(page: Dict[str, Any]) -> List[str]:
    """Return unique canonical audiences explicitly stored on a page."""
    result: List[str] = []
    for value in normalise_list(page.get("audiences")):
        audience = canonical_audience(str(value))
        if audience and audience not in result:
            result.append(audience)
    return result


def accessible_section_label(title: str) -> str:
    """Use newcomer-friendly wording for known internal CiviCRM concepts."""
    clean = str(title).strip()
    return ACCESSIBLE_SECTION_LABELS.get(clean.casefold(), clean)


def install_index_page_css(
    docs_root: Path,
) -> str:
    """Install the stylesheet used by generated browse indexes."""

    relative_path = (
        Path("css")
        / "cividoc-index-pages.css"
    )

    destination = (
        docs_root
        / relative_path
    )

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    destination.write_text(
        INDEX_PAGES_CSS.strip() + "\n",
        encoding="utf-8",
    )

    return relative_path.as_posix()

def iter_markdown(folder: Path) -> Iterable[Path]:
    if folder.exists():
        yield from sorted(folder.rglob("*.md"))


def destination_path(guide: Any, relative_path: str) -> str:
    relative_path = relative_path.replace("\\", "/").lstrip("/")
    return (
        f"{guide.destination_prefix}/{relative_path}"
        if guide.destination_prefix
        else relative_path
    )


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


def safe_rmtree(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


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
        compacted.append(
            {
                "title": accessible_section_label(str(node.get("title", ""))),
                "children": children,
            }
        )
    return compacted

def page_metadata_value(
    page: Dict[str, Any],
    key: str,
    default: Any = "",
) -> Any:
    """Read a value from a flattened or nested inventory page."""

    value = page.get(key)

    if value not in (
        None,
        "",
        [],
    ):
        return value

    metadata = page.get("metadata")

    if isinstance(metadata, dict):
        value = metadata.get(key)

        if value not in (
            None,
            "",
            [],
        ):
            return value

    return default


def readable_label(
    value: Any,
) -> str:
    """Turn a metadata slug into a readable label."""

    text = str(value or "").strip()

    if not text:
        return ""

    return (
        text
        .replace("_", " ")
        .replace("-", " ")
        .strip()
        .title()
    )


def metadata_list(
    value: Any,
) -> List[str]:
    """Normalise display metadata into unique strings."""

    if value is None:
        values: List[Any] = []
    elif isinstance(
        value,
        (list, tuple, set),
    ):
        values = list(value)
    else:
        values = [value]

    return list(
        dict.fromkeys(
            str(item).strip()
            for item in values
            if str(item).strip()
        )
    )


def index_card_html(
    page: Dict[str, Any],
    link: str,
) -> List[str]:
    """Render one category or audience index card."""

    title = escape(
        str(
            page_metadata_value(
                page,
                "title",
                "Untitled page",
            )
        ).strip()
    )

    topic = readable_label(
        page_metadata_value(
            page,
            "topic",
        )
    )

    component = str(
        page_metadata_value(
            page,
            "component",
        )
    ).strip()

    level = readable_label(
        page_metadata_value(
            page,
            "level",
            "basic",
        )
    )

    summary = escape(
        str(
            page_metadata_value(
                page,
                "summary",
            )
        ).strip()
    )

    versions = metadata_list(
        page_metadata_value(
            page,
            "civicrm_versions",
            page_metadata_value(
                page,
                "civicrm_version",
            ),
        )
    )

    last_modified = str(
        page_metadata_value(
            page,
            "last_modified",
        )
    ).strip()

    primary_metadata = list(
        dict.fromkeys(
            value
            for value in (
                topic,
                component,
                level,
            )
            if value
        )
    )

    detail_items: List[str] = []

    if versions:
        detail_items.append(
            "CiviCRM "
            + ", ".join(
                escape(version)
                for version in versions
            )
        )

    if last_modified:
        detail_items.append(
            "Updated "
            + escape(last_modified)
        )

    lines = [
        "<li>",
        (
            f'  <a href="{escape(link, quote=True)}">'
            f"<strong>{title}</strong>"
            "</a>"
        ),
    ]

    if primary_metadata:
        lines.append(
            '  <span class="cividoc-category-meta">'
            + " · ".join(
                escape(value)
                for value in primary_metadata
            )
            + "</span>"
        )

    if summary:
        lines.append(
            '  <span class="cividoc-category-summary">'
            + summary
            + "</span>"
        )

    if detail_items:
        lines.append(
            '  <span class="cividoc-category-details">'
        )

        for detail in detail_items:
            lines.append(
                f"    <span>{detail}</span>"
            )

        lines.append(
            "  </span>"
        )

    lines.append("</li>")

    return lines

def nav_entries(
    nav: Any,
    breadcrumbs: Optional[List[str]] = None,
) -> List[Tuple[str, List[str]]]:
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


def page_inventory(
    docs_root: Path,
    official_navs: Dict[str, Any],
) -> List[Dict[str, Any]]:
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
        title = resolve_page_title(metadata, body, path) or markdown_title(body, page.stem)
        current_order, breadcrumbs = positions.get(path, (next_order, []))
        if path not in positions:
            next_order += 1

        versions = (
            normalise_list(metadata.get("civicrm_versions"))
            or normalise_list(metadata.get("civicrm_version"))
        )
        audiences = [
            canonical_audience(str(value))
            for value in normalise_list(metadata.get("audiences"))
            if canonical_audience(str(value))
        ]

        inventory.append(
            {
                "id": "",
                "destination_path": path,
                "title": title,
                "summary": str(metadata.get("summary", "")).strip(),
                "word_count": len(re.findall(r"\b\w+\b", body)),
                "h2_count": len(re.findall(r"(?m)^##\s+", body)),
                "topic": str(metadata.get("topic", "general")).strip(),
                "subtopic": str(metadata.get("subtopic", "general")).strip(),
                "component": str(metadata.get("component", "CiviCRM Core")).strip(),
                "category": str(metadata.get("category", "reference")).strip(),
                "audiences": list(dict.fromkeys(audiences)),
                "level": str(metadata.get("level", "basic")).strip(),
                "journey_stage": str(
                    metadata.get("journey_stage", "everyday-tasks")
                ).strip(),
                "guide": str(metadata.get("guide", "user-en")).strip(),
                "civicrm_version": versions,
                "last_modified": str(metadata.get("last_modified", "")).strip(),
                "current_order": current_order,
                "current_breadcrumbs": breadcrumbs,
            }
        )

    inventory.sort(key=lambda item: (item["current_order"], item["destination_path"]))
    for index, item in enumerate(inventory, 1):
        item["id"] = f"p{index:05d}"
    return inventory


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
        return [
            normalise_navigation_titles(item, fallback_title)
            for item in node
            if item is not None
        ]
    if not isinstance(node, dict):
        return node
    if set(node) == {"page_id"}:
        return {"page_id": str(node.get("page_id", "")).strip()}
    children = node.get("children", [])
    title = str(node.get("title", "")).strip() or fallback_title
    return {
        "title": accessible_section_label(title),
        "children": normalise_navigation_titles(children, fallback_title),
    }


def validate_navigation_plan(
    plan: Any,
    expected_ids: List[str],
    depth: int = 0,
) -> None:
    if depth > MAX_NAV_DEPTH:
        raise RuntimeError(
            f"Invalid navigation plan: more than {MAX_NAV_DEPTH} section levels before a page."
        )
    if not isinstance(plan, list):
        raise RuntimeError("Invalid navigation plan: nav must be an array.")

    sibling_sections: Counter[str] = Counter()
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
            sibling_sections[title.casefold()] += 1
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

    duplicate_sections = sorted(
        label for label, count in sibling_sections.items() if count > 1
    )
    if duplicate_sections:
        raise RuntimeError(
            "Invalid navigation plan: duplicate sibling section labels (case-insensitive): "
            + ", ".join(duplicate_sections)
        )

    if depth == 0:
        actual = plan_id_entries(plan)
        duplicates = sorted(
            page_id for page_id, count in Counter(actual).items() if count > 1
        )
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


def resolve_navigation_plan(
    plan: List[Any],
    inventory: List[Dict[str, Any]],
) -> List[Any]:
    """Resolve page ids and disambiguate sibling labels case-insensitively."""
    by_id = {item["id"]: item for item in inventory}

    def resolve(nodes: List[Any]) -> List[Any]:
        bases: List[str] = []
        for node in nodes:
            if "page_id" in node:
                page = by_id[node["page_id"]]
                base = "Home" if page["destination_path"] == "index.md" else str(page["title"])
            else:
                base = accessible_section_label(str(node["title"]))
            bases.append(base.strip() or "Untitled")

        counts = Counter(label.casefold() for label in bases)
        used: Counter[str] = Counter()
        result: List[Any] = []
        for node, base in zip(nodes, bases):
            label = base
            folded = base.casefold()
            if counts[folded] > 1:
                if "page_id" in node:
                    page = by_id[node["page_id"]]
                    context = str(
                        page.get("component")
                        or topic_label(str(page.get("topic", "general")))
                    )
                    candidate = f"{base} — {context}"
                    if candidate.casefold() in used:
                        guide = str(page.get("guide", "documentation")).replace("-", " ").title()
                        candidate = f"{base} — {context} ({guide})"
                    if candidate.casefold() in used:
                        parent = (
                            PurePosixPath(str(page["destination_path"]))
                            .parent.name.replace("-", " ")
                            .title()
                        )
                        candidate = f"{candidate} — {parent}"
                    label = candidate
                else:
                    used[folded] += 1
                    label = f"{base} ({used[folded]})"
            used[label.casefold()] += 1
            if "page_id" in node:
                page = by_id[node["page_id"]]
                result.append({label: page["destination_path"]})
            else:
                result.append({label: resolve(node["children"])})
        return result

    return resolve(plan)


def topic_label(topic: str) -> str:
    return TOPIC_LABELS.get(topic, topic.replace("-", " ").title())


def topic_sort_key(topic: str) -> Tuple[int, str]:
    preferred = list(TOPIC_LABELS)
    return (preferred.index(topic) if topic in preferred else 999, topic)


def balanced_chunks(
    items: List[Dict[str, Any]],
    maximum: int,
) -> List[List[Dict[str, Any]]]:
    """Split items without creating an oversized or singleton chunk."""
    if maximum < 2:
        raise ValueError("maximum must be at least 2")
    if len(items) <= maximum:
        return [items]

    chunk_count = (len(items) + maximum - 1) // maximum
    base_size, remainder = divmod(len(items), chunk_count)
    chunks: List[List[Dict[str, Any]]] = []
    start = 0
    for index in range(chunk_count):
        size = base_size + (1 if index < remainder else 0)
        chunks.append(items[start : start + size])
        start += size
    return chunks


def deterministic_navigation_plan(inventory: List[Dict[str, Any]]) -> List[Any]:
    """Build a shallow fallback: domain -> topic -> optional stage -> page."""
    by_domain: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for page in inventory:
        if page["destination_path"] == "index.md":
            continue
        topic = str(page.get("topic", "general"))
        domain = TOPIC_DOMAIN.get(topic, "Configure, automate and extend")
        by_domain[domain][topic].append(page)

    roots: List[Any] = []
    home = next(
        (page for page in inventory if page["destination_path"] == "index.md"),
        None,
    )
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
                    stage_chunks = balanced_chunks(stage_pages, MAX_NAV_CHOICES)
                    offset = 0
                    for chunk in stage_chunks:
                        first_position = offset + 1
                        last_position = offset + len(chunk)
                        offset = last_position
                        chunk_label = (
                            label
                            if len(stage_chunks) == 1
                            else f"{label} — entries {first_position}–{last_position}"
                        )
                        children.append(
                            {
                                "title": chunk_label,
                                "children": [
                                    {"page_id": page["id"]} for page in chunk
                                ],
                            }
                        )
            topic_nodes.append(
                {"title": topic_label(topic), "children": children}
            )
        roots.append(
            {"title": accessible_section_label(domain), "children": topic_nodes}
        )

    roots = normalise_navigation_titles(roots)
    return collapse_single_child_sections(roots)


def build_global_navigation(
    paths: "Paths",
    inventory: List[Dict[str, Any]],
    provider: str,
    model: str,
    preset: str,
    retries: int,
    request_ai: bool,
    refresh: bool,
    ai_request_fn: Callable[..., str],
) -> List[Any]:
    expected_ids = [item["id"] for item in inventory]
    digest = sha256_json(
        {
            "version": NAVIGATION_PROMPT_VERSION,
            "prompt": NAVIGATION_PROMPT,
            "provider": provider,
            "model": model,
            "preset": preset,
            "inventory": inventory,
        }
    )
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
                raw = ai_request_fn(
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
            print(
                "AI navigation was rejected after 3 attempts; "
                "using the shallow deterministic fallback."
            )
            source = "deterministic-fallback"

    plan = normalise_navigation_titles(plan)
    plan = collapse_single_child_sections(plan)
    validate_navigation_plan(plan, expected_ids)
    save_json(
        cache_path,
        {
            "sha256": digest,
            "plan": plan,
            "source": source,
            "id_to_path": {
                item["id"]: item["destination_path"] for item in inventory
            },
        },
    )
    return resolve_navigation_plan(plan, inventory)


def relative_link(from_path: str, to_path: str) -> str:
    directory = posixpath.dirname(from_path) or "."
    return posixpath.relpath(to_path, directory)


def write_generated_index(
    docs_root: Path,
    relative_path: str,
    title: str,
    intro: str,
    groups: List[
        Tuple[
            str,
            List[Dict[str, Any]],
        ]
    ],
) -> None:
    """Generate a styled category or audience index."""

    normalised_relative_path = (
        relative_path
        .replace("\\", "/")
        .casefold()
    )

    is_audience_index = (
        "/audiences/" in normalised_relative_path
        or normalised_relative_path.startswith(
            "_browse/audiences/"
        )
    )

    list_class = (
        "cividoc-audience-list"
        if is_audience_index
        else "cividoc-category-list"
    )

    lines: List[str] = [
        "---",
        f"title: {json.dumps(title)}",
        "generated_index: true",
        "hide:",
        "  - toc",
        "---",
        "",
        f"# {title}",
        "",
        intro,
        "",
    ]

    page_count = sum(
        len(pages)
        for _, pages in groups
    )

    section_type = (
        "audience"
        if is_audience_index
        else "section"
    )

    lines.extend([
        (
            f"{page_count} page(s) "
            f"in this {section_type}."
        ),
        "",
    ])

    rendered_group = False

    for heading, pages in groups:
        if not pages:
            continue

        rendered_group = True

        if heading:
            lines.extend([
                f"## {heading}",
                "",
            ])

        lines.extend([
            f'<div class="{list_class}">',
            "<ul>",
        ])

        for page in pages:
            raw_destination = str(
                page.get(
                    "destination_path",
                    "",
                )
            ).strip()

            target = relative_link(
                relative_path,
                raw_destination,
            )

            page_title = escape(
                str(
                    page.get(
                        "title",
                        "Untitled page",
                    )
                ).strip()
            )

            safe_target = escape(
                target,
                quote=True,
            )

            details: List[str] = []

            topic = str(
                page.get(
                    "topic",
                    "general",
                )
            ).strip()

            if topic:
                details.append(
                    topic_label(topic)
                )

            component = str(
                page.get(
                    "component",
                    "",
                )
            ).strip()

            if component and (
                not details
                or component.casefold()
                != details[0].casefold()
            ):
                details.append(component)

            level = str(
                page.get(
                    "level",
                    "",
                )
            ).strip()

            if level:
                details.append(
                    level
                    .replace("-", " ")
                    .title()
                )

            versions = (
                normalise_list(
                    page.get(
                        "civicrm_versions"
                    )
                )
                or normalise_list(
                    page.get(
                        "civicrm_version"
                    )
                )
            )

            last_modified = str(
                page.get(
                    "last_modified",
                    "",
                )
            ).strip()

            summary = escape(
                str(
                    page.get(
                        "summary",
                        "",
                    )
                ).strip()
            )

            lines.extend([
                "<li>",
                (
                    f'  <a href="{safe_target}">'
                    f"<strong>{page_title}</strong>"
                    "</a>"
                ),
            ])

            if details:
                safe_details = (
                    " · ".join(
                        escape(
                            str(detail)
                        )
                        for detail in details
                        if str(detail).strip()
                    )
                )

                if safe_details:
                    lines.append(
                        "  "
                        '<span class="'
                        'cividoc-category-meta">'
                        f"{safe_details}"
                        "</span>"
                    )

            if summary:
                lines.append(
                    "  "
                    '<span class="'
                    'cividoc-category-summary">'
                    f"{summary}"
                    "</span>"
                )

            secondary_details: List[str] = []

            if versions:
                secondary_details.append(
                    "CiviCRM "
                    + ", ".join(
                        escape(
                            str(version)
                        )
                        for version in versions
                    )
                )

            if last_modified:
                secondary_details.append(
                    "Updated "
                    + escape(last_modified)
                )

            if secondary_details:
                lines.append(
                    "  "
                    '<span class="'
                    'cividoc-category-details">'
                )

                for detail in secondary_details:
                    lines.append(
                        f"    <span>{detail}</span>"
                    )

                lines.append(
                    "  </span>"
                )

            lines.append("</li>")

        lines.extend([
            "</ul>",
            "</div>",
            "",
        ])

    if not rendered_group:
        lines.extend([
            "_No pages are currently available "
            "in this section._",
            "",
        ])

    target_path = (
        docs_root
        / Path(relative_path)
    )

    target_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    target_path.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )

def group_label(page: Dict[str, Any]) -> str:
    """Return a stable functional heading for generated browse pages."""
    topic = str(page.get("topic", "general"))
    if topic != "general":
        domain = TOPIC_DOMAIN.get(topic, "Other")
        return f"{accessible_section_label(domain)} — {topic_label(topic)}"
    crumbs = [
        str(value).strip()
        for value in page.get("current_breadcrumbs", [])
        if str(value).strip()
        and str(value).strip().casefold() not in {"general", "basic", "overview"}
    ]
    if crumbs:
        return accessible_section_label(crumbs[0])
    guide = str(page.get("guide", "user-en"))
    return {
        "installation": "Installation",
        "sysadmin": "System administration",
    }.get(guide, "Getting started and community")


def grouped_pages(
    pages: List[Dict[str, Any]],
) -> List[Tuple[str, List[Dict[str, Any]]]]:
    """Deduplicate and group browse-page entries by functional area."""
    buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    seen_paths: set[str] = set()
    for page in pages:
        path = str(page.get("destination_path", "")).casefold()
        if not path or path in seen_paths:
            continue
        seen_paths.add(path)
        buckets[group_label(page)].append(page)
    return [
        (
            label,
            sorted(
                values,
                key=lambda item: (
                    STAGE_ORDER.get(str(item.get("journey_stage", "")), 99),
                    str(item.get("subtopic", "")).casefold(),
                    str(item.get("title", "")).casefold(),
                ),
            ),
        )
        for label, values in sorted(
            buckets.items(),
            key=lambda item: item[0].casefold(),
        )
    ]


def build_audience_navigation(
    docs_root: Path,
    inventory: List[Dict[str, Any]],
) -> List[Any]:
    """Generate non-empty audience indexes and return their MkDocs nav entries."""
    labels = effective_audience_labels()
    pages_by_audience: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    for page in inventory:
        for audience in page_audiences(page):
            if audience in labels:
                pages_by_audience[audience].append(page)

    audience_nav: List[Any] = []
    for audience, label in labels.items():
        pages = pages_by_audience.get(audience, [])
        if not pages:
            continue
        relative = f"{BROWSE_DIR}/audiences/{audience}.md"
        write_generated_index(
            docs_root,
            relative,
            label,
            AUDIENCE_INTROS.get(
                audience,
                "Browse documentation for this audience by functional area and component.",
            ),
            grouped_pages(pages),
        )
        audience_nav.append({label: relative})

    return audience_nav


def generate_browse_indexes(
    docs_root: Path,
    inventory: List[Dict[str, Any]],
) -> Tuple[List[Any], List[Any]]:
    """Build category and audience landing pages with topic, level and dates."""
    install_index_page_css(
        docs_root,
    )
    browse_root = docs_root / BROWSE_DIR
    safe_rmtree(browse_root)
    browse_root.mkdir(parents=True, exist_ok=True)

    category_nav: List[Any] = []
    for category, label in CATEGORY_LABELS.items():
        pages = [page for page in inventory if page.get("category") == category]
        relative = f"{BROWSE_DIR}/categories/{category}.md"
        write_generated_index(
            docs_root,
            relative,
            label,
            "Browse this Diátaxis content type by functional area and component.",
            grouped_pages(pages),
        )
        category_nav.append({label: relative})

    audience_nav = build_audience_navigation(docs_root, inventory)
    return category_nav, audience_nav


def navigation_markdown_lines(nav: Any, depth: int = 0) -> List[str]:
    """Render a resolved MkDocs navigation tree as readable Markdown."""
    lines: List[str] = []
    indent = "  " * depth
    if isinstance(nav, list):
        for item in nav:
            lines.extend(navigation_markdown_lines(item, depth))
    elif isinstance(nav, dict):
        for title, value in nav.items():
            if isinstance(value, str):
                lines.append(f"{indent}- **{title}** — `{value}`")
            elif isinstance(value, list):
                lines.append(f"{indent}- **{title}**")
                lines.extend(navigation_markdown_lines(value, depth + 1))
    return lines


def export_navigation_plan(paths: "Paths", config: Dict[str, Any]) -> None:
    """Export the resolved navigation to human-readable YAML and Markdown."""
    paths.reports.mkdir(parents=True, exist_ok=True)
    navigation = config.get("nav", [])
    navigation_manifest = load_json(paths.state / "navigation-manifest.json")
    navigation_source = str(navigation_manifest.get("source", "unknown"))
    yaml_payload = {
        "navigation_source": navigation_source,
        "nav": navigation,
    }
    yaml_path = paths.reports / "navigation-plan.yaml"
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
    markdown_lines.extend(navigation_markdown_lines(navigation))
    markdown_path = paths.reports / "navigation-plan.md"
    markdown_path.write_text(
        "\n".join(markdown_lines).rstrip() + "\n",
        encoding="utf-8",
    )
    print("Navigation previews written to:")
    print(f"  {markdown_path}")
    print(f"  {yaml_path}")


def validate_nav_files(config: Dict[str, Any], docs_root: Path) -> None:
    paths = collect_nav_paths(config.get("nav", []))
    missing = sorted({path for path in paths if not (docs_root / Path(path)).exists()})
    duplicates = sorted(path for path, count in Counter(paths).items() if count > 1)
    messages: List[str] = []
    if missing:
        messages.append("missing files: " + ", ".join(missing))
    if duplicates:
        messages.append("duplicate navigation paths: " + ", ".join(duplicates))
    if messages:
        raise RuntimeError("Navigation validation failed: " + "; ".join(messages))
