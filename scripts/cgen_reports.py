# Copyright 2024 Amedeo Pelliccia / AEROSPACEMODEL Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
cgen_reports.py — CGen Generation Report Generator
====================================================
Collects statistics from a completed CGen run (or from a manifest JSON) and
generates human-readable and machine-readable reports under cd/reports/.

Outputs:
  - cd/reports/cgen_report_{date}.md    — Human-readable markdown summary
  - cd/reports/cgen_summary.yaml        — Machine-readable YAML summary

Usage:
    python scripts/cgen_reports.py \\
        --output-dir cd/reports \\
        --timestamp 2026-03-07T03:00:00Z \\
        --manifest cd/reports/cgen_manifest.json
"""

import argparse
import hashlib
import json
import logging
import sys
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
CGEN_VERSION = "1.0.0"

log = logging.getLogger("cgen_reports")

# ATA 03 categories for summary
ATA03_SECTIONS = [
    "00 — General",
    "10 — Towing Equipment",
    "20 — Servicing Equipment",
    "30 — Docking and Maintenance Stands",
    "40 — Tooling",
    "50 — Test Equipment",
    "60 — Safety Equipment",
    "70 — H2-Specific GSE",
]

H2GSE_SECTIONS = [
    "10 — H2 Refueling Systems",
    "20 — Cryogenic Storage",
    "30 — Boil-Off Recovery",
    "40 — Leak Detection",
    "50 — Emergency Systems",
    "60 — Supply Chain",
]

INFRA_LC_PHASES = ["LC04", "LC06", "LC10", "LC11", "LC12"]


def _setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )


def _sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _write_file(path: Path, content: str, dry_run: bool) -> str:
    if dry_run:
        log.info("[DRY RUN] Would write: %s", path)
        return "skipped"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return "unchanged"
        path.write_text(content, encoding="utf-8")
        log.info("Updated: %s", path)
        return "updated"
    path.write_text(content, encoding="utf-8")
    log.info("Created: %s", path)
    return "created"


def _load_manifest(manifest_path: Path) -> dict:
    """Load a cgen_manifest.json file."""
    if not manifest_path.exists():
        log.warning("Manifest not found: %s — using empty stats", manifest_path)
        return {}
    with manifest_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _collect_stats_from_manifest(manifest: dict) -> dict:
    """Extract statistics from a manifest dict."""
    files = manifest.get("files", [])
    summary = manifest.get("summary", {})

    stats = {
        "total_files": summary.get("total_files", len(files)),
        "files_created": summary.get("files_created", sum(1 for f in files if f.get("action") == "created")),
        "files_updated": summary.get("files_updated", sum(1 for f in files if f.get("action") == "updated")),
        "files_unchanged": summary.get("files_unchanged", sum(1 for f in files if f.get("action") == "unchanged")),
        "files_skipped": sum(1 for f in files if f.get("action") == "skipped"),
        "generators": {},
        "targets": summary.get("targets", []),
    }

    for f in files:
        gen = f.get("generator", "unknown")
        stats["generators"].setdefault(gen, 0)
        stats["generators"][gen] += 1

    return stats


def _generate_markdown_report(stats: dict, timestamp: str, run_mode: str, dry_run: bool) -> str:
    """Generate a human-readable markdown report."""
    date_str = timestamp[:10] if len(timestamp) >= 10 else timestamp

    lines = [
        "# CGen Generation Report",
        "",
        f"| Field | Value |",
        f"| ----- | ----- |",
        f"| **Generated At** | `{timestamp}` |",
        f"| **CGen Version** | `{CGEN_VERSION}` |",
        f"| **Run Mode** | `{run_mode}` |",
        f"| **Dry Run** | `{dry_run}` |",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"| ------ | ----- |",
        f"| Total files processed | {stats['total_files']} |",
        f"| Files created | {stats['files_created']} |",
        f"| Files updated | {stats['files_updated']} |",
        f"| Files unchanged (idempotent) | {stats['files_unchanged']} |",
        f"| Files skipped (dry-run) | {stats['files_skipped']} |",
        "",
        "## Targets",
        "",
    ]

    if stats.get("targets"):
        for target in stats["targets"]:
            lines.append(f"- `{target}`")
    else:
        lines.append("_No target information available._")

    lines += [
        "",
        "## Generators",
        "",
        "| Generator | Files |",
        "| --------- | ----- |",
    ]
    for gen, count in sorted(stats["generators"].items()):
        lines.append(f"| `{gen}` | {count} |")

    lines += [
        "",
        "## ATA 03 Coverage",
        "",
        "Sections covered by this generation run:",
        "",
    ]
    for section in ATA03_SECTIONS:
        lines.append(f"- ATA 03-{section}")

    lines += [
        "",
        "## H2 GSE Coverage",
        "",
        "H2 GSE stub sections generated:",
        "",
    ]
    for section in H2GSE_SECTIONS:
        lines.append(f"- ATA IN-{section}")

    lines += [
        "",
        "## Lifecycle Phase Coverage",
        "",
        "Infrastructure lifecycle phases referenced:",
        "",
        "| Phase | Name |",
        "| ----- | ---- |",
        "| LC04  | Design Definition |",
        "| LC06  | Integration & Test |",
        "| LC10  | Industrial & Supply Chain |",
        "| LC11  | Operations Customization |",
        "| LC12  | Continued Airworthiness & MRO |",
        "",
        "---",
        f"_Report generated by `cgen_reports.py` v{CGEN_VERSION} at `{timestamp}`_",
        "",
    ]
    return "\n".join(lines)


def _generate_yaml_summary(stats: dict, timestamp: str, run_mode: str, dry_run: bool) -> str:
    """Generate a machine-readable YAML summary."""
    summary = {
        "meta": {
            "generated_at": timestamp,
            "cgen_version": CGEN_VERSION,
            "run_mode": run_mode,
            "dry_run": dry_run,
        },
        "stats": {
            "total_files": stats["total_files"],
            "files_created": stats["files_created"],
            "files_updated": stats["files_updated"],
            "files_unchanged": stats["files_unchanged"],
            "files_skipped": stats["files_skipped"],
            "generators": stats["generators"],
        },
        "targets": stats.get("targets", []),
        "coverage": {
            "ata03_sections": ATA03_SECTIONS,
            "h2gse_sections": H2GSE_SECTIONS,
            "lc_phases": INFRA_LC_PHASES,
        },
    }
    return yaml.dump(summary, default_flow_style=False, allow_unicode=True, sort_keys=False)


def run(output_dir: Path, timestamp: str, dry_run: bool, run_mode: str, manifest_path: Path | None) -> list:
    """Run report generation."""
    log.info("=== CGen Reports v%s ===", CGEN_VERSION)
    log.info("Output dir : %s", output_dir)
    log.info("Timestamp  : %s", timestamp)

    manifest = _load_manifest(manifest_path) if manifest_path else {}
    stats = _collect_stats_from_manifest(manifest)

    date_str = timestamp[:10].replace("-", "")
    if len(date_str) != 8 or not date_str.isdigit():
        raise ValueError(f"Invalid timestamp format: {timestamp!r} — expected ISO 8601, e.g. 2026-03-07T03:00:00Z")
    manifest_entries = []

    # Markdown report
    md_content = _generate_markdown_report(stats, timestamp, run_mode, dry_run)
    md_dest = output_dir / f"cgen_report_{date_str}.md"
    action = _write_file(md_dest, md_content, dry_run)
    manifest_entries.append({
        "path": str(md_dest.relative_to(REPO_ROOT)),
        "sha256": _sha256(md_content),
        "action": action,
        "size_bytes": len(md_content.encode("utf-8")),
        "generator": "cgen_reports.py",
    })

    # YAML summary
    yaml_content = _generate_yaml_summary(stats, timestamp, run_mode, dry_run)
    yaml_dest = output_dir / "cgen_summary.yaml"
    action = _write_file(yaml_dest, yaml_content, dry_run)
    manifest_entries.append({
        "path": str(yaml_dest.relative_to(REPO_ROOT)),
        "sha256": _sha256(yaml_content),
        "action": action,
        "size_bytes": len(yaml_content.encode("utf-8")),
        "generator": "cgen_reports.py",
    })

    log.info("Report generation complete: %d files", len(manifest_entries))
    return manifest_entries


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate CGen run summary reports.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "cd" / "reports",
        help="Directory to write reports into (default: cd/reports/)",
    )
    parser.add_argument(
        "--timestamp",
        type=str,
        required=True,
        help="ISO 8601 UTC generation timestamp",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="Path to cgen_manifest.json to read stats from",
    )
    parser.add_argument(
        "--run-mode",
        type=str,
        default="full",
        choices=["full", "docs-only", "indexes-only"],
        help="CGen run mode for report header",
    )
    parser.add_argument(
        "--manifest-out",
        type=Path,
        default=None,
        help="Optional path to write per-script manifest JSON",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    _setup_logging(args.verbose)

    entries = run(
        output_dir=args.output_dir.resolve(),
        timestamp=args.timestamp,
        dry_run=args.dry_run,
        run_mode=args.run_mode,
        manifest_path=args.manifest.resolve() if args.manifest else None,
    )

    if args.manifest_out:
        args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
        args.manifest_out.write_text(
            json.dumps({"files": entries}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
