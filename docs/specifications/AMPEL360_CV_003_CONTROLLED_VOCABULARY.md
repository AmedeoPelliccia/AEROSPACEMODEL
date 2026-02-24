# AMPEL360 Q100 — Controlled Vocabulary & Identifier Grammar

**Document ID:** AMPEL360-CV-003  
**Revision:** 3.0  
**Date:** 2026-02-18  
**Status:** ACTIVE  
**Scope:** Artifact IDs, PBS/WBS Linkage, Metadata Record Schema  
**Aligned to:** TLI v2.1 Canonical Lifecycle Phase Registry + OPT-IN Framework Index v3  
**Authority:** ASIT (Aircraft Systems Information Transponder)

---

## 1. Purpose

This document defines the **canonical identifier grammar** for all engineering and publication artifacts within the AMPEL360 Q100/Q10 program. It ensures every record is traceable from aircraft-level down to sub-subject deliverables and maps into the OPT-IN Framework's 7-axis / 33-subdomain structure.

**Normative references:**
- **TLI v2.1** — Canonical lifecycle phase definitions, packages, baselines, gates (L1 authority)
- **OPT-IN Framework Index v4** — Domain/sub-domain topology, ATA chapter mapping, novel technology designations

---

## 2. Precedence Model (L0–L8)

Per TLI v2.1:

| Layer | Name | Authority |
|-------|------|-----------|
| L0 | Program Governance | Immutable |
| L1 | LC Canonical Contract | ASIT |
| L2 | Domain Pack | Domain Steward |
| L3 | Config Context | Configuration Manager |
| L4 | Data Contracts | Contract Owner |
| L5 | Generation Workflow | GenLM Agent |
| L6 | Assurance Gates | Quality Assurance |
| L7 | Human Authority | Subject Matter Expert |
| L8 | OPS Feedback Loop | Operations |

This vocabulary operates at **L2/L4**. The scaffold generator operates at **L5**.

---

## 3. OPT-IN Domain & Sub-Domain Topology

### 3.1 Complete Structure (7 Domains, 33 Sub-Domains)

