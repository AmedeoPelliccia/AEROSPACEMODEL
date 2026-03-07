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
cgen_ata03.py — ATA 03 Ground Support Equipment and Tooling Infrastructure Generator
=====================================================================================
Generates YAML metadata template files and documentation for ATA 03 GSE content
under OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_03-SUPPORT_INFRA.

Usage:
    python scripts/cgen_ata03.py \\
        --output-dir OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_03-SUPPORT_INFRA \\
        --timestamp 2026-03-07T03:00:00Z

The script is idempotent: given the same --timestamp, it always produces the same output.
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
LIFECYCLE_REGISTRY = REPO_ROOT / "lifecycle" / "LC_PHASE_REGISTRY.yaml"
ARTIFACT_TYPES_FILE = REPO_ROOT / "schemas" / "ampel360_artifact_types.yaml"
BREX_FILE = REPO_ROOT / "ASIGT" / "brex" / "S1000D_5.0_DEFAULT.yaml"
TEMPLATE_FILE = REPO_ROOT / "templates" / "cgen" / "ata03_meta.yaml.j2"

CGEN_VERSION = "1.0.0"
AIRCRAFT_ID = "AMPEL360"
MODEL_ID = "Q100"
MSN = "MSN001"

# Infrastructure-relevant lifecycle phases for ATA 03
INFRA_LC_PHASES = ["LC04", "LC06", "LC10", "LC11", "LC12"]

# ATA 03 GSE categories to generate
ATA03_CATEGORIES = [
    {
        "filename": "ATA_03-00-00_GSE_GENERAL.meta.yaml",
        "ata_section": "00",
        "ata_subject": "00",
        "section_title": "General",
        "subject_title": "General",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03 Ground Support Equipment — General Overview",
        "lc_phase": "LC04",
        "novel_technology": False,
        "notes": "General GSE overview covering all ATA 03 subcategories.",
        "cross_refs": [],
    },
    {
        "filename": "ATA_03-10-00_TOWING_EQUIPMENT.meta.yaml",
        "ata_section": "10",
        "ata_subject": "00",
        "section_title": "Towing Equipment",
        "subject_title": "Towing and Taxiing Equipment",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-10 Towing and Taxiing Equipment",
        "lc_phase": "LC04",
        "novel_technology": False,
        "notes": "Equipment for towing and taxiing the AMPEL360 Q100 aircraft.",
        "cross_refs": ["ATA_12-SERVICING_INFRA"],
    },
    {
        "filename": "ATA_03-20-00_SERVICING_EQUIPMENT.meta.yaml",
        "ata_section": "20",
        "ata_subject": "00",
        "section_title": "Servicing Equipment",
        "subject_title": "Servicing and Cleaning Equipment",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-20 Servicing and Cleaning Equipment",
        "lc_phase": "LC04",
        "novel_technology": False,
        "notes": "Ground servicing and cleaning equipment for routine operations.",
        "cross_refs": ["ATA_12-SERVICING_INFRA"],
    },
    {
        "filename": "ATA_03-30-00_DOCKING_MAINTENANCE_STANDS.meta.yaml",
        "ata_section": "30",
        "ata_subject": "00",
        "section_title": "Docking and Maintenance Stands",
        "subject_title": "Docking and Maintenance Access Stands",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-30 Docking and Maintenance Access Stands",
        "lc_phase": "LC04",
        "novel_technology": False,
        "notes": "Aircraft docking platforms and maintenance access stands.",
        "cross_refs": [],
    },
    {
        "filename": "ATA_03-40-00_TOOLING.meta.yaml",
        "ata_section": "40",
        "ata_subject": "00",
        "section_title": "Tooling",
        "subject_title": "Specialized Tooling",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-40 Specialized Tooling",
        "lc_phase": "LC04",
        "novel_technology": False,
        "notes": "Specialized tooling requirements for Q100 maintenance and assembly.",
        "cross_refs": [],
    },
    {
        "filename": "ATA_03-50-00_TEST_EQUIPMENT.meta.yaml",
        "ata_section": "50",
        "ata_subject": "00",
        "section_title": "Test Equipment",
        "subject_title": "Test and Calibration Equipment",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-50 Test and Calibration Equipment",
        "lc_phase": "LC06",
        "novel_technology": False,
        "notes": "Test and calibration equipment required for system verification.",
        "cross_refs": [],
    },
    {
        "filename": "ATA_03-60-00_SAFETY_EQUIPMENT.meta.yaml",
        "ata_section": "60",
        "ata_subject": "00",
        "section_title": "Safety Equipment",
        "subject_title": "Safety and Protective Equipment",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-60 Safety and Protective Equipment",
        "lc_phase": "LC10",
        "novel_technology": False,
        "notes": "Personal protective equipment and safety systems for ground operations.",
        "cross_refs": [],
    },
    {
        "filename": "ATA_03-70-00_H2_SPECIFIC_GSE.meta.yaml",
        "ata_section": "70",
        "ata_subject": "00",
        "section_title": "H2 Specific GSE",
        "subject_title": "Hydrogen-Specific Ground Support Equipment",
        "artifact_type": "DES",
        "artifact_type_name": "Design Document",
        "artifact_title": "ATA 03-70 Hydrogen-Specific Ground Support Equipment",
        "lc_phase": "LC04",
        "novel_technology": True,
        "notes": "Novel hydrogen-specific GSE. Links to ATA_IN_H2_GSE_AND_SUPPLY_CHAIN for extended scope.",
        "cross_refs": [
            "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN",
            "ATA_28-FUEL",
            "ATA_71-FUEL_CELL_SYSTEMS",
        ],
    },
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log = logging.getLogger("cgen_ata03")


def _setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )


