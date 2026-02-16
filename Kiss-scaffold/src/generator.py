from __future__ import annotations

import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List
import textwrap


@dataclass
class GenContext:
    base: Path
    mode: str  # overwrite | safe | fail
    now_iso: str
    date_short: str
    written: List[Path]


class GenerationError(Exception):
    """Raised for generation-time conflicts and invalid inputs."""


def _norm(content: str) -> str:
    """Normalize multiline literals: dedent and remove leading blank lines."""
    return textwrap.dedent(content).lstrip("\n")


def _atomic_write_text(path: Path, content: str) -> None:
    """
    Atomically write UTF-8 text with LF newlines.

    Ensures file content is either old or fully new, never partial.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def _write(ctx: GenContext, rel_path: str, content: str) -> None:
    """
    Write a file under ctx.base using collision policy:
      - fail: raise if exists
      - safe: skip if exists
      - overwrite: replace if exists
    """
    p = ctx.base / rel_path

    if p.exists():
        if ctx.mode == "fail":
            raise GenerationError(f"Collision in mode=fail: {p}")
        if ctx.mode == "safe":
            return
        if ctx.mode != "overwrite":
            raise GenerationError(f"Unknown mode: {ctx.mode}")

    _atomic_write_text(p, _norm(content))
    ctx.written.append(p)


def gen_root(ctx: GenContext) -> None:
    """Generate ATA 00 root docs."""
    _write(
        ctx,
        "00-00-general/README.md",
        f"""\
        # ATA 00-00 — GenKISS

        - `GENESIS/` — Knowledge Determination Space
        - `SSOT/` — Authoritative Information Source
        - `PUB/ATDP/` — Aircraft Technical Data Product umbrella

        **GenKISS**: General Knowledge and Information Standard Systems
        
        Generated: {ctx.date_short}
        """,
    )

    _write(
        ctx,
        "00-00-general/00_INDEX.md",
        """\
        # ATA 00-00 — Index
        - GENESIS
        - SSOT
        - CSDB_REF
        - PUB/ATDP
        - ../00-90-tables-schemas-index
        """,
    )


def gen_genesis(ctx: GenContext) -> None:
    """Generate GENESIS knowledge space seed."""
    _write(
        ctx,
        "00-00-general/GENESIS/README.md",
        """\
        # GENESIS — Knowledge Determination Space

        > Epistemic workspace for uncertainty discovery, justification, and framing before SSOT commitment.

        ---

        ## Purpose

        `GENESIS` is the **knowledge domain** of Aircraft GenKISS.  
        It captures what is not yet authoritative:

        - unknowns
        - assumptions
        - decision alternatives
        - framing boundaries
        - acceptance intent prior to lifecycle execution

        GENESIS artifacts are **pre-authoritative** and exist to make epistemic state explicit before information enters SSOT.

        ---

        ## Epistemic Position

        | Attribute | GENESIS |
        |---|---|
        | Nature | Uncertain, exploratory, contextual |
        | Authority | Pre-authoritative |
        | Mutability | High (iterative knowledge work) |
        | Primary Function | Determine what must be resolved and why |
        | Output | Graduatable KNOT framing for SSOT entry |

        ---

        ## Locked Governance Rule

        **Locked Rule 1**  
        `GENESIS` must not contain executed lifecycle artifacts.

        ### Forbidden in GENESIS
        - `_executions/` directories
        - certification evidence packages
        - production release artifacts
        - authoritative compliance records

        ### Allowed in GENESIS
        - O-KNOT, Y-KNOT, KNOT records
        - rationale, options analysis, boundary framing
        - registries describing knowledge progression
        - schema-conformant pre-authoritative metadata

        ---

        ## Canonical Knowledge Pipeline

        ```text
        O-KNOT  ->  Y-KNOT  ->  KNOT  ->  (graduation)  ->  SSOT/LC01+
        Discovery   Justify     Frame                        Authoritative lifecycle
        ```

        ### O-KNOT (Discovery)

        **Question**: What is unknown?  
        **Outputs**: uncertainty statement, context, initial trace anchors.

        ### Y-KNOT (Justification)

        **Question**: Why does it matter, and which option is preferable?  
        **Outputs**: options analysis, decision rationale, tradeoff basis.

        ### KNOT (Framing)

        **Question**: What exactly will be resolved and how acceptance is defined?  
        **Outputs**: bounded scope, acceptance criteria, planned downstream KNUs.

        ---

        ## Directory Layout

        ```text
        GENESIS/
        ├── README.md
        ├── _registry/
        │   ├── o-knot_registry.csv
        │   ├── y-knot_registry.csv
        │   └── knot_registry.csv
        ├── O-KNOT/
        │   └── O-KNOT-<ID>/
        ├── Y-KNOT/
        │   └── Y-KNOT-<ID>/
        └── KNOT/
            └── KNOT-<ID>/
        ```

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """,
    )

    _write(
        ctx,
        "00-00-general/GENESIS/_registry/o-knot_registry.csv",
        """\
        O_KNOT_ID,Title,ATA_Chapter,ATA_Section,Status,Discovery_Date,Owner_AoR,Heritage_Ref,Notes
        O-KNOT-00-00-001,GenKISS Ontology Foundation,00,00,OPEN,,STK_DATA,,Seed
        """,
    )


def gen_ssot(ctx: GenContext, phases: Dict[str, Any]) -> None:
    """
    Generate SSOT structure and canonical LC README stubs.

    `phases` can include optional internal key `_ordered_lc_ids`.
    If absent, LC keys are inferred and sorted lexicographically.
    """
    _write(
        ctx,
        "00-00-general/SSOT/README.md",
        """\
        # SSOT — Authoritative Information Source
        Executions must be under `_executions/<UTC>/`.
        """,
    )

    _write(
        ctx,
        "00-00-general/SSOT/LC01_PROBLEM_STATEMENT/KNOTS.csv",
        """\
        KNOT_ID,Title,Status
        KNOT-00-00-005,GenKISS Baseline Definition,OPEN
        """,
    )

    safe_ts = ctx.now_iso.replace(":", "-")
    _write(
        ctx,
        f"00-00-general/SSOT/LC02_SYSTEM_REQUIREMENTS/"
        f"KNU-00-00-005-LC02-GenKISS-SYS_REQ/_executions/{safe_ts}/artifact.md",
        f"""\
        # Execution
        Execution: {ctx.now_iso}
        Status: DRAFT
        """,
    )

    ordered_ids = phases.get("_ordered_lc_ids")
    if not isinstance(ordered_ids, list):
        ordered_ids = sorted([k for k in phases.keys() if k.startswith("LC")])

    for lc_id in ordered_ids:
        if lc_id not in phases:
            continue
        spec = phases[lc_id]
        if not isinstance(spec, dict):
            raise GenerationError(f"{lc_id} spec must be object; got {type(spec).__name__}")

        canonical_name = spec.get("canonical_name", "")
        ssot_dir = spec.get("ssot_dir", "")
        phase_type = spec.get("phase_type", "")

        _write(
            ctx,
            f"00-00-general/SSOT/{lc_id}/README.md",
            f"""\
            # {lc_id}
            Canonical name: {canonical_name}
            Canonical registry path: {ssot_dir}
            Phase type: {phase_type}
            """,
        )


def gen_csdb_pub(ctx: GenContext, atdp_cfg: Dict[str, Any]) -> None:
    """Generate CSDB_REF and PUB/ATDP structure."""
    products = atdp_cfg.get("products")
    common_csdb_dirs = atdp_cfg.get("common_csdb_dirs")

    if not isinstance(products, list) or not all(isinstance(x, str) for x in products):
        raise GenerationError("atdp_cfg['products'] must be list[str]")
    if not isinstance(common_csdb_dirs, list) or not all(isinstance(x, str) for x in common_csdb_dirs):
        raise GenerationError("atdp_cfg['common_csdb_dirs'] must be list[str]")

    _write(ctx, "00-00-general/CSDB_REF/README.md", """\
        # CSDB_REF — Reference Dataset

        > Atomic, traceable reference layer for GenKISS (not a replacement for SSOT authority).

        ---

        ## Purpose

        `CSDB_REF` stores **NU (Atomic Reference Units)** derived from validated SSOT executions, so downstream consumers can reuse distilled technical knowledge without traversing full lifecycle trees.

        This directory belongs to the ATA 00 KISS scaffold:

        - **GENESIS** → Knowledge Determination Space (uncertain, exploratory)
        - **SSOT** → Authoritative Information Source (validated, lifecycle-bound)
        - **CSDB_REF** → Derived atomic references for controlled reuse
        - **PUB/ATDP** → Delivery surface for Aircraft Technical Data Products

        ---

        ## Governance Position

        `CSDB_REF` is a **derived layer**:

        - It **must trace back** to SSOT execution artifacts.
        - It **must not host** primary certification authority.
        - It **must not contain** raw GENESIS exploratory artifacts.
        - It is **ATDP-agnostic** and can feed AMM, IPC, SRM, TSM, WDM, FIM, MMEL, MPD.

        ---

        ## Structure

        ```text
        CSDB_REF/
        └── NU/
            ├── index.csv
            ├── schema/
            │   └── nu_source.schema.yaml
            └── NU-<ID>/
                ├── content.*        # atomic distilled reference
                ├── _source.yaml     # mandatory provenance to SSOT execution
                └── metadata.yaml    # optional classification/effectivity
        ```

        ---

        ## Mandatory Rules

        1. Every `NU-<ID>/` shall include `_source.yaml`.
        2. `_source.yaml` shall reference a valid SSOT path under:
           - `.../SSOT/.../_executions/<timestamp>/`
        3. No orphan NU directories (must appear in `index.csv`).
        4. NU content is derivative and must never replace SSOT authority.

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """)
    _write(ctx, "00-00-general/CSDB_REF/NU/.gitkeep", "")
    _write(
        ctx,
        "00-00-general/CSDB_REF/NU/README.md",
        """\
        # CSDB_REF / NU — Atomic Reference Units

        This directory stores **atomic consumable reference units (NU)** derived from SSOT executions.

        ## Role in GenKISS

        - **GENESIS**: knowledge determination (uncertain)
        - **SSOT**: authoritative lifecycle information (validated)
        - **CSDB_REF/NU**: distilled reference units for downstream consumption

        NU content is derivative and must never replace SSOT authority.

        ## Rules

        1. Every `NU-<ID>/` must contain `_source.yaml`.
        2. `_source.yaml` must point to an SSOT execution artifact path.
        3. No orphan NU directories (must appear in `index.csv`).
        4. NU is ATDP-agnostic: can feed AMM, IPC, SRM, TSM, WDM, FIM, MMEL, MPD.

        ## Minimal Unit Structure

        ```text
        NU-<ID>/
        ├── content.*            # atomic reference content
        ├── _source.yaml         # provenance from SSOT execution
        └── metadata.yaml        # optional classification/tags/effectivity
        ```

        ## Example index.csv

        ```csv
        NU_ID,Title,Source_KNU_ID,Source_SSOT_Path,Status,Created_UTC,Owner_AoR,Notes
        NU-28-10-001,Tank Geometry Reference,KNU-28-10-001,SSOT/LC05/.../artifact.yaml,ACTIVE,2026-01-15T10:00:00Z,ENG_STRUCT,
        ```

        ## Example _source.yaml Schema

        ```yaml
        nu_id: NU-28-10-001
        source_knu_id: KNU-28-10-001
        source_ssot_execution_path: SSOT/LC05_ANALYSIS_MODELS/KNU-28-10-001/_executions/2026-01-15T10-00-00Z/artifact.yaml
        derived_utc: 2026-01-15T10:30:00Z
        transformation_contract: CNT-SSOT-TO-NU-001
        ```

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """,
    )
    _write(
        ctx,
        "00-00-general/CSDB_REF/NU/index.csv",
        """\
        NU_ID,Title,Source_KNU_ID,Source_SSOT_Path,Status,Created_UTC,Owner_AoR,Notes
        """,
    )
    _write(
        ctx,
        "00-00-general/CSDB_REF/NU/schema/nu_source.schema.yaml",
        """\
        $schema: "http://json-schema.org/draft-07/schema#"
        title: "NU Source Record"
        description: "Traceability record for CSDB_REF atomic units"
        type: object
        required:
          - nu_id
          - source_knu_id
          - source_ssot_execution_path
          - derived_utc
        properties:
          nu_id:
            type: string
            pattern: "^NU-[A-Z0-9\\-]+$"
          source_knu_id:
            type: string
          source_ssot_execution_path:
            type: string
            description: "Path to SSOT _executions/<timestamp>/ artifact"
          derived_utc:
            type: string
            format: date-time
          transformation_contract:
            type: string
            description: "Contract ID governing SSOT->NU transformation"
        """,
    )

    _write(
        ctx,
        "00-00-general/PUB/README.md",
        """\
        # PUB — Publication Surface
        ATDP is umbrella; CSDB is not AMM-only.
        """,
    )
    _write(ctx, "00-00-general/PUB/ATDP/README.md", "# ATDP — Aircraft Technical Data Product\n")
    _write(
        ctx,
        "00-00-general/PUB/ATDP/COMMON_CSDB/README.md",
        """\
        # COMMON_CSDB — Shared CSDB Components for ATDP

        > Reusable, product-agnostic CSDB building blocks for Aircraft Technical Data Products (ATDP).

        ---

        ## Purpose

        `PUB/ATDP/COMMON_CSDB` contains **shared publication primitives** used across ATDP products (AMM, IPC, SRM, TSM, WDM, FIM, MMEL, MPD, etc.).

        This layer avoids duplication and enforces consistency in:

        - data module structures
        - publication module composition
        - business rules (BREX)
        - applicability logic
        - common warnings/cautions/notes
        - graphics and reusable assets

        ---

        ## Position in GenKISS

        ```text
        GENESIS (knowledge determination)
            -> SSOT (authoritative lifecycle information)
                -> CSDB_REF (atomic references)
                    -> PUB/ATDP/COMMON_CSDB (shared publication components)
                        -> PUB/ATDP/PRODUCTS/<AMM|IPC|SRM|...> (final publications)
        ```

        ---

        ## Structure

        ```text
        COMMON_CSDB/
        ├── DM/              # Data Modules (reusable content units)
        ├── PM/              # Publication Modules (composition logic)
        ├── ICN/             # Illustrations (graphics, diagrams)
        ├── BREX/            # Business Rules Exchange (validation rules)
        └── APL/             # Applicability (effectivity, configuration)
        ```

        ---

        ## Governance Rules

        1. **Shared primitives only**: No product-specific content.
        2. **Traceability required**: All DM/PM must trace to CSDB_REF or SSOT.
        3. **Version control**: Changes to COMMON_CSDB require CCB approval.
        4. **Reuse mandatory**: Products must use COMMON_CSDB when available.

        ---

        ## Example Use Cases

        - **Common Warning DM**: "High Voltage Warning" used in AMM, IPC, WDM
        - **Standard Procedure PM**: "Lockout/Tagout Procedure" composition
        - **Generic Illustration**: "Tool Kit Assembly" graphic
        - **Applicability Rule**: "A320 Series with Winglet" effectivity

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """,
    )

    # Generate enhanced COMMON_CSDB structure with detailed subdirectories
    for d in common_csdb_dirs:
        _gen_common_csdb_dir(ctx, d)

    # Generate enhanced product structures with full CSDB hierarchy
    for product in products:
        _gen_product_structure(ctx, product)

    # Generate enhanced ATDP README
    _gen_atdp_readme(ctx)

    _write(ctx, "00-00-general/PUB/ATDP/EXPORT/.gitkeep", "")
    _write(ctx, "00-00-general/PUB/ATDP/IETP/.gitkeep", "")


def _gen_common_csdb_dir(ctx: GenContext, dir_name: str) -> None:
    """Generate enhanced COMMON_CSDB subdirectory with templates and schemas."""
    base_path = f"00-00-general/PUB/ATDP/COMMON_CSDB/{dir_name}"
    
    if dir_name == "DM":
        _write(ctx, f"{base_path}/.gitkeep", "")
        _write(ctx, f"{base_path}/README.md", f"""\
            # COMMON_CSDB / DM — Shared Data Module Layer

            This directory contains reusable, product-agnostic Data Module (DM) assets
            for ATDP products (AMM, IPC, SRM, TSM, WDM, FIM, MMEL, MPD).

            ## Purpose
            - Provide common DM templates and fragments
            - Enforce uniform metadata and traceability
            - Reduce duplication across product-specific publication trees

            ## Rules
            1. Every DM asset must be registered in `dm_index.csv`.
            2. Every DM metadata file must include SSOT/CSDB_REF provenance.
            3. No product-exclusive payload in COMMON DM.
            4. Naming must be deterministic and stable.

            ## Minimal naming convention
            - Content: `DM-<DOMAIN>-<CODE>.md`
            - Metadata: `DM-<DOMAIN>-<CODE>.meta.yaml`

            Example:
            - `DM-TEMPLATE-COMMON-0001.md`
            - `DM-TEMPLATE-COMMON-0001.meta.yaml`

            ---

            **GenKISS**: General Knowledge and Information Standard Systems
            """)
        _write(ctx, f"{base_path}/dm_index.csv", """\
            DM_ID,Title,Type,Language,Applicability,Source_Type,Source_Ref,Status,Owner_AoR,Last_Updated_UTC,Notes
            DM-TEMPLATE-COMMON-0001,Common DM Skeleton,TEMPLATE,EN,ALL,SSOT,KNU-00-00-005-LC02-GenKISS-SYS_REQ,ACTIVE,STK_DATA,2026-02-16T10:00:00Z,Seed shared template
            """)
        _write(ctx, f"{base_path}/schema/dm_header.schema.yaml", """\
            $schema: "http://json-schema.org/draft-07/schema#"
            title: "Common DM Header Metadata"
            type: object
            required:
              - dm_id
              - title
              - type
              - language
              - applicability
            properties:
              dm_id:
                type: string
                pattern: "^DM-[A-Z0-9\\-]+$"
              title:
                type: string
              type:
                type: string
                enum: ["TEMPLATE", "FRAGMENT", "MODULE", "REFERENCE"]
              language:
                type: string
                pattern: "^[A-Z]{2}$"
              applicability:
                type: string
              version:
                type: string
              owner_aor:
                type: ["string", "null"]
              tags:
                type: array
                items: { type: string }
            """)
        _write(ctx, f"{base_path}/schema/dm_trace.schema.yaml", """\
            $schema: "http://json-schema.org/draft-07/schema#"
            title: "DM Traceability Schema"
            type: object
            required:
              - dm_id
              - source_type
              - source_ref
            properties:
              dm_id:
                type: string
              source_type:
                type: string
                enum: ["SSOT", "CSDB_REF", "COMMON_CSDB"]
              source_ref:
                type: string
              derived_utc:
                type: string
                format: date-time
            """)
        _write(ctx, f"{base_path}/templates/DM-TEMPLATE-COMMON-0001.md", """\
            # DM-TEMPLATE-COMMON-0001: Common DM Skeleton

            This is a seed template for common data modules.

            ## Content Structure
            - Introduction
            - Procedure/Description
            - References
            - Warnings/Cautions/Notes

            ---

            **GenKISS**: General Knowledge and Information Standard Systems
            """)
        _write(ctx, f"{base_path}/templates/DM-TEMPLATE-COMMON-0001.meta.yaml", """\
            dm_id: DM-TEMPLATE-COMMON-0001
            title: Common DM Skeleton
            type: TEMPLATE
            language: EN
            applicability: ALL
            version: 1.0.0
            owner_aor: STK_DATA
            tags: [template, common, seed]
            source_type: SSOT
            source_ref: KNU-00-00-005-LC02-GenKISS-SYS_REQ
            """)
    
    elif dir_name == "PM":
        _write(ctx, f"{base_path}/.gitkeep", "")
        _write(ctx, f"{base_path}/README.md", f"""\
            # COMMON_CSDB / PM — Shared Publication Module Layer

            This directory contains reusable, product-agnostic Publication Module (PM)
            assets for ATDP products (AMM, IPC, SRM, TSM, WDM, FIM, MMEL, MPD).

            ## Purpose
            - Provide common PM assembly templates
            - Standardize module composition order
            - Preserve traceability to SSOT/CSDB_REF sources

            ## Rules
            1. Every PM asset must be registered in `pm_index.csv`.
            2. Every PM metadata file must include provenance and derived UTC.
            3. COMMON PM must not include product-exclusive payload.
            4. PMs can reference COMMON_CSDB/DM modules only through declared refs.

            ## Minimal naming convention
            - Content: `PM-<DOMAIN>-<CODE>.md`
            - Metadata: `PM-<DOMAIN>-<CODE>.meta.yaml`

            Example:
            - `PM-TEMPLATE-COMMON-0001.md`
            - `PM-TEMPLATE-COMMON-0001.meta.yaml`

            ---

            **GenKISS**: General Knowledge and Information Standard Systems
            """)
        _write(ctx, f"{base_path}/pm_index.csv", """\
            PM_ID,Title,Type,Language,Applicability,Source_Type,Source_Ref,Status,Owner_AoR,Last_Updated_UTC,Notes
            PM-TEMPLATE-COMMON-0001,Common PM Skeleton,TEMPLATE,EN,ALL,SSOT,KNU-00-00-005-LC02-GenKISS-SYS_REQ,ACTIVE,STK_DATA,2026-02-16T10:00:00Z,Seed shared publication module template
            """)
        _write(ctx, f"{base_path}/schema/pm_header.schema.yaml", """\
            $schema: "http://json-schema.org/draft-07/schema#"
            title: "Common PM Header Metadata"
            type: object
            required:
              - pm_id
              - title
              - type
              - language
              - applicability
            properties:
              pm_id:
                type: string
                pattern: "^PM-[A-Z0-9\\-]+$"
              title:
                type: string
              type:
                type: string
                enum: ["TEMPLATE", "ASSEMBLY", "REFERENCE"]
              language:
                type: string
                pattern: "^[A-Z]{2}$"
              applicability:
                type: string
              version:
                type: string
              owner_aor:
                type: ["string", "null"]
              tags:
                type: array
                items: { type: string }
            """)
        _write(ctx, f"{base_path}/schema/pm_trace.schema.yaml", """\
            $schema: "http://json-schema.org/draft-07/schema#"
            title: "PM Traceability Schema"
            type: object
            required:
              - pm_id
              - source_type
              - source_ref
            properties:
              pm_id:
                type: string
              source_type:
                type: string
                enum: ["SSOT", "CSDB_REF", "COMMON_CSDB"]
              source_ref:
                type: string
              derived_utc:
                type: string
                format: date-time
            """)
        _write(ctx, f"{base_path}/templates/PM-TEMPLATE-COMMON-0001.md", """\
            # PM-TEMPLATE-COMMON-0001: Common PM Skeleton

            This is a seed template for common publication modules.

            ## Composition Structure
            - Title Page
            - Table of Contents
            - Referenced DM Modules
            - Appendices

            ---

            **GenKISS**: General Knowledge and Information Standard Systems
            """)
        _write(ctx, f"{base_path}/templates/PM-TEMPLATE-COMMON-0001.meta.yaml", """\
            pm_id: PM-TEMPLATE-COMMON-0001
            title: Common PM Skeleton
            type: TEMPLATE
            language: EN
            applicability: ALL
            version: 1.0.0
            owner_aor: STK_DATA
            tags: [template, common, seed]
            source_type: SSOT
            source_ref: KNU-00-00-005-LC02-GenKISS-SYS_REQ
            """)
    else:
        _write(ctx, f"{base_path}/.gitkeep", "")


def _gen_product_structure(ctx: GenContext, product: str) -> None:
    """Generate comprehensive product-specific CSDB structure."""
    base_path = f"00-00-general/PUB/ATDP/PRODUCTS/{product}"
    
    _write(ctx, f"{base_path}/.gitkeep", "")
    _write(ctx, f"{base_path}/README.md", f"""\
        # ATDP / PRODUCTS / {product} — {_get_product_full_name(product)} Domain

        {product} product domain under `PUB/ATDP/PRODUCTS`.

        ## Scope
        This folder hosts {product}-specific publication assets and configuration.
        Shared reusable primitives must be consumed from:

        - `../../COMMON_CSDB/DM`
        - `../../COMMON_CSDB/PM`
        - `../../COMMON_CSDB/BREX`
        - `../../COMMON_CSDB/APPLICABILITY`
        - `../../COMMON_CSDB/COMMON`
        - `../../COMMON_CSDB/ICN`

        ## Governance
        - {product} content is publication-layer output and must trace to SSOT/CSDB_REF lineage.
        - No authority inversion: SSOT remains authoritative lifecycle source.
        - Product deltas must be explicit and versioned.

        ## Minimal Deliverables
        - {product} DM/PM seeds
        - DML seed
        - Applicability seed
        - Traceability lineage map
        - Export target configuration

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """)
    
    # Generate index
    _write(ctx, f"{base_path}/{product.lower()}_index.csv", f"""\
        Asset_ID,Asset_Type,Path,Status,Source_Type,Source_Ref,Last_Updated_UTC,Owner_AoR,Notes
        {product}-DM-INTRO-0001,DM,CSDB/DM/{product}-DM-INTRO-0001.md,DRAFT,COMMON_CSDB,DM-TEMPLATE-COMMON-0001,2026-02-16T10:00:00Z,STK_DATA,Seed {product} intro module
        {product}-PM-MAIN-0001,PM,CSDB/PM/{product}-PM-MAIN-0001.md,DRAFT,COMMON_CSDB,PM-TEMPLATE-COMMON-0001,2026-02-16T10:00:00Z,STK_DATA,Seed {product} main publication module
        """)
    
    # CONFIG subdirectories
    _write(ctx, f"{base_path}/CONFIG/effectivity.yaml", f"""\
        # {product} Effectivity Configuration
        applicability_rules:
          - rule_id: {product}-EFF-001
            description: Default applicability for {product}
            condition: ALL
        """)
    _write(ctx, f"{base_path}/CONFIG/publication_profile.yaml", f"""\
        # {product} Publication Profile
        product_code: {product}
        language: EN
        output_formats: [PDF, HTML, IETP]
        brex_reference: {product}-BREX-0001
        """)
    _write(ctx, f"{base_path}/CONFIG/export_targets.yaml", f"""\
        # {product} Export Targets
        targets:
          - target_id: {product}-EXPORT-PDF
            format: PDF
            output_path: ../EXPORT/PDF
          - target_id: {product}-EXPORT-HTML
            format: HTML
            output_path: ../EXPORT/HTML
          - target_id: {product}-EXPORT-IETP
            format: IETP_PACKAGE
            output_path: ../EXPORT/IETP_PACKAGE
        """)
    
    # CSDB subdirectories
    _write(ctx, f"{base_path}/CSDB/DM/.gitkeep", "")
    _write(ctx, f"{base_path}/CSDB/DM/README.md", f"# {product} Data Modules\n\nProduct-specific DM content for {product}.\n")
    _write(ctx, f"{base_path}/CSDB/DM/{product}-DM-INTRO-0001.md", f"""\
        # {product}-DM-INTRO-0001: {product} Introduction

        This is the introductory data module for {product}.

        ## Purpose
        Provides overview and scope of {product} documentation.

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """)
    
    _write(ctx, f"{base_path}/CSDB/PM/.gitkeep", "")
    _write(ctx, f"{base_path}/CSDB/PM/README.md", f"# {product} Publication Modules\n\nProduct-specific PM content for {product}.\n")
    _write(ctx, f"{base_path}/CSDB/PM/{product}-PM-MAIN-0001.md", f"""\
        # {product}-PM-MAIN-0001: {product} Main Publication

        Main publication module for {product}.

        ## Referenced Modules
        - {product}-DM-INTRO-0001

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """)
    
    _write(ctx, f"{base_path}/CSDB/DML/.gitkeep", "")
    _write(ctx, f"{base_path}/CSDB/DML/{product}-DML-0001.csv", f"""\
        DML_Entry_ID,DM_ID,PM_ID,Sequence,Status
        {product}-DML-E001,{product}-DM-INTRO-0001,{product}-PM-MAIN-0001,1,ACTIVE
        """)
    
    _write(ctx, f"{base_path}/CSDB/BREX/.gitkeep", "")
    _write(ctx, f"{base_path}/CSDB/BREX/{product}-BREX-0001.md", f"""\
        # {product}-BREX-0001: {product} Business Rules

        Business rules and validation constraints for {product}.

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """)
    
    _write(ctx, f"{base_path}/CSDB/ICN/.gitkeep", "")
    _write(ctx, f"{base_path}/CSDB/COMMON/.gitkeep", "")
    
    _write(ctx, f"{base_path}/CSDB/APPLICABILITY/.gitkeep", "")
    _write(ctx, f"{base_path}/CSDB/APPLICABILITY/{product}-ACT-0001.yaml", f"""\
        # {product} Applicability Table
        act_id: {product}-ACT-0001
        rules:
          - rule_id: {product}-APP-001
            description: Default applicability
            condition: ALL
        """)
    
    # TRACE subdirectories
    _write(ctx, f"{base_path}/TRACE/lineage.yaml", f"""\
        # {product} Lineage Tracking
        product: {product}
        ssot_sources:
          - LC02_SYSTEM_REQUIREMENTS
          - LC04_DESIGN_DEFINITION
        csdb_ref_sources:
          - NU/*
        """)
    _write(ctx, f"{base_path}/TRACE/compliance_map.csv", f"""\
        Requirement_ID,Source_LC,Target_DM,Compliance_Status,Verification_Method
        REQ-{product}-001,LC02,{product}-DM-INTRO-0001,PENDING,REVIEW
        """)
    
    # EXPORT subdirectories
    _write(ctx, f"{base_path}/EXPORT/.gitkeep", "")
    _write(ctx, f"{base_path}/EXPORT/PDF/.gitkeep", "")
    _write(ctx, f"{base_path}/EXPORT/HTML/.gitkeep", "")
    _write(ctx, f"{base_path}/EXPORT/IETP_PACKAGE/.gitkeep", "")


def _get_product_full_name(product: str) -> str:
    """Get full name for product code."""
    names = {
        "AMM": "Aircraft Maintenance Manual",
        "IPC": "Illustrated Parts Catalog",
        "SRM": "Structural Repair Manual",
        "CMM": "Component Maintenance Manual",
    }
    return names.get(product, product)


def _gen_atdp_readme(ctx: GenContext) -> None:
    """Generate enhanced PUB/ATDP README."""
    _write(ctx, "00-00-general/PUB/ATDP/README.md", """\
        # PUB / ATDP — Aircraft Technical Data Product Umbrella

        ATDP is the canonical publication umbrella for aircraft technical data products in the GenKISS scaffold.  
        Within ATDP, **CSDB is shared infrastructure** (COMMON_CSDB), and each product domain (AMM, IPC, SRM, CMM, etc.) provides product-specific deltas under `PRODUCTS/`.

        ---

        ## 1) Mission

        Provide a governed publication surface that:

        - Reuses shared CSDB primitives across products
        - Preserves product-specific specialization without duplicating common assets
        - Maintains strict lineage to SSOT and CSDB_REF
        - Supports deterministic export and IETP packaging flows

        ---

        ## 2) Canonical Structure

        ```text
        PUB/ATDP/
        ├── README.md
        ├── COMMON_CSDB/
        │   ├── README.md
        │   ├── DM/
        │   ├── PM/
        │   ├── DML/
        │   ├── BREX/
        │   ├── ICN/
        │   ├── COMMON/
        │   └── APPLICABILITY/
        ├── PRODUCTS/
        │   ├── AMM/
        │   ├── IPC/
        │   ├── SRM/
        │   ├── CMM/
        │   └── ...
        ├── EXPORT/
        │   ├── .gitkeep
        │   ├── PDF/
        │   ├── HTML/
        │   └── IETP_PACKAGE/
        └── IETP/
            └── .gitkeep
        ```

        ---

        ## 3) Governance Boundaries

        ### 3.1 Authority Model
        - SSOT remains the authoritative lifecycle source.
        - CSDB_REF provides atomic reference units derived from SSOT.
        - PUB/ATDP is delivery-oriented and must never become an upstream authority.

        ### 3.2 Non-Inversion Rule

        No product folder in `PUB/ATDP/PRODUCTS/*` may redefine lifecycle truth or bypass SSOT provenance.

        ### 3.3 Delta Rule

        Product directories contain only:
        - product-specific content,
        - product-specific applicability/configuration,
        - product-specific trace mappings.

        Shared templates and primitives belong in COMMON_CSDB.

        ---

        ## 4) Product Domains

        A product domain (e.g., PRODUCTS/AMM) should include:
        - `CONFIG/` (effectivity, publication profile, export targets)
        - `CSDB/` (DM, PM, DML, BREX, APPLICABILITY, etc.)
        - `TRACE/` (lineage + compliance mapping)
        - `EXPORT/` (product-local export outputs if enabled)

        Each product must carry explicit lineage to:
        - `../../SSOT`
        - `../../CSDB_REF/NU`
        - `../../COMMON_CSDB`

        ---

        ## 5) Reuse Philosophy

        COMMON_CSDB hosts:
        - Generic warnings, cautions, notes
        - Standard procedures and checklists
        - Reusable illustrations and graphics
        - Business rules (BREX) for validation
        - Applicability logic templates

        Products consume and specialize, but do not duplicate.

        ---

        **GenKISS**: General Knowledge and Information Standard Systems
        """)


def gen_0090(ctx: GenContext, phases: Dict[str, Any], atdp_cfg: Dict[str, Any]) -> None:
    """Generate ATA 00-90 tables/index artifacts."""
    _write(ctx, "00-90-tables-schemas-index/README.md", "# ATA 00-90 — Tables, Schemas & Index\n")

    ordered_ids = phases.get("_ordered_lc_ids")
    if not isinstance(ordered_ids, list):
        ordered_ids = sorted([k for k in phases.keys() if k.startswith("LC")])

    lines = ["LC_ID,Phase_Type,Canonical_Name,Canonical_SSOT_Dir"]
    for lc_id in ordered_ids:
        if lc_id not in phases:
            continue
        s = phases[lc_id]
        lines.append(f"{lc_id},{s.get('phase_type','')},{s.get('canonical_name','')},{s.get('ssot_dir','')}")
    _write(
        ctx,
        "00-90-tables-schemas-index/tables/canonical_lifecycle_registry.csv",
        "\n".join(lines) + "\n",
    )

    products = atdp_cfg.get("products", [])
    p_lines = ["Product_Code,Uses_Common_CSDB"]
    for p in products:
        p_lines.append(f"{p},TRUE")
    _write(ctx, "00-90-tables-schemas-index/tables/atdp_products.csv", "\n".join(p_lines) + "\n")
