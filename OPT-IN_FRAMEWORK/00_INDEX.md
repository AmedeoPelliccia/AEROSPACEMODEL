# OPT-IN_FRAMEWORK Index

**AIRCRAFT/SPACECRAFT TLI v2.1 Canonical Architecture**

> **Controlled Vocabulary:** This structure is governed by [AMPEL360-CV-003](../docs/specifications/AMPEL360_CV_003_CONTROLLED_VOCABULARY.md)  
> **Identifier Grammar:** `AMPEL360_{MODEL}_MSN{nnn}_ATA{ccc}-{ss}-{ss}_LC{nn}_{TYPE}_{seq}`  
> **PBS Grammar:** `PBS-{AXIS}{SUBDOM}-{ATA}-{SECTION}-{SUBJECT}-{ITEM}`  
> **Chapter format:** 3-digit zero-padded (000–124)  
> **Chapter Master Table:** [CHAPTER_MASTER_TABLE.yaml](CHAPTER_MASTER_TABLE.yaml)

---

## Domain Structure

| Domain | Code | Path | ATA Scope | Description |
|--------|------|------|-----------|-------------|
| **O-ORGANIZATIONS** | O | `O-ORGANIZATIONS/` | ATA 001–004, 012, 018 | Organizational and governance documentation |
| **P-PROGRAMS** | P | `P-PROGRAMS/` | ATA 000, 005–011 | Program-level procedures and servicing |
| **R-RESERVED** | R | *(virtual)* | ATA 014–016, 019 | Reserved chapters for future programme allocation |
| **T-TECHNOLOGIES** | T | `T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/` | ATA 020–079, 095–097 | Complete on-board systems (15 subdomains) |
| **I-INFRASTRUCTURES** | I | `I-INFRASTRUCTURES/` | ATA 080–089 | Ground support and supply chain |
| **N-NEURAL_NETWORKS** | N | `N-NEURAL_NETWORKS/` | ATA 090–099 | AI governance and traceability |
| **S-SIMTEST_DIGITAL_TWIN** | S | *(new)* | ATA 100–124 excl. 113, 117 | Simulation, test, and digital twin (7 subdomains) |

---

## Technology Subdomains (T-TECHNOLOGIES)

| Subdomain | Code | ATA Chapters | Technology Type |
|-----------|------|--------------|-----------------|
| Airframe & Cabins | A | 020, 025, 044, 050–057 | Standard |
| Mechanics | M | 027, 029, 032 | Standard |
| Environment | E1 | 021, 026, 030, 035–038, 047 | Standard |
| Data | D | 031, 045 | Standard |
| Information | I | 046 | Standard |
| Energy | E2 | 024, 049 | Standard |
| Electrics | E3 | 033, 039 | Standard |
| Logics | L1 | Reserved | Future |
| Links | L2 | 034 | Standard |
| Comms | C1 | 023 | Standard |
| **Cryogenic Cells** | **C2** | **028** | **Novel Technology** ⭐ |
| **Intelligence** | **I2** | **095, 097** | **Novel Technology** ⭐ |
| Avionics | A2 | 022, 042 | Standard |
| Operating Systems | O | 040 | Standard |
| **Propulsion** | **P** | **060–061, 071–079** | **Novel Technology** ⭐ |

⭐ **Novel Technology** = Full LC01–LC14 lifecycle activation with Special Conditions

---

## Organization Subdomains (O-ORGANIZATIONS)

| Subdomain | Code | ATA Chapters | Description |
|-----------|------|--------------|-------------|
| Authoritative | **A** | 001, 002, 018 | Agency, regulatory, and legal-derived requirements |
| Business Enforcement | **B** | 003, 004, 012 | Operator business policies and enforcement |

---

## Program Subdomains (P-PROGRAMS)

| Subdomain | Code | ATA Chapters | Description |
|-----------|------|--------------|-------------|
| Product Definition | **P** | 000, 006, 008, 011 | What the product is — dimensions, weight, markings |
| Service Instruction | **S** | 005, 007, 009, 010 | How to handle it — lifting, towing, servicing |

---

## Reserved Subdomain (R-RESERVED)

| Subdomain | Code | ATA Chapters | Description |
|-----------|------|--------------|-------------|
| Reserved | **R** | 014–016, 019 | Reserved chapters for future programme allocation (X13/X17 exclusion removes 013, 017) |

---

## Infrastructure Subdomains (I-INFRASTRUCTURES)

| Subdomain | Code | Categories | Description |
|-----------|------|------------|-------------|
| Manufacturing Facilities | **M1** | ATA 080–083 | Production lines, test rigs, assembly benches |
| Maintenance Environments | **M2** | ATA 084–086 | In-line, hangars, shops |
| Operations & Service Structures | **O** | ATA 087–089 | Airport facilities, fuel logistics, ground services |

---

## Neural Network Subdomains (N-NEURAL_NETWORKS)