def _load_yaml(path: Path) -> dict:
    """Load a YAML file safely; raise on error."""
    log.debug("Loading YAML: %s", path)
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if data is None:
        raise ValueError(f"Empty YAML file: {path}")
    return data


def _load_lifecycle_registry() -> dict:
    """Load and return the LC phase registry."""
    registry = _load_yaml(LIFECYCLE_REGISTRY)
    plm = registry.get("plm_phases", {})
    ops = registry.get("ops_phases", {})
    combined = {}
    combined.update(plm)
    combined.update(ops)
    return combined


def _load_brex_metadata() -> str:
    """Load BREX file and return the brex_id."""
    brex_data = _load_yaml(BREX_FILE)
    brex_id = brex_data.get("brex", {}).get("metadata", {}).get("brex_id", "BREX-S1000D-5.0-DEFAULT")
    return brex_id


def _load_artifact_types() -> dict:
    """Load artifact type registry; return dict mapping code → name."""
    data = _load_yaml(ARTIFACT_TYPES_FILE)
    types: dict = {}
    for _phase_key, entries in data.items():
        if _phase_key == "meta":
            continue
        if isinstance(entries, list):
            for entry in entries:
                if isinstance(entry, dict) and "code" in entry:
                    types[entry["code"]] = entry.get("name", entry["code"])
    return types


def _make_record_id(ata_section: str, ata_subject: str, lc_phase: str, artifact_type: str, seq: int = 1) -> str:
    """Build a canonical AMPEL360 record identifier.

    Pattern: AMPEL360_Q100_MSN{nnn}_ATA{cc}-{ss}-{ss}_LC{nn}_{TYPE}_{seq:03d}
    """
    return (
        f"AMPEL360_Q100_{MSN}_ATA03-{ata_section}-{ata_subject}"
        f"_{lc_phase}_{artifact_type}_{seq:03d}"
    )


def _render_template(template_path: Path, context: dict) -> str:
    """Render a Jinja2 template with the given context."""
    try:
        from jinja2 import Environment, FileSystemLoader, StrictUndefined

        env = Environment(
            loader=FileSystemLoader(str(template_path.parent)),
            undefined=StrictUndefined,
            keep_trailing_newline=True,
        )
        tmpl = env.get_template(template_path.name)
        return tmpl.render(**context)
    except ImportError:
        log.warning("Jinja2 not installed; using PyYAML direct render instead of template.")
        return None