| Domain | Sub-Domain | Code | ATA Chapters | Type | Description |
|--------|-----------|------|--------------|------|-------------|
| **O** Organizations | Authoritative | **A** | 001, 002, 018 | — | Agency, regulatory, legal-derived requirements |
| **O** Organizations | Business Enforcement | **B** | 003, 004, 012 | — | Operator business policies and enforcement |
| **P** Programs | Product Definition | **P** | 000, 006, 008, 011 | — | What the product is — dimensions, weight, markings |
| **P** Programs | Service Instruction | **S** | 005, 007, 009, 010 | — | How you handle it — lifting, towing, servicing |
| **R** Reserved | Reserved | **R** | 014–016, 019 | — | Reserved for future programme allocation (excl. 013, 017) |
| **T** Technologies | Airframe & Cabins | **A** | 020, 025, 044, 050–057 | Standard | Structures, furnishings, doors, windows, wings |
| **T** Technologies | Mechanics | **M** | 027, 029, 032 | Standard | Flight controls, hydraulics, landing gear |
| **T** Technologies | Environment | **E1** | 021, 026, 030, 035–038, 047 | Standard | ECS, fire, ice/rain, oxygen, pneumatic, water |
| **T** Technologies | Data | **D** | 031, 045 | Standard | Indicating/recording, CMS |
| **T** Technologies | Information | **I** | 046 | Standard | Information systems |
| **T** Technologies | Energy | **E2** | 024, 049 | Standard | Electrical power, APU |
| **T** Technologies | Electrics | **E3** | 033, 039 | Standard | Lights, panels/components |
| **T** Technologies | Logics | **L1** | *(reserved)* | Future | Reserved for future systems |
| **T** Technologies | Links | **L2** | 034 | Standard | Navigation |
| **T** Technologies | Comms | **C1** | 023 | Standard | Communications |
| **T** Technologies | Cryogenic Cells | **C2** | 028 | ⭐ Novel | H₂ cryogenic fuel storage and distribution |
| **T** Technologies | Intelligence | **I2** | 095, 097 | ⭐ Novel | AI/ML models, synthetic data validation |
| **T** Technologies | Avionics | **A2** | 022, 042 | Standard | Auto flight, IMA |
| **T** Technologies | Operating Systems | **O** | 040 | Standard | Multisystem |
| **T** Technologies | Propulsion | **P** | 060–061, 071–079 | ⭐ Novel | H₂ powerplant, fuel cells, engine systems |
| **I** Infrastructures | Manufacturing Facilities | **M1** | 080–083 | — | Production lines, test rigs, assembly benches |
| **I** Infrastructures | Maintenance Environments | **M2** | 084–086 | — | In-line, hangars, shops |
| **I** Infrastructures | Operations & Service Structures | **O** | 087–089 | — | Airport facilities, fuel logistics, ground services |
| **N** Neural Networks | Digital Thread & Traceability | **D** | 090–093 | — | Ledger, DPP, hash chain, identifiers, audit packs |
| **N** Neural Networks | AI Governance & Assurance | **A** | 094, 096 | — | Certification pathway, ethics, human authority, explainability |
| **N** Neural Networks | Program Reserved | **P*** | 098–099 | — | Expansion slot for future systems |
| **S** SimTest & Digital Twin | Geometry & Mesh | **G** | 100–102 | — | CAD geometry, mesh generation, outer mold-line |
| **S** SimTest & Digital Twin | CFD / FEM Simulation | **X** | 103–105 | — | Computational fluid dynamics and finite element models |
| **S** SimTest & Digital Twin | Thermal Simulation | **T** | 106–108 | — | Thermal analysis models and heat transfer |
| **S** SimTest & Digital Twin | Validation | **V** | 109–111 | — | Model validation against test data |
| **S** SimTest & Digital Twin | Functional Simulation | **F** | 112, 114–116 | — | System-level functional and mission simulations |
| **S** SimTest & Digital Twin | UQ — Uncertainty Quantification | **U** | 118–123 | — | Monte Carlo, surrogate models, sensitivity analysis |
| **S** SimTest & Digital Twin | Extended Reality (XR/AR/VR) | **R** | 124 | — | AR/VR/MR training, XR cockpit, immersive digital twin |

> **ATA chapter range:** 000–124 (3-digit zero-padded). Chapters 013, 017, 113, 117 permanently excluded (X13/X17 cultural exclusion policy). See `OPT-IN_FRAMEWORK/AMPEL360-OPTIN-CULTURAL-EXCLUSION-001.yaml`.
> 
> **Backward compat:** Legacy 2-digit chapter codes (ATA 00–98) are zero-padded to 3 digits automatically by the identifier module. e.g. "25" → "025".

### 3.2 Novel Technology Designation (⭐)

Sub-domains marked ⭐ Novel Technology require **full LC01–LC14 lifecycle activation** with special conditions. This applies to:

| Sub-Domain | Rationale |
|-----------|-----------|
| T/C2 (Cryogenic Cells) | First-of-type H₂ cryogenic fuel system — no certification precedent |
| T/I2 (Intelligence) | AI/ML in airborne systems — DO-178C AI supplement pathway |
| T/P (Propulsion) | H₂-electric hybrid powerplant — novel type design |

All other sub-domains follow standard lifecycle activation per domain steward discretion.

### 3.3 ENGINEERING_SSOT Front-End

| Domain | Path | Scope |
|--------|------|-------|
| **ENGINEERING_SSOT** | `ENGINEERING_SSOT/` | Front-end for posting completed SSOT & Custom Information Data Sheets |

ENGINEERING_SSOT is a **publication surface**, not a lifecycle domain. Artifacts originate in SSOT (PLM/OPS) and are posted to ENGINEERING_SSOT once approved.

---

## 4. Identifier Hierarchy

