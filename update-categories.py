#!/usr/bin/env python3
"""Corrige le rendu des pages « Browse by content category » de CiviDoc."""

from __future__ import annotations

import argparse
import ast
import py_compile
import shutil
import sys
from pathlib import Path
from typing import Dict

GENERATE_DIATAXIS_INDEXES = '''def generate_diataxis_indexes(docs_root: Path) -> None:
    """Génère les quatre index Diátaxis avec des cartes Markdown valides."""
    output_dir = docs_root / DIATAXIS_INDEX_DIR

    if output_dir.exists():
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    pages_by_type: Dict[str, List[Dict[str, str]]] = {
        category: []
        for category in DIATAXIS_TYPES
    }

    for page in iter_markdown(docs_root):
        relative = page.relative_to(docs_root)

        if relative.parts and relative.parts[0] == DIATAXIS_INDEX_DIR:
            continue

        metadata, body = split_front_matter(
            page.read_text(encoding="utf-8-sig")
        )

        categories = metadata.get("categories", [])
        if isinstance(categories, str):
            categories = [categories]

        if not isinstance(categories, list) or len(categories) != 1:
            continue

        category = str(categories[0]).strip().lower()
        if category not in pages_by_type:
            continue

        fallback_title = (
            page.stem
            .replace("-", " ")
            .replace("_", " ")
            .strip()
            .capitalize()
        )

        pages_by_type[category].append({
            "title": markdown_title(body, fallback_title),
            "summary": str(metadata.get("summary", "")).strip(),
            "section": str(metadata.get("section", "")).strip(),
            "level": str(metadata.get("level", "")).strip(),
            "path": relative.as_posix(),
        })

    for category, pages in pages_by_type.items():
        pages.sort(
            key=lambda item: (
                item["section"].casefold(),
                item["title"].casefold(),
                item["path"].casefold(),
            )
        )

        info = DIATAXIS_TYPES[category]
        slug = info["slug"]
        lines = [
            "---",
            f"title: {info['label']}",
            "generated_diataxis_index: true",
            "hide:",
            "  - toc",
            "---",
            "",
            f"# {info['label']}",
            "",
            info["description"],
            "",
        ]

        if pages:
            lines.extend([
                f"{len(pages)} page(s) in this category.",
                "",
                "## Pages",
                "",
                '<div class="cividoc-category-list" markdown="1">',
                "",
            ])

            for page in pages:
                title = escape_markdown_label(page["title"])
                target = f"../{page['path']}"
                metadata_parts = [
                    value
                    for value in (page["section"], page["level"])
                    if value
                ]

                lines.append(f"- [**{title}**]({target})")

                if metadata_parts:
                    metadata_text = escape(" · ".join(metadata_parts))
                    lines.append(
                        '  <span class="cividoc-category-meta">'
                        f"{metadata_text}</span>"
                    )

                if page["summary"]:
                    lines.append(
                        '  <span class="cividoc-category-summary">'
                        f"{escape(page['summary'])}</span>"
                    )

            lines.extend(["", "</div>", ""])
        else:
            lines.append(info["empty"])

        (output_dir / f"{slug}.md").write_text(
            "\\n".join(lines).rstrip() + "\\n",
            encoding="utf-8",
        )

    overview_lines = [
        "---",
        "title: Browse by content category",
        "generated_diataxis_index: true",
        "hide:",
        "  - toc",
        "---",
        "",
        "# Browse by content category",
        "",
        "Choose the kind of documentation that matches your current need.",
        "",
        '<div class="cividoc-category-cards" markdown="1">',
        "",
    ]

    for info in DIATAXIS_TYPES.values():
        overview_lines.extend([
            f"- [**{info['label']}**]({info['slug']}.md)",
            f"  {info['description']}",
        ])

    overview_lines.extend(["", "</div>", ""])

    (output_dir / "index.md").write_text(
        "\\n".join(overview_lines).rstrip() + "\\n",
        encoding="utf-8",
    )

    counts = ", ".join(
        f"{DIATAXIS_TYPES[category]['label']}: {len(pages)}"
        for category, pages in pages_by_type.items()
    )
    print(f"✅ Pages de catégories générées — {counts}")
'''

