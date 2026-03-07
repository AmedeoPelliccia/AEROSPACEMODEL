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
cgen_indexes.py — Index Generator
==================================
Walks a target directory, finds all `.meta.yaml` files, and regenerates the
`00_INDEX.md` file with a sorted markdown table.

Usage:
    python scripts/cgen_indexes.py \\
        --output-dir OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_03-SUPPORT_INFRA \\
        --timestamp 2026-03-07T03:00:00Z
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

log = logging.getLogger("cgen_indexes")


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


def _collect_meta_files(directory: Path) -> list:
    """Collect all .meta.yaml files recursively, sorted by path."""
    meta_files = sorted(directory.rglob("*.meta.yaml"))
    log.debug("Found %d .meta.yaml files in %s", len(meta_files), directory)
    return meta_files


def _extract_meta_info(meta_file: Path) -> dict:
    """Load meta.yaml and extract display information."""
    try:
        with meta_file.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if not data:
            return {"file": meta_file.name, "title": meta_file.stem, "status": "UNKNOWN", "lc_phase": "-", "ata": "-"}
        return {
            "file": meta_file.name,
            "title": data.get("artifact_title", data.get("record_id", meta_file.stem)),
            "status": data.get("status", "UNKNOWN"),
            "lc_phase": data.get("lc_phase", "-"),
            "ata": f"ATA {data.get('ata_chapter', '??')}-{data.get('section', '??')}-{data.get('subject', '??')}",
            "record_id": data.get("record_id", ""),
        }
    except Exception as exc:  # noqa: BLE001
        log.warning("Could not read meta file %s: %s", meta_file, exc)
        return {"file": meta_file.name, "title": meta_file.stem, "status": "ERROR", "lc_phase": "-", "ata": "-"}


def _generate_index(directory: Path, meta_files: list, timestamp: str) -> str:
    """Generate 00_INDEX.md content for the given directory."""
    dir_name = directory.name
    total = len(meta_files)

    lines = [
        f"# 00 — Index: {dir_name}",
        "",
        f"> Generated: `{timestamp}`  ",
        f"> File count: `{total}` metadata records",
        "",
    ]

    if not meta_files:
        lines += [
            "_No metadata records found in this directory._",
            "",
        ]
    else:
        lines += [
            "## Metadata Records",
            "",
            "| # | File | ATA | Title | LC Phase | Status |",
            "| - | ---- | --- | ----- | -------- | ------ |",
        ]
        for i, meta_file in enumerate(meta_files, 1):
            info = _extract_meta_info(meta_file)
            rel = meta_file.relative_to(directory)
            lines.append(
                f"| {i} | [{rel}]({rel}) "
                f"| {info.get('ata', '-')} "
                f"| {info.get('title', '-')} "
                f"| {info.get('lc_phase', '-')} "
                f"| {info.get('status', '-')} |"
            )
        lines.append("")

    # List other files
    other_md = sorted(
        f for f in directory.iterdir()
        if f.is_file() and f.suffix == ".md" and f.name not in ("00_INDEX.md",)
    )
    if other_md:
        lines += [
            "## Documentation",
            "",
            "| File | Description |",
            "| ---- | ----------- |",
        ]
        for md_file in other_md:
            lines.append(f"| [{md_file.name}]({md_file.name}) | — |")
        lines.append("")

    lines += [
        "---",
        f"_Index generated by `cgen_indexes.py` v{CGEN_VERSION} at `{timestamp}`_",
        "",
    ]
    return "\n".join(lines)


def run(output_dir: Path, timestamp: str, dry_run: bool) -> list:
    """Run index generation for the given directory."""
    log.info("=== CGen Indexes v%s ===", CGEN_VERSION)
    log.info("Output dir : %s", output_dir)
    log.info("Timestamp  : %s", timestamp)

    if not output_dir.exists():
        log.warning("Output directory does not exist: %s — creating", output_dir)
        if not dry_run:
            output_dir.mkdir(parents=True, exist_ok=True)

    meta_files = _collect_meta_files(output_dir)
    content = _generate_index(output_dir, meta_files, timestamp)

    dest = output_dir / "00_INDEX.md"
    action = _write_file(dest, content, dry_run)

    entry = {
        "path": str(dest.relative_to(REPO_ROOT)),
        "sha256": _sha256(content),
        "action": action,
        "size_bytes": len(content.encode("utf-8")),
        "generator": "cgen_indexes.py",
    }

    log.info("Index generation complete: %s (%s)", dest.name, action)
    return [entry]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate 00_INDEX.md for a target directory.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Target directory to index",
    )
    parser.add_argument(
        "--timestamp",
        type=str,
        required=True,
        help="ISO 8601 UTC generation timestamp",
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
