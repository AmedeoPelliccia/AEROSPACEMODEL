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
cgen_h2gse.py — H2 GSE and Supply Chain Stub Generator
=======================================================
Generates placeholder `.meta.yaml` files for hydrogen GSE categories under
OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN.

All generated files are marked `status: PLACEHOLDER` — they are stubs intended
to be replaced with full content in a future generation cycle once detailed
H2 GSE specifications are available.

Usage:
    python scripts/cgen_h2gse.py \\
        --output-dir OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN \\
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
LIFECYCLE_REGISTRY = REPO_ROOT / "lifecycle" / "LC_PHASE_REGISTRY.yaml"
BREX_FILE = REPO_ROOT / "ASIGT" / "brex" / "S1000D_5.0_DEFAULT.yaml"

CGEN_VERSION = "1.0.0"
MSN = "MSN001"

# H2 GSE categories — use "IN" chapter code for cross-domain/novel ATA chapters
H2GSE_CATEGORIES = [
    {
        "filename": "ATA_IN-10-00_H2_REFUELING_SYSTEMS.meta.yaml",
        "ata_section": "10",
        "ata_subject": "00",
        "section_title": "H2 Refueling Systems",
        "subject_title": "Hydrogen Refueling Systems",
        "artifact_title": "ATA IN-10-00 Hydrogen Refueling Systems — Stub",
        "lc_phase": "LC04",
        "notes": "Stub placeholder for H2 refueling systems GSE. Full content pending H2 GSE specification.",
        "cross_refs": ["ATA_03-70-00_H2_SPECIFIC_GSE", "ATA_28-FUEL"],
    },
    {
        "filename": "ATA_IN-20-00_CRYOGENIC_STORAGE.meta.yaml",
        "ata_section": "20",
        "ata_subject": "00",
        "section_title": "Cryogenic Storage",
        "subject_title": "Cryogenic LH2 Storage Infrastructure",
        "artifact_title": "ATA IN-20-00 Cryogenic LH2 Storage Infrastructure — Stub",
        "lc_phase": "LC04",
        "notes": "Stub placeholder for cryogenic LH2 storage GSE. Covers ground-side cryo vessels and insulation.",
        "cross_refs": ["ATA_28-FUEL", "ATA_71-FUEL_CELL_SYSTEMS"],
    },
    {
        "filename": "ATA_IN-30-00_BOILOFF_RECOVERY.meta.yaml",
        "ata_section": "30",
        "ata_subject": "00",
        "section_title": "Boil-Off Recovery",
        "subject_title": "Hydrogen Boil-Off Recovery and Management",
        "artifact_title": "ATA IN-30-00 Hydrogen Boil-Off Recovery — Stub",
        "lc_phase": "LC10",
        "notes": "Stub placeholder for H2 boil-off recovery equipment. Covers recovery, reliquefaction, safe venting.",
        "cross_refs": ["ATA_IN-20-00_CRYOGENIC_STORAGE"],
    },
    {
        "filename": "ATA_IN-40-00_LEAK_DETECTION.meta.yaml",
        "ata_section": "40",
        "ata_subject": "00",
        "section_title": "Leak Detection",
        "subject_title": "Hydrogen Leak Detection Systems",
        "artifact_title": "ATA IN-40-00 Hydrogen Leak Detection Systems — Stub",
        "lc_phase": "LC06",
        "notes": "Stub placeholder for ground-side H2 leak detection. Covers electrochemical, optical, and thermal sensors.",
        "cross_refs": ["ATA_IN-50-00_EMERGENCY_SYSTEMS"],
    },
    {
        "filename": "ATA_IN-50-00_EMERGENCY_SYSTEMS.meta.yaml",
        "ata_section": "50",
        "ata_subject": "00",
        "section_title": "Emergency Systems",
        "subject_title": "Hydrogen Emergency Response Systems",
        "artifact_title": "ATA IN-50-00 Hydrogen Emergency Response Systems — Stub",
        "lc_phase": "LC10",
        "notes": "Stub placeholder for H2 emergency response GSE. Covers fire suppression, emergency venting, PPE.",
        "cross_refs": ["ATA_IN-40-00_LEAK_DETECTION"],
    },
    {
        "filename": "ATA_IN-60-00_SUPPLY_CHAIN.meta.yaml",
        "ata_section": "60",
        "ata_subject": "00",
        "section_title": "Supply Chain",
        "subject_title": "Hydrogen Supply Chain Infrastructure",
        "artifact_title": "ATA IN-60-00 Hydrogen Supply Chain Infrastructure — Stub",
        "lc_phase": "LC10",
        "notes": "Stub placeholder for H2 supply chain infrastructure. Covers production, transport, and delivery.",
        "cross_refs": ["ATA_IN-10-00_H2_REFUELING_SYSTEMS"],
    },
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log = logging.getLogger("cgen_h2gse")


def _setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if data is None:
        raise ValueError(f"Empty YAML file: {path}")
    return data


def _load_lifecycle_registry() -> dict:
    registry = _load_yaml(LIFECYCLE_REGISTRY)
    combined: dict = {}
    combined.update(registry.get("plm_phases", {}))
    combined.update(registry.get("ops_phases", {}))
    return combined


def _load_brex_id() -> str:
    brex_data = _load_yaml(BREX_FILE)
    return brex_data.get("brex", {}).get("metadata", {}).get("brex_id", "BREX-S1000D-5.0-DEFAULT")


def _make_record_id(ata_section: str, ata_subject: str, lc_phase: str, seq: int = 1) -> str:
    """Build canonical AMPEL360 identifier for IN (novel) ATA chapter."""
    return f"AMPEL360_Q100_{MSN}_ATAIN-{ata_section}-{ata_subject}_{lc_phase}_DES_{seq:03d}"


def _build_content(cat: dict, phases: dict, brex_id: str, timestamp: str) -> str:
    """Build .meta.yaml content for a H2 GSE category."""
    lc_phase = cat["lc_phase"]
    phase_info = phases.get(lc_phase, {})
    lc_canonical_name = phase_info.get("canonical_name", lc_phase)
    lc_phase_type = phase_info.get("phase_type", "PLM")
    gate_id = phase_info.get("gate_id", f"G-{lc_phase}")
    package_origin = (phase_info.get("packages") or ["INFRA"])[0]

    record_id = _make_record_id(cat["ata_section"], cat["ata_subject"], lc_phase, 1)
    ssot_dir = (
        "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES"
        "/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN"
    )

    cross_refs_yaml = ""
    if cat.get("cross_refs"):
        lines = "\n".join(f'  - "{r}"' for r in cat["cross_refs"])
        cross_refs_yaml = f"cross_references:\n{lines}"
    else:
        cross_refs_yaml = "cross_references: []"

    return f"""\
# =============================================================================
# AMPEL360 Q100 — H2 GSE Metadata Stub Record
# Generated by cgen_h2gse.py v{CGEN_VERSION}
# STATUS: PLACEHOLDER — replace with full content when H2 GSE spec available
# =============================================================================
record_id: "{record_id}"
aircraft_id: "AMPEL360"
model_id: "Q100"
msn: "{MSN}"

ata_chapter: "IN"
ata_chapter_title: "Hydrogen GSE and Supply Chain"
section: "{cat['ata_section']}"
section_title: "{cat['section_title']}"
subject: "{cat['ata_subject']}"
subject_title: "{cat['subject_title']}"

optin_axis: "I"
optin_subaxis: "O"
optin_subaxis_name: "Operations & Service Structures"

novel_technology: true

phase_type: "{lc_phase_type}"
lc_phase: "{lc_phase}"
lc_canonical_name: "{lc_canonical_name}"
package_origin: "{package_origin}"

lifecycle_applicability:
  - {{phase: "LC04", description: "Infrastructure design and specifications"}}
  - {{phase: "LC06", description: "Infrastructure testing and commissioning"}}
  - {{phase: "LC10", description: "Infrastructure production and deployment"}}
  - {{phase: "LC11", description: "Customer infrastructure integration"}}
  - {{phase: "LC12", description: "Infrastructure maintenance and upgrades"}}

artifact_type: "DES"
artifact_type_name: "Design Document"
artifact_title: "{cat['artifact_title']}"

owner_aor: "ASIT/I-INFRASTRUCTURES/O-OPERATIONS"
status: "PLACEHOLDER"
revision: "00"
prepared_by: "cgen_h2gse.py"
date_created: "{timestamp}"
date_modified: "{timestamp}"
classification: "UNCLASSIFIED"

ssot_root: "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES"
ssot_dir: "{ssot_dir}"

gate_id: "{gate_id}"

brex_reference:
  brex_id: "{brex_id}"
  standard: "S1000D Issue 5.0"
  validated: true

{cross_refs_yaml}

notes: "{cat.get('notes', '')}"

cgen:
  generated_by: "cgen_h2gse.py"
  generated_at: "{timestamp}"
  cgen_version: "{CGEN_VERSION}"
  target_dir: "OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/O-OPERATIONS_SERVICE_STRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN"
  idempotent: true
"""


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


# ---------------------------------------------------------------------------
# Main generation logic
# ---------------------------------------------------------------------------

def run(output_dir: Path, timestamp: str, dry_run: bool) -> list:
    """Run H2 GSE stub generation. Returns list of manifest file entries."""
    log.info("=== CGen H2 GSE v%s ===", CGEN_VERSION)
    log.info("Output dir : %s", output_dir)
    log.info("Timestamp  : %s", timestamp)
    log.info("Dry run    : %s", dry_run)

    phases = _load_lifecycle_registry()
    brex_id = _load_brex_id()

    manifest_entries = []

    for cat in H2GSE_CATEGORIES:
        content = _build_content(cat, phases, brex_id, timestamp)

        # Validate YAML parseable
        try:
            yaml.safe_load(content)
        except yaml.YAMLError as exc:
            log.error("YAML validation failed for %s: %s", cat["filename"], exc)
            raise

        dest = output_dir / cat["filename"]
        action = _write_file(dest, content, dry_run)
        manifest_entries.append({
            "path": str(dest.relative_to(REPO_ROOT)),
            "sha256": _sha256(content),
            "action": action,
            "size_bytes": len(content.encode("utf-8")),
            "generator": "cgen_h2gse.py",
        })

    log.info(
        "H2 GSE generation complete: %d files (%d created, %d updated, %d unchanged)",
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
        description="Generate H2 GSE stub metadata files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT
        / "OPT-IN_FRAMEWORK"
        / "I-INFRASTRUCTURES"
        / "O-OPERATIONS_SERVICE_STRUCTURES"
        / "ATA_IN_H2_GSE_AND_SUPPLY_CHAIN",
        help="Target output directory",
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
