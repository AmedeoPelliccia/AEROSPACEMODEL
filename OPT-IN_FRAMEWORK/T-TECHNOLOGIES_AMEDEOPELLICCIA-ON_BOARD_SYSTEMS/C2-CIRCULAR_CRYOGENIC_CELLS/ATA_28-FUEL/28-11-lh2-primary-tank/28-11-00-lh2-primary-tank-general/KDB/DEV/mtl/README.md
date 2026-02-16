# Method Token Library (MTL) — ATA 28-11-00

**LH₂ Primary Tank — Circular Cryogenic Cells**

| Key | Value |
|-----|-------|
| Lifecycle Context | LC04 (Design Definition) → feeds LC05 (Parametric Models) |
| ATA Mapping | 28-11 LH₂ Primary Tank |
| Subject Token Pattern | `MTK-28-11-{DOMAIN}-{SEQ}` |
| Process Token Pattern | `MTP-28-11-{DOMAIN}-{SEQ}` |
| Procedure Token Pattern | `STP-28-11-{SEQ}` |
| Status | DEV (non-baselined) |

## Contents

| File | Description |
|------|-------------|
| `MTL-28-11-00_method_token_library.yaml` | Subject-level token library (19 tokens across 4 domains) |
| `MTL-28-11-00_method_token_library.md` | Human-readable companion |
| `MTL-28-11-00_process_methods.yaml` | Process and scaling method tokens (21 tokens across 5 domains) |
| `MTL-28-11-00_process_methods.md` | Human-readable companion |
| `STP-28-11-00_standard_procedures.yaml` | Standard Token Procedures — 5 composed procedures (40 token refs) |
| `STP-28-11-00_standard_procedures.md` | Human-readable companion |

## Three-Layer Token Architecture

The MTL has three layers.  Each layer builds on the previous one,
and a model can consume tokens at any layer:

1. **Subject tokens** (`MTK-*`): tokenise every subject title from trade
   studies, compliance matrices, evaluation criteria, and special conditions
   into a flat namespace of deterministic method identifiers.

2. **Process/scaling tokens** (`MTP-*`): extract the actual industry
   processes (closed-form analytical methods) and scaling relationships
   (empirical correlations where no inference boundary exists) embedded
   in every YAML file.

3. **Standard Token Procedures** (`STP-*`): compose subject and process
   tokens into end-to-end standard procedures.  A model consuming one
   STP token receives the full procedure — inputs, sequenced steps,
   intermediate hand-offs, terminal outputs, and acceptance gates —
   enabling a complete standard procedure in a single token call.

Each token defines `method_class`, `inputs`, and `outputs` for model
programming and can be referenced by parametric models, scoring
pipelines, and test matrices.

## Governance

This MTL resides in `KDB/DEV/mtl/` and is **not baselined**.
Promotion to `KDB/LM/SSOT/` requires:

- BREX validation
- Trace coverage verification
- STK_ENG approval
- ECR submission via `GOVERNANCE/CHANGE_CONTROL/`