INSTALL_CATEGORY_HOMEPAGE = '''def install_category_homepage(docs_root: Path) -> None:
    """Ajoute à l’accueil un bloc de catégories sans attribut visible."""
    homepage = docs_root / "index.md"

    if not homepage.exists():
        print("⚠️ Impossible d'ajouter les catégories : docs/index.md est absent.")
        return

    text = homepage.read_text(encoding="utf-8-sig")
    start_marker = "<!-- CiviDoc category browser:start -->"
    end_marker = "<!-- CiviDoc category browser:end -->"

    text = re.sub(
        re.escape(start_marker) + r"[\\s\\S]*?" + re.escape(end_marker) + r"\\s*",
        "",
        text,
    )
    text = re.sub(
        r"(?ms)^## Browse by content category\\s*$.*?(?=^##\\s|\\Z)",
        "",
        text,
    )

    lines = [
        start_marker,
        "## Browse by content category",
        "",
        "To match your learning needs, browse the documentation by content category:",
        "",
        '<div class="cividoc-category-cards" markdown="1">',
        "",
    ]

    for info in DIATAXIS_TYPES.values():
        lines.extend([
            f"- [**{info['label']}**]({DIATAXIS_INDEX_DIR}/{info['slug']}.md)",
            f"  {info['description']}",
        ])

    lines.extend(["", "</div>", end_marker, ""])
    block = "\\n".join(lines)
    first_h2 = re.search(r"(?m)^##\\s+", text)

    if first_h2:
        position = first_h2.start()
        text = (
            text[:position].rstrip()
            + "\\n\\n"
            + block
            + "\\n"
            + text[position:].lstrip()
        )
    else:
        source_comment = re.search(r"(?im)^<!--\\s*Source:.*?-->\\s*$", text)
        if source_comment:
            position = source_comment.start()
            text = (
                text[:position].rstrip()
                + "\\n\\n"
                + block
                + "\\n"
                + text[position:]
            )
        else:
            text = text.rstrip() + "\\n\\n" + block

    homepage.write_text(text.rstrip() + "\\n", encoding="utf-8")
    print("✅ Sélecteur de catégories ajouté à la page d'accueil")
'''

CONFIGURE_CATEGORY_PRESENTATION = '''def configure_category_presentation(
    site: Path,
    config: Dict[str, Any],
) -> None:
    """Installe le style des cartes et les extensions Markdown nécessaires."""
    css_dir = site / "docs" / "css"
    css_dir.mkdir(parents=True, exist_ok=True)

    css = r"""
.cividoc-category-cards > ul,
.cividoc-category-list > ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
  padding: 0;
  list-style: none;
}

.cividoc-category-cards > ul > li,
.cividoc-category-list > ul > li {
  margin: 0 !important;
  padding: 1.1rem 1.2rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 0.65rem;
  background: var(--md-default-bg-color);
  box-shadow: 0 0.15rem 0.45rem rgb(0 0 0 / 7%);
  transition: transform 160ms ease, border-color 160ms ease,
    box-shadow 160ms ease;
}

.cividoc-category-cards > ul > li:hover,
.cividoc-category-list > ul > li:hover {
  transform: translateY(-0.15rem);
  border-color: var(--md-primary-fg-color);
  box-shadow: 0 0.45rem 1rem rgb(0 0 0 / 11%);
}

.cividoc-category-cards > ul > li > p,
.cividoc-category-list > ul > li > p {
  margin: 0;
}

.cividoc-category-cards a,
.cividoc-category-list a {
  display: block;
  margin-bottom: 0.4rem;
  color: var(--md-primary-fg-color);
  font-size: 1.05rem;
}

.cividoc-category-meta {
  display: block;
  margin-bottom: 0.45rem;
  color: var(--md-default-fg-color--light);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.035em;
  text-transform: uppercase;
}

.cividoc-category-summary {
  display: block;
  color: var(--md-default-fg-color--light);
  line-height: 1.5;
}

@media (max-width: 40rem) {
  .cividoc-category-cards > ul,
  .cividoc-category-list > ul {
    grid-template-columns: 1fr;
  }
}
""".strip()

    (css_dir / "categories.css").write_text(css + "\\n", encoding="utf-8")

    extra_css = config.setdefault("extra_css", [])
    if not isinstance(extra_css, list):
        extra_css = []
        config["extra_css"] = extra_css
    if "css/categories.css" not in extra_css:
        extra_css.append("css/categories.css")

    extensions = config.setdefault("markdown_extensions", [])
    if not isinstance(extensions, list):
        extensions = []
        config["markdown_extensions"] = extensions

    extension_names = set()
    for extension in extensions:
        if isinstance(extension, str):
            extension_names.add(extension)
        elif isinstance(extension, dict):
            extension_names.update(extension.keys())

    if (
        "attr_list" not in extension_names
        and "markdown.extensions.attr_list" not in extension_names
    ):
        extensions.append("attr_list")

    if (
        "md_in_html" not in extension_names
        and "markdown.extensions.md_in_html" not in extension_names
    ):
        extensions.append("md_in_html")
'''

