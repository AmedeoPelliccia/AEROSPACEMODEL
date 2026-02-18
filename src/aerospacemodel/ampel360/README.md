# AMPEL360 Q100 Module

Python implementation of the AMPEL360 Q100 controlled vocabulary and identifier grammar per CV-003 specification.

## Overview

This module provides utilities for working with AMPEL360 Q100 artifacts, including:

- **Canonical Identifier Grammar**: Create, parse, and validate artifact identifiers
- **PBS/WBS Linkage**: Product and Work Breakdown Structure management
- **Metadata Records**: Schema-based metadata validation (JSON Schema)
- **Artifact Types**: 63 controlled artifact types across 14 lifecycle phases

## Installation

```bash
pip install -e .
```

## Quick Start

### Artifact Identifiers

```python
from aerospacemodel.ampel360 import ArtifactID, IDFormat, parse_identifier

# Create an identifier
artifact_id = ArtifactID(
    msn="MSN001",
    ata_chapter="28",
    section="10",
    subject="00",
    lc_phase="LC02",
    artifact_type="REQ",
    sequence="001"
)

# Generate different formats
print(artifact_id.to_compact())      # AMPEL360_Q100_MSN001_ATA28-10-00_LC02_REQ_001
print(artifact_id.to_hyphenated())   # AMPEL360-Q100-MSN001-ATA28-10-00-LC02-REQ-001
print(artifact_id.to_urn())          # urn:ampel360:q100:msn001:ata28-10-00:lc02:req:001

# Parse an existing identifier
parsed = parse_identifier("AMPEL360_Q100_MSN001_ATA28-10-00_LC02_REQ_001")
print(parsed.get_phase_type())       # PhaseType.PLM
print(parsed.get_ssot_root())        # KDB/LM/SSOT/PLM
```

### PBS/WBS Structures

```python
from aerospacemodel.ampel360 import create_pbs_id, create_wbs_id, parse_pbs

# Create PBS identifier (Product Breakdown Structure)
pbs_id = create_pbs_id(
    axis="T",
    subdomain="C2",
    ata_chapter="28",
    section="10",
    subject="00",
    item_name="CRYO_TANK_FWD"
)
print(pbs_id)  # PBS-TC2-ATA28-10-00-CRYO_TANK_FWD

# Parse and check for novel technology
pbs = parse_pbs(pbs_id)
print(pbs.is_novel_technology())  # True (C2 is Novel Technology ⭐)

# Create WBS identifier (Work Breakdown Structure)
wbs_id = create_wbs_id(lc_phase="LC02", hierarchy="1.2.3")
print(wbs_id)  # WBS-REQ-1.2.3
```

### Auto-Sequencing

```python
from aerospacemodel.ampel360 import IDGenerator

generator = IDGenerator()

# Generate with auto-sequencing
req1 = generator.generate(
    msn="MSN001",
    ata_chapter="28",
    section="10",
    subject="00",
    lc_phase="LC02",
    artifact_type="REQ"
)
print(req1)  # AMPEL360_Q100_MSN001_ATA28-10-00_LC02_REQ_001

req2 = generator.generate(
    msn="MSN001",
    ata_chapter="28",
    section="10",
    subject="00",
    lc_phase="LC02",
    artifact_type="REQ"
)
print(req2)  # AMPEL360_Q100_MSN001_ATA28-10-00_LC02_REQ_002 (auto-incremented)
```

## Identifier Grammar

### Format

```
AMPEL360-Q100-MSN{nnn}-ATA{cc}-{ss}-{ss}-LC{nn}-{Type}-{Seq}
│         │      │        │      │    │     │       │       │
│         │      │        │      │    │     │       │       └─ Sequence (001–999)
│         │      │        │      │    │     │       └─ Artifact type code
│         │      │        │      │    │     └─ Lifecycle phase (LC01–LC14)
│         │      │        │      │    └─ Sub-subject (00–99)
│         │      │        │      └─ Subject (00–99)
│         │      │        └─ ATA chapter (00–98, IN)
│         │      └─ Manufacturer Serial Number (001–999)
│         └─ Model designation
└─ Aircraft program
```

### Supported Formats

1. **Compact**: `AMPEL360_Q100_MSN001_ATA25-10-00_LC02_REQ_001`
2. **Hyphenated**: `AMPEL360-Q100-MSN001-ATA25-10-00-LC02-REQ-001`
3. **URN**: `urn:ampel360:q100:msn001:ata25-10-00:lc02:req:001`

## OPT-IN Framework

### 5 Domains, 25 Sub-Domains

| Domain | Sub-Domain | Code | Novel | Description |
|--------|-----------|------|-------|-------------|
| **O** Organizations | Authoritative | A | — | Regulatory, legal requirements |
| **O** Organizations | Business Enforcement | B | — | Business policies |
| **P** Programs | Product Definition | P | — | Dimensions, weight, markings |
| **P** Programs | Service Instruction | S | — | Lifting, towing, servicing |
| **T** Technologies | Cryogenic Cells | C2 | ⭐ | H₂ cryogenic fuel systems |
| **T** Technologies | Intelligence | I2 | ⭐ | AI/ML models |
| **T** Technologies | Propulsion | P | ⭐ | H₂ powerplant, fuel cells |
| **T** Technologies | *(13 others)* | ... | — | Standard systems |
| **I** Infrastructures | Manufacturing | M1 | — | Production facilities |
| **I** Infrastructures | Maintenance | M2 | — | Hangars, shops |
| **I** Infrastructures | Operations | O | — | Ground services |
| **N** Neural Networks | Digital Thread | D | — | Traceability, ledger |
| **N** Neural Networks | AI Governance | A | — | Ethics, explainability |
| **N** Neural Networks | Reserved | P* | — | Future expansion |

