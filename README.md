# CiviCRM documentation pipeline

This project builds one source-faithful documentation site from the official CiviCRM user, installation, and system-administrator repositories.

## What changed

The global navigation is task- and feature-oriented. It has no generic **User Guide** wrapper. Functional topics use a consistent reader journey where the source pages support it:

1. Overview
2. Plan and configure
3. Everyday tasks
4. Manage and automate
5. Reports and review
6. Reference and troubleshooting
7. Extensions and integrations

The pipeline does not force every group into every topic. It limits direct choices and adds semantic subgroups when a branch becomes too large. A `What is CiviX?` page is kept first as the component entry page, with its existing title and physical URL.

The navigation planner now sends immutable `page_id` values to the AI instead of writable paths. The AI can choose conceptual placement, but it cannot rename or move a file. The script resolves each validated ID to the exact existing `destination_path`. An invalid AI proposal is rejected and replaced by deterministic navigation, so it cannot stop the build or corrupt the cache.

The front matter includes category, topic, subtopic, component, audiences, level, journey stage, summary, extensions, related pages, review priority, review notes, and source provenance. Diátaxis categories and audiences are generated as secondary **Browse** views rather than competing primary taxonomies.

## Requirements

Use Python 3.10 or later, Git, and MkDocs Material. Install the Python dependencies in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install mkdocs-material pyyaml python-dotenv requests
```

For Perplexity, define `PERPLEXITY_API_KEY`. For OpenAI, define `OPENAI_API_KEY`. AI is optional.

## First run

Synchronise the three official repositories:

```powershell
python cividoc.py sync
```

Prepare the merged documentation without AI and without an HTML build:

```powershell
python cividoc.py prepare --refresh-nav --skip-build
```

Build the complete site:

```powershell
python cividoc.py run
```

Serve the generated site:

```powershell
python cividoc.py serve --address 127.0.0.1:8000
```

## AI rewriting

Test a single source page first:

```powershell
python cividoc.py run `
  --ai `
  --include "user-en:events/what-is-civievent.md" `
  --limit 1 `
  --skip-build
```

Enable AI navigation separately:

```powershell
python cividoc.py run --ai-nav --refresh-nav --skip-build
```

`--ai` no longer enables AI navigation implicitly. This separation is intentional.

## Navigation cache

The only navigation cache is:

```text
.cividoc/state/navigation-manifest.json
```

It stores a structural plan made of immutable page IDs, plus a separate ID-to-path map. The plan itself contains no Markdown paths. To regenerate it:

```powershell
Remove-Item ".cividoc\state\navigation-manifest.json" -Force -ErrorAction SilentlyContinue
python cividoc.py prepare --ai-nav --refresh-nav --skip-build
```

Do not delete `rewrite-manifest.json` unless you intentionally want to discard rewrite state.

## Source-fidelity policy

The source page is the only authority on CiviCRM behaviour. The rewrite prompt forbids adding steps, options, or facts; omitting steps, options, or warnings; and changing menu paths, field names, or button labels. Unclear, contradictory, or apparently obsolete content must be preserved and recorded in `review_notes`, not silently corrected.

`review_priority` is calculated and validated from those notes:

- `high`: the reader could be misled or unable to complete a task;
- `medium`: the page remains usable but shows age, ambiguity, or gaps;
- `low`: notes are empty or minor.

The script also verifies preservation of links, images, code fences, anchors, menu paths, quoted UI labels, and technical literals before accepting an AI rewrite.

## Output

The merged MkDocs project is written to `generated-civicrm-docs`. Audit files are written to `generated-civicrm-docs/reports`.

Useful commands:

```powershell
python cividoc.py --help
python cividoc.py --list-guides
python cividoc.py prepare --skip-build
python cividoc.py run --no-strict
python cividoc.py serve
```

On Windows, stop any active MkDocs server before using `--fresh`; an open process can lock the generated site directory.