| Subdomain | Code | ATA / Scope | Description |
|-----------|------|-------------|-------------|
| Digital Thread & Traceability | **D** | ATA 090–093 | Ledger, DPP, hash chain, identifiers, schemas, audit packs |
| AI Governance & Assurance | **A** | ATA 094, 096 | Certification pathway, ethics, human authority protocols, explainability |
| Program Reserved | **P*** | ATA 098–099 | Expansion slot for future systems |

---

## SimTest & Digital Twin Subdomains (S-SIMTEST_DIGITAL_TWIN)

| Subdomain | Code | ATA Chapters | Description |
|-----------|------|--------------|-------------|
| Geometry & Mesh | **G** | 100–102 | CAD geometry, mesh generation, outer mold-line |
| CFD / FEM Simulation | **X** | 103–105 | Computational fluid dynamics and finite element models |
| Thermal Simulation | **T** | 106–108 | Thermal analysis models and heat transfer |
| Validation | **V** | 109–111 | Model validation against test data |
| Functional Simulation | **F** | 112, 114–116 | System-level functional and mission simulations |
| UQ — Uncertainty Quantification | **U** | 118–123 | Monte Carlo, surrogate models, sensitivity analysis |
| **Extended Reality (XR/AR/VR)** | **R** | **124** | AR/VR/MR training, XR cockpit, immersive digital twin |

> **X13/X17 Exclusion:** Chapters 113 and 117 are permanently excluded.  
> Content originally at 113 (UQ Platform) → **123**; at 117 (XR Governance) → **124**.  
> Cultural exclusion policy: [AMPEL360-OPTIN-CULTURAL-EXCLUSION-001.yaml](AMPEL360-OPTIN-CULTURAL-EXCLUSION-001.yaml)

---

## Quick Navigation

### Organizational & Governance
- [O-ORGANIZATIONS README](O-ORGANIZATIONS/README.md)

### Programs
- [P-PROGRAMS README](P-PROGRAMS/README.md)

### On-Board Systems
- [T-TECHNOLOGIES README](T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/README.md)

### Infrastructure
- [I-INFRASTRUCTURES README](I-INFRASTRUCTURES/README.md)

### Neural Networks & AI Governance
- [N-NEURAL_NETWORKS README](N-NEURAL_NETWORKS/README.md)

### Engineering SSOT Front-End
- [ENGINEERING_SSOT README](ENGINEERING_SSOT/README.md)
- [SSOT Registry Browser (front-end)](ENGINEERING_SSOT/index.html)

---

## Total Coverage (CV-003 Specification)

- **7** Top-Level Domains (O, P, R, T, I, N, S)
- **33** Sub-Domains Total:
  - **2** Organization Sub-Domains (O/A, O/B)
  - **2** Program Sub-Domains (P/P, P/S)
  - **1** Reserved Sub-Domain (R/R)
  - **15** Technology Sub-Domains (T/A, T/M, T/E1, T/D, T/I, T/E2, T/E3, T/L1, T/L2, T/C1, T/C2⭐, T/I2⭐, T/A2, T/O, T/P⭐)
  - **3** Infrastructure Sub-Domains (I/M1, I/M2, I/O)
  - **3** Neural Network Sub-Domains (N/D, N/A, N/P*)
  - **7** SimTest & Digital Twin Sub-Domains (S/G, S/X, S/T, S/V, S/F, S/U, S/R)
- **3** Novel Technology Designations (⭐): T/C2, T/I2, T/P
- **121** Active Chapters (000–124, excluding X13/X17 set {013, 017, 113, 117})
- **3-digit** zero-padded chapter format (000–124)
- **14** Lifecycle Phases (LC01–LC14)
- **63** Artifact Type Codes
- **3** Exclusive Baselines (FBL, DBL, PBL)

---

## Related Documents

| Document | Path | Description |
|----------|------|-------------|
| **Chapter Master Table** | `OPT-IN_FRAMEWORK/CHAPTER_MASTER_TABLE.yaml` | Authoritative 121-chapter SSOT |
| **Cultural Exclusion Policy** | `OPT-IN_FRAMEWORK/AMPEL360-OPTIN-CULTURAL-EXCLUSION-001.yaml` | X13/X17 exclusion policy |
| **CV-003 Specification** | `docs/specifications/AMPEL360_CV_003_CONTROLLED_VOCABULARY.md` | Complete controlled vocabulary and identifier grammar |
| **Artifact Types Registry** | `schemas/ampel360_artifact_types.yaml` | 63 artifact types with package origins |
| **Metadata Schema** | `schemas/ampel360_metadata_record.schema.json` | JSON Schema for artifact metadata |
| **TLI v2.1 Registry** | `lifecycle/LC_PHASE_REGISTRY.yaml` | Canonical lifecycle phase definitions |
| **T-Subdomain Activation** | `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml` | Technology subdomain lifecycle rules |
| **Python Module** | `src/aerospacemodel/ampel360/` | Identifier grammar and PBS/WBS utilities |

---

*Refer to main [OPT-IN_FRAMEWORK README](README.md) for detailed information.*