⭐ **Novel Technology** = Full LC01–LC14 lifecycle activation required

## Lifecycle Phases (TLI v2.1)

### PLM Phases (LC01–LC10)
- **LC01**: Problem Statement → **LC02**: System Requirements (FBL)
- **LC03**: Safety & Reliability → **LC04**: Design Definition (DBL)
- **LC05**: Analysis Models → **LC06**: Integration & Test
- **LC07**: QA & Process → **LC08**: Certification
- **LC09**: ESG & Sustainability → **LC10**: Industrial & Supply (PBL)

### OPS Phases (LC11–LC14)
- **LC11**: Operations Customization → **LC12**: Continued Airworthiness & MRO
- **LC13**: Maintenance Source Data → **LC14**: End of Life

## Artifact Types

63 controlled artifact types across all phases:

- **LC01** (7): KNOT, KNU, GOV, TKN, RACI, TML, AWD
- **LC02** (5): REQ, REQ-TRC, ICD, DATA, CMP-I
- **LC03** (3): SAF, REL, HAZ
- **LC04** (4): DES, DWG, CFG, IFC
- **LC05** (4): ANA, TRD, MDL, SIM-V
- **LC06** (4): TPR, TRS, INT, CNF
- **LC07** (3): QAR, PRC, ACC
- **LC08** (3): CBA, CMP, FTR
- **LC09** (3): ESG, LCA, ENC
- **LC10** (3): IND, SUP, QPR
- **LC11** (3): CDL, OCF, RLN
- **LC12** (6): SBL, RPR, QRY, AOG, COC, CMP-O
- **LC13** (6): MSR, MSR-E, RSR, RSR-E, OSR, OSR-E
- **LC14** (4): DSM, MRC, DPC, EEL
- **PUB** (5): DM, PM, DML, ICN, BREX

See `schemas/ampel360_artifact_types.yaml` for complete definitions.

## Validation Rules

1. **ID Uniqueness**: Every `record_id` globally unique
2. **ATA Chapter Range**: `00–98` or `IN`
3. **LC Phase**: `LC01–LC14` per TLI v2.1
4. **Phase Type**: LC01–LC10 → PLM; LC11–LC14 → OPS
5. **Sub-Domain Consistency**: Valid for declared axis
6. **Novel Technology**: If true, full LC01–LC14 must be activated
7. **Baseline Exclusivity**: FBL→LC02; DBL→LC04; PBL→LC10
8. **Certification Continuity**: LC12/LC13 must trace back through LC08→LC10

## API Reference

### Classes

- **`ArtifactID`**: Canonical artifact identifier
- **`PBSID`**: Product Breakdown Structure identifier
- **`WBSID`**: Work Breakdown Structure identifier
- **`IDParser`**: Parse identifiers from strings
- **`IDGenerator`**: Generate identifiers with auto-sequencing
- **`PBSWBSLinker`**: Link PBS and WBS structures

### Enums

- **`IDFormat`**: `COMPACT`, `HYPHENATED`, `URN`
- **`PhaseType`**: `PLM`, `OPS`
- **`OPTINAxis`**: `O`, `P`, `T`, `I`, `N`

### Constants

- **`WBS_PHASE_CODES`**: Mapping of LC phases to WBS codes
- **`SUBDOMAIN_CODES`**: Valid sub-domains per axis
- **`NOVEL_TECHNOLOGY_SUBDOMAINS`**: C2, I2, P

## Testing

```bash
# Run all tests
pytest tests/test_ampel360_*.py -v

# Run specific test module
pytest tests/test_ampel360_identifiers.py -v
pytest tests/test_ampel360_pbs_wbs.py -v
```

## Documentation

- **Specification**: `docs/specifications/AMPEL360_CV_003_CONTROLLED_VOCABULARY.md`
- **Artifact Types**: `schemas/ampel360_artifact_types.yaml`
- **Metadata Schema**: `schemas/ampel360_metadata_record.schema.json`

## Related Documents

| Document | Path |
|----------|------|
| CV-003 Specification | `docs/specifications/AMPEL360_CV_003_CONTROLLED_VOCABULARY.md` |
| TLI v2.1 Registry | `lifecycle/LC_PHASE_REGISTRY.yaml` |
| OPT-IN Framework | `OPT-IN_FRAMEWORK/00_INDEX.md` |
| T-Subdomain Activation | `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml` |

## License

CC0-1.0 (Public Domain Dedication)

## Author

ASIT (Aircraft Systems Information Transponder)  
Document: AMPEL360-CV-003 v3.0  
Date: 2026-02-18