def _build_meta_yaml_direct(context: dict) -> str:
    """Fallback: build meta.yaml content directly without Jinja2."""
    cross_refs_yaml = ""
    if context.get("cross_refs"):
        lines = "\n".join(f'  - "{r}"' for r in context["cross_refs"])
        cross_refs_yaml = f"cross_references:\n{lines}"
    else:
        cross_refs_yaml = "cross_references: []"

    notes_val = context.get("notes", "")

    return f"""\
# =============================================================================
# AMPEL360 Q100 — ATA 03 Metadata Record
# Generated by cgen_ata03.py v{CGEN_VERSION}
# =============================================================================
record_id: "{context['record_id']}"
aircraft_id: "AMPEL360"
model_id: "Q100"
msn: "{MSN}"

ata_chapter: "03"
ata_chapter_title: "Ground Support Equipment and Tooling"
section: "{context['ata_section']}"
section_title: "{context['section_title']}"
subject: "{context['ata_subject']}"
subject_title: "{context['subject_title']}"

optin_axis: "I"
optin_subaxis: "O"
optin_subaxis_name: "Operations & Service Structures"

novel_technology: {str(context['novel_technology']).lower()}

phase_type: "{context['lc_phase_type']}"
lc_phase: "{context['lc_phase']}"
lc_canonical_name: "{context['lc_canonical_name']}"
package_origin: "{context['package_origin']}"

lifecycle_applicability:
  - {{phase: "LC04", description: "Infrastructure design and specifications"}}
  - {{phase: "LC06", description: "Infrastructure testing and commissioning"}}
  - {{phase: "LC10", description: "Infrastructure production and deployment"}}
  - {{phase: "LC11", description: "Customer infrastructure integration"}}
  - {{phase: "LC12", description: "Infrastructure maintenance and upgrades"}}

artifact_type: "{context['artifact_type']}"
artifact_type_name: "{context['artifact_type_name']}"
artifact_title: "{context['artifact_title']}"

owner_aor: "ASIT/I-INFRASTRUCTURES/O-OPERATIONS"
status: "{context['status']}"
revision: "{context['revision']}"
prepared_by: "cgen_ata03.py"
date_created: "{context['cgen_timestamp']}"
date_modified: "{context['cgen_timestamp']}"
classification: "{context['classification']}"

ssot_root: "{context['ssot_root']}"
ssot_dir: "{context['ssot_dir']}"
ssot_filesystem_path: "{context['ssot_filesystem_path']}"

gate_id: "{context['gate_id']}"

brex_reference:
  brex_id: "{context['brex_id']}"
  standard: "S1000D Issue 5.0"
  validated: true

{cross_refs_yaml}

notes: "{notes_val}"

cgen:
  generated_by: "cgen_ata03.py"
  generated_at: "{context['cgen_timestamp']}"
  cgen_version: "{CGEN_VERSION}"
  template: "templates/cgen/ata03_meta.yaml.j2"
  target_dir: "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_03-SUPPORT_INFRA"
  idempotent: true
"""


def _write_file(path: Path, content: str, dry_run: bool) -> str:
    """Write content to path; return action taken: created/updated/unchanged."""
    if dry_run:
        log.info("[DRY RUN] Would write: %s", path)
        return "skipped"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            log.debug("Unchanged: %s", path)
            return "unchanged"
        path.write_text(content, encoding="utf-8")
        log.info("Updated: %s", path)
        return "updated"
    path.write_text(content, encoding="utf-8")
    log.info("Created: %s", path)
    return "created"


def _sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Content generators
# ---------------------------------------------------------------------------

def _generate_readme(categories: list, timestamp: str) -> str:
    """Generate README.md for the ATA_03-SUPPORT_INFRA directory."""
    lines = [
        "# ATA 03 — Ground Support Equipment and Tooling Infrastructure",
        "",
        "> **OPT-IN Framework Axis:** I — Infrastructures  ",
        "> **Sub-Axis:** O — Operations & Service Structures  ",
        "> **Generated by:** `scripts/cgen_ata03.py`  ",
        f"> **Last generated:** `{timestamp}`",
        "",
        "## Overview",
        "",
        "This directory contains metadata records for ATA 03 Ground Support Equipment (GSE)",
        "and tooling infrastructure within the AMPEL360 Q100 programme.",
        "",
        "ATA 03 covers all ground support equipment, specialised tooling, and related",
        "infrastructure required for aircraft operations, maintenance, and servicing.",
        "Novel hydrogen-specific GSE is marked with `novel_technology: true` and cross-",
        "references the `ATA_IN_H2_GSE_AND_SUPPLY_CHAIN` directory.",
        "",
        "## GSE Categories",
        "",
        "| Section | Title | Novel Technology | Primary LC Phase |",
        "| ------- | ----- | :--------------: | ---------------- |",
    ]
    for cat in categories:
        novel = "✓" if cat.get("novel_technology") else ""
        lines.append(
            f"| ATA 03-{cat['ata_section']}-{cat['ata_subject']} "
            f"| {cat['section_title']} | {novel} | {cat['lc_phase']} |"
        )
    lines += [
        "",
        "## Lifecycle Applicability",
        "",
        "The following infrastructure lifecycle phases apply to ATA 03 GSE content:",
        "",
        "| Phase | Name | Description |",
        "| ----- | ---- | ----------- |",
        "| LC04  | Design Definition | Infrastructure design and specifications |",
        "| LC06  | Integration & Test | Infrastructure testing and commissioning |",
        "| LC10  | Industrial & Supply Chain | Infrastructure production and deployment |",
        "| LC11  | Operations Customization | Customer infrastructure integration |",
        "| LC12  | Continued Airworthiness & MRO | Infrastructure maintenance and upgrades |",
        "",
        "## Related Infrastructure",
        "",
        "| Path | Description |",
        "| ---- | ----------- |",
        "| `../ATA_IN_H2_GSE_AND_SUPPLY_CHAIN/` | Hydrogen GSE and supply chain (extended scope) |",
        "| `../../M2-MAINTENANCE_ENVIRONMENTS/ATA_12-SERVICING_INFRA/` | Servicing infrastructure |",
        "",
        "## File Naming Convention",
        "",
        "```",
        "ATA_03-{section}-{subject}_{TITLE}.meta.yaml",
        "```",
        "",
        "All `.meta.yaml` files conform to `schemas/ampel360_metadata_record.schema.json`.",
        "",
        "## Authority",
        "",
        "- **Authority:** ASIT (Aircraft Systems Information Transponder)",
        "- **Compliance:** S1000D Issue 5.0, TLI v2.1",
        "- **BREX:** BREX-S1000D-5.0-DEFAULT",
        "",
    ]
    return "\n".join(lines)