```
AMPEL360-{MODEL}-MSN{nnn}-ATA{ccc}-{ss}-{ss}-LC{nn}-{ArtifactType}-{Seq}
│         │       │        │        │    │     │       │             │
│         │       │        │        │    │     │       │             └─ Sequence (001–999)
│         │       │        │        │    │     │       └─ Artifact type code
│         │       │        │        │    │     └─ Lifecycle phase (LC01–LC14)
│         │       │        │        │    └─ Sub-subject (00–99)
│         │       │        │        └─ Subject (00–99)
│         │       │        └─ ATA chapter (000–124, excl. X13/X17, or IN/infra suffix)
│         │       └─ Manufacturer Serial Number (001–999)
│         └─ Model designation (Q100 = AIR-T, Q10 = SPACE-T)
└─ Aircraft/Spacecraft program
```

### 4.1 Compact Form

```
AMPEL360_Q100_MSN001_ATA025-10-00_LC02_REQ_001
```

### 4.2 URN Form

```
urn:ampel360:q100:msn001:ata025-10-00:lc02:req:001
```

---

## 5. TLI v2.1 Canonical Lifecycle Phases

### 5.1 PLM Phases (LC01–LC10) — Root: `KDB/LM/SSOT/PLM/`

| Phase | Canonical Name | SSOT Directory | Baseline | Gate ID |
|-------|---------------|----------------|----------|---------|
| LC01 | Problem Statement | `LC01_PROBLEM_STATEMENT` | — | G-LC01-ENTRY |
| LC02 | System Requirements | `LC02_SYSTEM_REQUIREMENTS` | **FBL** | G-LC02-FBL |
| LC03 | Safety & Reliability | `LC03_SAFETY_RELIABILITY` | — | G-LC03-SAFETY |
| LC04 | Design Definition | `LC04_DESIGN_DEFINITION` | **DBL** | G-LC04-DBL |
| LC05 | Analysis Models | `LC05_ANALYSIS_MODELS` | — | G-LC05-ANALYSIS |
| LC06 | Integration & Test | `LC06_VERIFICATION` | — | G-LC06-CONFORMITY |
| LC07 | QA & Process Compliance | `LC07_QA_PROCESS` | — | G-LC07-QA |
| LC08 | Certification | `LC08_CERTIFICATION` | — | G-LC08-CERT |
| LC09 | ESG & Sustainability | `LC09_ESG_SUSTAINABILITY` | — | G-LC09-ESG |
| LC10 | Industrial & Supply Chain | `LC10_INDUSTRIAL_SUPPLY` | **PBL** | G-LC10-PBL |

### 5.2 OPS Phases (LC11–LC14) — Root: `IDB/OPS/LM/`

| Phase | Canonical Name | SSOT Directory | Gate ID |
|-------|---------------|----------------|---------|
| LC11 | Operations Customization | `LC11_OPERATIONS_CUSTOMIZATION` | G-LC11-OPS |
| LC12 | Continued Airworthiness & MRO | `LC12_MAINTENANCE_REPAIR` | G-LC12-MRO |
| LC13 | Maintenance Source Data | `LC13_MAINTENANCE_SOURCE` | G-LC13-SOURCE |
| LC14 | End of Life | `LC14_END_OF_LIFE` | G-LC14-EOL |

### 5.3 Baseline Model

| Baseline | Producer | Authority | Exclusivity |
|----------|---------|-----------|-------------|
| **FBL** | LC02 | Systems Engineering | Sole producer |
| **DBL** | LC04 | Design Engineering | Sole producer |
| **PBL** | LC10 | Manufacturing Engineering | Sole producer |

---

## 6. Artifact Type Codes (Package-Derived)

### 6.1 Summary by Phase

| Phase | # Types | Key Types |
|-------|---------|-----------|
| LC01 | 7 | KNOT, KNU, GOV, TKN, RACI, TML, AWD |
| LC02 | 5 | REQ, REQ-TRC, ICD, DATA, CMP-I |
| LC03 | 3 | SAF, REL, HAZ |
| LC04 | 4 | DES, DWG, CFG, IFC |
| LC05 | 4 | ANA, TRD, MDL, SIM-V |
| LC06 | 4 | TPR, TRS, INT, CNF |
| LC07 | 3 | QAR, PRC, ACC |
| LC08 | 3 | CBA, CMP, FTR |
| LC09 | 3 | ESG, LCA, ENC |
| LC10 | 3 | IND, SUP, QPR |
| LC11 | 3 | CDL, OCF, RLN |
| LC12 | 6 | SBL, RPR, QRY, AOG, COC, CMP-O |
| LC13 | 6 | MSR, MSR-E, RSR, RSR-E, OSR, OSR-E |
| LC14 | 4 | DSM, MRC, DPC, EEL |
| PUB | 5 | DM, PM, DML, ICN, BREX |
| **Total** | **63** | |