REPLACEMENTS: Dict[str, str] = {
    "generate_diataxis_indexes": GENERATE_DIATAXIS_INDEXES,
    "install_category_homepage": INSTALL_CATEGORY_HOMEPAGE,
    "configure_category_presentation": CONFIGURE_CATEGORY_PRESENTATION,
}


def function_ranges(source: str) -> Dict[str, tuple[int, int]]:
    tree = ast.parse(source)
    ranges: Dict[str, tuple[int, int]] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in REPLACEMENTS:
                ranges[node.name] = (node.lineno - 1, node.end_lineno or node.lineno)
    return ranges


def patch_source(source: str) -> str:
    ranges = function_ranges(source)
    missing = sorted(set(REPLACEMENTS) - set(ranges))
    if missing:
        raise RuntimeError(
            "Fonction(s) introuvable(s) dans le script cible : " + ", ".join(missing)
        )

    lines = source.splitlines(keepends=True)
    operations = sorted(
        (
            (start, end, REPLACEMENTS[name].rstrip() + "\n\n")
            for name, (start, end) in ranges.items()
        ),
        reverse=True,
    )
    for start, end, replacement in operations:
        lines[start:end] = [replacement]

    result = "".join(lines)
    result = result.replace("{: .cividoc-category-list }", "")
    result = result.replace("{: .cividoc-category-cards }", "")
    ast.parse(result)
    return result


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Met à jour cividoc.py pour corriger l'affichage des attributs "
            "de listes dans les pages Browse by content category."
        )
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="cividoc.py",
        help="script CiviDoc à mettre à jour (défaut : cividoc.py)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--in-place",
        action="store_true",
        help="remplace le script cible et crée une sauvegarde .bak",
    )
    mode.add_argument(
        "--output",
        help="chemin du nouveau script (défaut : cividoc-categories-fixed.py)",
    )
    return parser.parse_args()


def main() -> int:
    args = arguments()
    target = Path(args.target).resolve()
    if not target.is_file():
        print(f"❌ Script introuvable : {target}", file=sys.stderr)
        return 2

    try:
        source = target.read_text(encoding="utf-8-sig")
        patched = patch_source(source)

        if args.in_place:
            destination = target
            backup = target.with_suffix(target.suffix + ".categories.bak")
            shutil.copy2(target, backup)
            print(f"💾 Sauvegarde : {backup}")
        else:
            destination = (
                Path(args.output).resolve()
                if args.output
                else target.with_name("cividoc-categories-fixed.py")
            )

        destination.write_text(patched, encoding="utf-8", newline="\n")
        py_compile.compile(str(destination), doraise=True)
    except Exception as exc:
        print(f"❌ Mise à jour impossible : {exc}", file=sys.stderr)
        return 1

    print(f"✅ Script corrigé : {destination}")
    print("   Relancez ensuite : python .\\cividoc.py run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