def _generate_index(categories: list, timestamp: str) -> str:
    """Generate 00_INDEX.md listing all generated files."""
    lines = [
        "# 00 — Index: ATA 03 Ground Support Equipment and Tooling",
        "",
        f"> Generated: `{timestamp}`  ",
        f"> File count: `{len(categories) + 2}` (including README.md and this index)",
        "",
        "## Metadata Records",
        "",
        "| # | File | Section | Title | Status |",
        "| - | ---- | ------- | ----- | ------ |",
    ]
    for i, cat in enumerate(categories, 1):
        lines.append(
            f"| {i} | [{cat['filename']}]({cat['filename']}) "
            f"| ATA 03-{cat['ata_section']}-{cat['ata_subject']} "
            f"| {cat['section_title']} | DRAFT |"
        )
    lines += [
        "",
        "## Documentation",
        "",
        "| File | Description |",
        "| ---- | ----------- |",
        "| [README.md](README.md) | Directory overview and GSE category table |",
        "| [00_INDEX.md](00_INDEX.md) | This index file |",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main generation logic
# ---------------------------------------------------------------------------

def run(output_dir: Path, timestamp: str, dry_run: bool) -> list:
    """Run ATA 03 generation. Returns list of manifest file entries."""
    log.info("=== CGen ATA 03 v%s ===", CGEN_VERSION)
    log.info("Output dir : %s", output_dir)
    log.info("Timestamp  : %s", timestamp)
    log.info("Dry run    : %s", dry_run)

    # Load dependencies
    phases = _load_lifecycle_registry()
    log.info("Loaded %d lifecycle phases from registry", len(phases))

    artifact_types = _load_artifact_types()
    log.info("Loaded %d artifact type codes", len(artifact_types))

    brex_id = _load_brex_metadata()
    log.info("BREX ID: %s", brex_id)

    manifest_entries = []

    # Generate .meta.yaml files for each category
    for cat in ATA03_CATEGORIES:
        lc_phase = cat["lc_phase"]
        phase_info = phases.get(lc_phase, {})
        lc_canonical_name = phase_info.get("canonical_name", lc_phase)
        lc_phase_type = phase_info.get("phase_type", "PLM")
        gate_id = phase_info.get("gate_id", f"G-{lc_phase}")
        package_origin = (phase_info.get("packages") or ["INFRA"])[0]

        # ssot_root and ssot_dir per schema: enum root + canonical LC dir name
        registry_ssot_path = phase_info.get("ssot_dir", "")
        ssot_dir = registry_ssot_path.split("/")[-1] if registry_ssot_path else f"{lc_phase}_DESIGN_DEFINITION"
        ssot_root = "KDB/LM/SSOT/PLM" if lc_phase_type == "PLM" else "IDB/OPS/LM"
        # Actual filesystem path stored separately
        ssot_filesystem_path = (
            "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES"
            "/ATA_03-SUPPORT_INFRA"
        )

        record_id = _make_record_id(
            cat["ata_section"],
            cat["ata_subject"],
            lc_phase,
            cat["artifact_type"],
            1,
        )

        context = {
            "record_id": record_id,
            "msn": MSN,
            "ata_section": cat["ata_section"],
            "ata_subject": cat["ata_subject"],
            "section_title": cat["section_title"],
            "subject_title": cat["subject_title"],
            "lc_phase": lc_phase,
            "lc_canonical_name": lc_canonical_name,
            "lc_phase_type": lc_phase_type,
            "artifact_type": cat["artifact_type"],
            "artifact_type_name": cat.get("artifact_type_name", artifact_types.get(cat["artifact_type"], cat["artifact_type"])),
            "artifact_title": cat["artifact_title"],
            "status": "DRAFT",
            "revision": "1.0",
            "classification": "SSOT",
            "novel_technology": cat.get("novel_technology", False),
            "cgen_timestamp": timestamp,
            "cgen_version": CGEN_VERSION,
            "brex_id": brex_id,
            "gate_id": gate_id,
            "ssot_root": ssot_root,
            "ssot_dir": ssot_dir,
            "ssot_filesystem_path": ssot_filesystem_path,
            "package_origin": package_origin,
            "notes": cat.get("notes", ""),
            "cross_refs": cat.get("cross_refs", []),
        }

        # Try Jinja2 template first, fall back to direct render
        content = _render_template(TEMPLATE_FILE, context) if TEMPLATE_FILE.exists() else None
        if content is None:
            log.debug("Using direct render for %s", cat["filename"])
            content = _build_meta_yaml_direct(context)

        # Validate YAML can be parsed
        try:
            parsed = yaml.safe_load(content)
        except yaml.YAMLError as exc:
            log.error("Generated YAML parse error for %s: %s", cat["filename"], exc)
            raise
        if not isinstance(parsed, dict) or parsed.get("record_id") != record_id:
            raise ValueError(
                f"record_id mismatch in {cat['filename']}: "
                f"expected '{record_id}', got '{parsed.get('record_id') if isinstance(parsed, dict) else type(parsed)}'"
            )

        dest = output_dir / cat["filename"]
        action = _write_file(dest, content, dry_run)
        manifest_entries.append({
            "path": str(dest.relative_to(REPO_ROOT)),
            "sha256": _sha256(content),
            "action": action,
            "size_bytes": len(content.encode("utf-8")),
            "generator": "cgen_ata03.py",
        })

    # Generate README.md
    readme_content = _generate_readme(ATA03_CATEGORIES, timestamp)
    readme_dest = output_dir / "README.md"
    action = _write_file(readme_dest, readme_content, dry_run)
    manifest_entries.append({
        "path": str(readme_dest.relative_to(REPO_ROOT)),
        "sha256": _sha256(readme_content),
        "action": action,
        "size_bytes": len(readme_content.encode("utf-8")),
        "generator": "cgen_ata03.py",
    })

    # Generate 00_INDEX.md
    index_content = _generate_index(ATA03_CATEGORIES, timestamp)
    index_dest = output_dir / "00_INDEX.md"
    action = _write_file(index_dest, index_content, dry_run)
    manifest_entries.append({
        "path": str(index_dest.relative_to(REPO_ROOT)),
        "sha256": _sha256(index_content),
        "action": action,
        "size_bytes": len(index_content.encode("utf-8")),
        "generator": "cgen_ata03.py",
    })

    log.info(
        "ATA 03 generation complete: %d files (%d created, %d updated, %d unchanged)",
        len(manifest_entries),
        sum(1 for e in manifest_entries if e["action"] == "created"),
        sum(1 for e in manifest_entries if e["action"] == "updated"),
        sum(1 for e in manifest_entries if e["action"] == "unchanged"),
    )
    return manifest_entries


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate ATA 03 GSE infrastructure metadata files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT
        / "OPT-IN_FRAMEWORK"
        / "I-INFRASTRUCTURES"
        / "O-OPERATIONS_SERVICE_STRUCTURES"
        / "ATA_03-SUPPORT_INFRA",
        help="Target output directory (default: real repo path)",
    )
    parser.add_argument(
        "--timestamp",
        type=str,
        required=True,
        help="ISO 8601 UTC generation timestamp, e.g. 2026-03-07T03:00:00Z",
    )
    parser.add_argument(
        "--manifest-out",
        type=Path,
        default=None,
        help="Optional path to write per-script manifest JSON",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and log without writing files",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
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
        log.info("Manifest written to %s", args.manifest_out)

    return 0


if __name__ == "__main__":
    sys.exit(main())