### 6.2 Complete Artifact Type Registry

See `schemas/ampel360_artifact_types.yaml` for full definitions.

---

## 7. PBS/WBS Linkage Schema

### 7.1 PBS Grammar (updated with sub-domain)

```
PBS-{AXIS}{SUBDOM}-{ATA}-{SECTION}-{SUBJECT}-{ITEM}

Examples:
  PBS-TA-ATA25-10-00-SEAT_ASSY        (T/Airframe, flight compartment seat)
  PBS-TC2-ATA28-10-00-CRYO_TANK_FWD   (T/Cryogenic, forward cryo tank)
  PBS-IM1-ATA85-10-00-TEST_RIG_FCS    (I/Manufacturing, fuel cell test rig)
  PBS-IO-ATAIN-50-00-GSE_COUPLER      (I/Ops&Service, H₂ GSE coupler)
  PBS-ND-ATA96-30-00-HASH_CHAIN       (N/Digital Thread, ledger hash chain)
  PBS-OA-ATA04-00-00-AL_LIMITS        (O/Authoritative, airworthiness limitations)
  PBS-PS-ATA12-10-00-SERVICE_REPL     (P/Service Instruction, replenishing)
```

### 7.2 WBS Phase Codes (TLI v2.1 Aligned)

| Code | Phase | TLI Canonical Name | Type |
|------|-------|--------------------|------|
| `PRB` | LC01 | Problem Statement | PLM |
| `REQ` | LC02 | System Requirements | PLM |
| `SAF` | LC03 | Safety & Reliability | PLM |
| `DES` | LC04 | Design Definition | PLM |
| `ANA` | LC05 | Analysis Models | PLM |
| `VER` | LC06 | Integration & Test | PLM |
| `QAP` | LC07 | QA & Process Compliance | PLM |
| `CRT` | LC08 | Certification | PLM |
| `ESG` | LC09 | ESG & Sustainability | PLM |
| `IND` | LC10 | Industrial & Supply Chain | PLM |
| `OPC` | LC11 | Operations Customization | OPS |
| `MRO` | LC12 | Continued Airworthiness & MRO | OPS |
| `MSD` | LC13 | Maintenance Source Data | OPS |
| `EOL` | LC14 | End of Life | OPS |
| `PUB` | — | Publication | Cross-cutting |

---

## 8. Metadata Record Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `record_id` | string | ✅ | Canonical artifact ID |
| `aircraft_id` | string | ✅ | `AMPEL360` |
| `model_id` | string | ✅ | `Q100` |
| `msn` | string | ✅ | `MSN001` |
| `ata_chapter` | string | ✅ | ATA chapter code |
| `ata_chapter_title` | string | ✅ | Human-readable chapter name |
| `section` | string | ✅ | Section code |
| `section_title` | string | ✅ | Human-readable section name |
| `subject` | string | ✅ | Subject code |
| `optin_axis` | string | ✅ | `O`, `P`, `T`, `I`, or `N` |
| `optin_subaxis` | string | ✅ | Sub-domain code (see §3.1) |
| `optin_subaxis_name` | string | ✅ | Sub-domain human name |
| `novel_technology` | boolean | ✅ | `true` for ⭐ Novel sub-domains |
| `phase_type` | string | ✅ | `PLM` or `OPS` |
| `lc_phase` | string | ✅ | Lifecycle phase code |
| `lc_canonical_name` | string | ✅ | TLI v2.1 canonical name |
| `package_origin` | string | ✅ | TLI package |
| `artifact_type` | string | ✅ | Controlled type code |
| `artifact_type_name` | string | ✅ | Descriptive type name |
| `artifact_title` | string | ✅ | Descriptive title |
| `pbs_id` | string | ○ | PBS node reference (§7.1 grammar) |
| `wbs_id` | string | ○ | WBS node reference |
| `trace_links` | array | ○ | Upstream/downstream artifact IDs |
| `knot_id` | string | ○ | Parent KNOT if applicable |
| `owner_aor` | string | ✅ | Area of Responsibility |
| `status` | string | ✅ | `PLANNED`/`DRAFT`/`REVIEW`/`APPROVED`/`SUPERSEDED`/`REJECTED` |
| `revision` | string | ✅ | Semantic version |
| `prepared_by` | string | ✅ | Author identifier |
| `date_created` | ISO date | ✅ | Creation timestamp |
| `date_modified` | ISO date | ✅ | Last modification timestamp |
| `ssot_root` | string | ✅ | `KDB/LM/SSOT/PLM` or `IDB/OPS/LM` |
| `ssot_dir` | string | ✅ | TLI canonical directory |
| `ssot_path` | string | ○ | Full computed SSOT path |
| `pub_path` | string | ○ | PUB tree path |
| `classification` | string | ✅ | `SSOT`, `PUB`, or `BOTH` |
| `baseline_ref` | string | ○ | `FBL`, `DBL`, or `PBL` |
| `gate_id` | string | ✅ | TLI gate identifier |
| `verification_method` | string | ○ | `Review`/`Inspection`/`Test`/`BREX+CI` |
| `certification_ref` | string | ○ | CS-25/Part 25 paragraph |
| `precedence_layer` | string | ○ | L0–L8 governing layer |

