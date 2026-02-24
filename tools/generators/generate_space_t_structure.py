#!/usr/bin/env python3
"""
AMPEL360 Space-T Directory Structure Generator
===============================================

Generates the canonical directory structure for AMPEL360-SPACE-T (Q10 PLUS)
following the unified primary code (7-axis / 33-subdomain / 3-digit chapters).

Chapter system: 000–124 (3-digit zero-padded), excluding X13/X17 set
{013, 017, 113, 117} per AMPEL360-OPTIN-CULTURAL-EXCLUSION-001.

Usage
-----
    # Dry run — print structure without creating files
    python generate_space_t_structure.py --dry-run

    # Generate full structure under ./AMPEL360-SPACE-T/
    python generate_space_t_structure.py

    # Generate only selected ATA systems
    python generate_space_t_structure.py --systems 028 057 071

    # Generate to a custom base directory
    python generate_space_t_structure.py --output /path/to/output

Author:   ASIT (Aircraft Systems Information Transponder)
Document: AMPEL360-GEN-SPACE-T-001
Date:     2026-02-24
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------------------

MAX_CHAPTER = 124

# X13/X17 cultural exclusion — permanently excluded chapters
EXCLUDED_CHAPTERS: frozenset[str] = frozenset(
    f"{i:03d}"
    for i in range(MAX_CHAPTER + 1)
    if "13" in f"{i:03d}" or "17" in f"{i:03d}"
)

# All active chapters (000–124 minus excluded)
ACTIVE_CHAPTERS: list[str] = [
    f"{i:03d}"
    for i in range(MAX_CHAPTER + 1)
    if f"{i:03d}" not in EXCLUDED_CHAPTERS
]

# ---------------------------------------------------------------------------
# AXIS / SUBDOMAIN DEFINITIONS
# ---------------------------------------------------------------------------

# O — Organization
O_CHAPTERS = ["001", "002", "003", "004", "012", "018"]

# P — Program
P_CHAPTERS = ["000", "005", "006", "007", "008", "009", "010", "011"]

# R — Reserved
R_CHAPTERS = ["014", "015", "016", "019"]

# T — Technology (ATA 020–079, 095, 097)
T_CHAPTERS = [
    "020", "021", "022", "023", "024", "025", "026", "027", "028", "029",
    "030", "031", "032", "033", "034", "035", "036", "037", "038", "039",
    "040", "041", "042", "043", "044", "045", "046", "047", "048", "049",
    "050", "051", "052", "053", "054", "055", "056", "057", "058", "059",
    "060", "061", "062", "063", "064", "065", "066", "067", "068", "069",
    "070", "071", "072", "073", "074", "075", "076", "077", "078", "079",
    "095", "097",
]

# I — Infrastructures (080–089)
I_CHAPTERS = ["080", "081", "082", "083", "084", "085", "086", "087", "088", "089"]

# N — Neural Networks / DPP (090–099)
N_CHAPTERS = ["090", "091", "092", "093", "094", "096", "098", "099"]

# S — SimTest & Digital Twin (100–124 excl. 113, 117)
S_CHAPTERS = [c for c in ACTIVE_CHAPTERS if 100 <= int(c) <= 124]

# S-axis subdomains
S_SUBDOMAINS: dict[str, list[str]] = {
    "G": ["100", "101", "102"],           # Geometry & Mesh
    "X": ["103", "104", "105"],           # CFD / FEM Simulation
    "T": ["106", "107", "108"],           # Thermal Simulation
    "V": ["109", "110", "111"],           # Validation
    "F": ["112", "114", "115", "116"],    # Functional Simulation (no 113)
    "U": ["118", "119", "120", "121", "122", "123"],  # UQ (no 117; 123 = ex-113)
    "R": ["124"],                          # Extended Reality XR/AR/VR (124 = ex-117)
}

# Lifecycle folder structure (14 phases, both PLM and OPS)
LIFECYCLE_FOLDERS = [
    "LC01_PROBLEM_STATEMENT",
    "LC02_SYSTEM_REQUIREMENTS",
    "LC03_SAFETY_RELIABILITY",
    "LC04_DESIGN_DEFINITION",
    "LC05_ANALYSIS_MODELS",
    "LC06_VERIFICATION",
    "LC07_QA_PROCESS",
    "LC08_CERTIFICATION",
    "LC09_ESG_SUSTAINABILITY",
    "LC10_INDUSTRIAL_SUPPLY",
    "LC11_OPERATIONS_CUSTOMIZATION",
    "LC12_MAINTENANCE_REPAIR",
    "LC13_MAINTENANCE_SOURCE",
    "LC14_END_OF_LIFE",
]

# 9 cross-ATA bucket folders per chapter
CROSS_ATA_BUCKETS = [
    "REQUIREMENTS",
    "DESIGN",
    "SAFETY",
    "ANALYSIS",
    "VERIFICATION",
    "CERTIFICATION",
    "OPERATIONS",
    "MAINTENANCE",
    "GOVERNANCE",
]

# Engineering cycle per subsystem
ENGINEERING_CYCLE = ["P", "CAD", "CAE", "CAM", "CAOS"]

# ---------------------------------------------------------------------------
# GENERATOR
# ---------------------------------------------------------------------------


def _make(path: Path, dry_run: bool) -> None:
    """Create a directory (or print in dry-run mode)."""
    if dry_run:
        print(f"  [DIR]  {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)


def _touch(path: Path, dry_run: bool) -> None:
    """Create an empty file or .gitkeep (or print in dry-run mode)."""
    if dry_run:
        print(f"  [FILE] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)


def generate_chapter(chapter: str, base: Path, dry_run: bool) -> None:
    """Generate the full folder hierarchy for a single chapter."""
    chapter_dir = base / f"ATA_{chapter}"
    _make(chapter_dir, dry_run)

    # 14-folder lifecycle structure
    for lc in LIFECYCLE_FOLDERS:
        _make(chapter_dir / lc, dry_run)
        _touch(chapter_dir / lc / ".gitkeep", dry_run)

    # 9 cross-ATA buckets
    buckets_dir = chapter_dir / "_CROSS_ATA_BUCKETS"
    for bucket in CROSS_ATA_BUCKETS:
        _touch(buckets_dir / bucket / ".gitkeep", dry_run)

    # P→CAD→CAE→CAM→CAOS engineering cycle (for subsystem 00)
    eng_dir = chapter_dir / "SUBSYSTEM_00" / "ENGINEERING_CYCLE"
    for phase in ENGINEERING_CYCLE:
        _touch(eng_dir / phase / ".gitkeep", dry_run)


def generate_s_axis(
    base: Path,
    dry_run: bool,
    filter_chapters: Optional[set[str]] = None,
) -> None:
    """Generate subdomain folders within the S-SIMTEST axis."""
    s_dir = base / "S-SIMTEST_DIGITAL_TWIN"
    _make(s_dir, dry_run)

    for subdomain_code, chapters in S_SUBDOMAINS.items():
        subdomain_names = {
            "G": "GEOMETRY_MESH",
            "X": "CFD_FEM_SIMULATION",
            "T": "THERMAL_SIMULATION",
            "V": "VALIDATION",
            "F": "FUNCTIONAL_SIMULATION",
            "U": "UNCERTAINTY_QUANTIFICATION",
            "R": "EXTENDED_REALITY_XR",
        }
        folder_name = f"S{subdomain_code}-{subdomain_names[subdomain_code]}"
        sd_dir = s_dir / folder_name

        active = [c for c in chapters if filter_chapters is None or c in filter_chapters]
        if not active:
            continue

        _make(sd_dir, dry_run)
        for chapter in active:
            generate_chapter(chapter, sd_dir, dry_run)


def generate_axis(
    axis_name: str,
    chapters: list[str],
    base: Path,
    dry_run: bool,
    filter_chapters: Optional[set[str]] = None,
) -> None:
    """Generate all chapters for a given axis."""
    axis_dir = base / axis_name
    _make(axis_dir, dry_run)

    for chapter in chapters:
        # filter_chapters is None → generate all; empty/non-empty set → filter
        if filter_chapters is not None and chapter not in filter_chapters:
            continue
        generate_chapter(chapter, axis_dir, dry_run)


def generate_all(
    output_dir: Path,
    dry_run: bool,
    filter_chapters: Optional[set[str]] = None,
) -> None:
    """Generate the complete AMPEL360-SPACE-T directory structure."""
    base = output_dir / "AMPEL360-SPACE-T"
    _make(base, dry_run)

    print(f"\n{'[DRY-RUN] ' if dry_run else ''}Generating AMPEL360-SPACE-T structure")
    print(f"  Output: {base}")
    print(f"  Active chapters: {len(ACTIVE_CHAPTERS)}")
    print(f"  Excluded chapters (X13/X17): {sorted(EXCLUDED_CHAPTERS)}\n")

    # O axis
    generate_axis("O-ORGANIZATIONS", O_CHAPTERS, base, dry_run, filter_chapters)

    # P axis
    generate_axis("P-PROGRAMS", P_CHAPTERS, base, dry_run, filter_chapters)

    # R axis
    generate_axis("R-RESERVED", R_CHAPTERS, base, dry_run, filter_chapters)

    # T axis
    generate_axis(
        "T-TECHNOLOGIES_ON_BOARD_SYSTEMS", T_CHAPTERS, base, dry_run, filter_chapters
    )

    # I axis
    generate_axis("I-INFRASTRUCTURES", I_CHAPTERS, base, dry_run, filter_chapters)

    # N axis
    generate_axis("N-NEURAL_NETWORKS_DPP", N_CHAPTERS, base, dry_run, filter_chapters)

    # S axis — special: has subdomain sub-folders
    # S axis is generated if no filter or if any S chapter passes the filter
    if filter_chapters is None or any(c in filter_chapters for c in S_CHAPTERS):
        generate_s_axis(base, dry_run, filter_chapters)

    print(f"\n{'[DRY-RUN] ' if dry_run else ''}Structure generation complete.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:  # pragma: no cover
    parser = argparse.ArgumentParser(
        description="Generate AMPEL360-SPACE-T directory structure (3-digit chapters 000–124)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print directories/files without creating them",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=".",
        help="Base output directory (default: current directory)",
    )
    parser.add_argument(
        "--systems",
        nargs="+",
        metavar="CCC",
        help="Optional: generate only these 3-digit chapter codes (e.g. 028 057 071)",
    )
    args = parser.parse_args()

    filter_chapters: Optional[set[str]] = None
    if args.systems:
        filter_chapters = set()
        for s in args.systems:
            code = f"{int(s):03d}"
            if code in EXCLUDED_CHAPTERS:
                print(
                    f"WARNING: Chapter {code} is permanently excluded "
                    "(X13/X17 policy). Skipping.",
                    file=sys.stderr,
                )
            else:
                filter_chapters.add(code)

    output_dir = Path(args.output).resolve()
    generate_all(output_dir, args.dry_run, filter_chapters)


if __name__ == "__main__":
    main()