---

## 9. Validation Rules

1. **ID Uniqueness**: Every `record_id` globally unique
2. **ATA Chapter Range**: `00–98` or `IN`
3. **LC Phase**: `LC01–LC14` per TLI v2.1
4. **Canonical Name**: Must match TLI `canonical_name`
5. **Phase Type**: LC01–LC10 → `PLM`; LC11–LC14 → `OPS`
6. **SSOT Root**: PLM → `KDB/LM/SSOT/PLM`; OPS → `IDB/OPS/LM`
7. **Sub-Domain Consistency**: `optin_subaxis` must be valid for the declared `optin_axis`
8. **ATA-to-SubDomain**: ATA chapter must map to the declared sub-domain per §3.1
9. **Novel Technology**: If `novel_technology=true`, full LC01–LC14 must be activated
10. **Baseline Exclusivity**: FBL→LC02 only; DBL→LC04 only; PBL→LC10 only
11. **Certification Continuity**: LC12/LC13 must trace back through LC08→LC10
12. **Production Authority**: LC09 must NOT carry production release
13. **Safety-Critical**: LC03/LC06 cannot be omitted for cert-eligible systems
14. **Package Origin**: Must match TLI package for declared phase
15. **Gate Consistency**: `gate_id` must match TLI gate for declared phase

---

## 10. Implementation References

| Component | Location |
|-----------|----------|
| Identifier Module | `src/aerospacemodel/ampel360/identifiers.py` |
| Metadata Schema | `schemas/ampel360_metadata_record.schema.json` |
| Artifact Types | `schemas/ampel360_artifact_types.yaml` |
| PBS/WBS Module | `src/aerospacemodel/ampel360/pbs_wbs.py` |
| OPT-IN Registry | `OPT-IN_FRAMEWORK/00_INDEX.md` |
| TLI Registry | `lifecycle/LC_PHASE_REGISTRY.yaml` |

---

## 11. Coverage Summary

- **5** Top-Level Domains (O, P, T, I, N)
- **25** Sub-Domains (2 + 2 + 15 + 3 + 3)
- **66** ATA Chapter Directories
- **3** Novel Technology Designations (T/C2, T/I2, T/P)
- **14** Lifecycle Phases (10 PLM + 4 OPS)
- **63** Artifact Type Codes
- **3** Exclusive Baselines (FBL, DBL, PBL)
- **1** Front-End Publication Surface (ENGINEERING_SSOT)

---

## Appendix A: Change History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| 1.0 | 2025-12-01 | ASIT | Initial draft |
| 2.0 | 2026-01-15 | ASIT | Added Novel Technology designations |
| 3.0 | 2026-02-18 | ASIT | Complete 25-subdomain topology, artifact types, validation rules |

---

*End of Document*
