# OPT-IN_FRAMEWORK Index

**AIRCRAFT TLI v2.1 Canonical Architecture**

> **Controlled Vocabulary:** This structure is governed by [AMPEL360-CV-003](../docs/specifications/AMPEL360_CV_003_CONTROLLED_VOCABULARY.md)  
> **Identifier Grammar:** `AMPEL360_Q100_MSN{nnn}_ATA{cc}-{ss}-{ss}_LC{nn}_{TYPE}_{seq}`  
> **PBS Grammar:** `PBS-{AXIS}{SUBDOM}-{ATA}-{SECTION}-{SUBJECT}-{ITEM}`

---

## Domain Structure

| Domain | Code | Path | ATA Scope | Description |
|--------|------|------|-----------|-------------|
| **O-ORGANIZATIONS** | O | `O-ORGANIZATIONS/` | ATA 00–05 | Organizational and governance documentation |
| **P-PROGRAMS** | P | `P-PROGRAMS/` | ATA 06–12 | Program-level procedures and servicing |
| **T-TECHNOLOGIES** | T | `T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/` | ATA 20–80, 95–97 | Complete on-board systems (15 subdomains) |
| **I-INFRASTRUCTURES** | I | `I-INFRASTRUCTURES/` | Infrastructure | Ground support and supply chain |
| **N-NEURAL_NETWORKS** | N | `N-NEURAL_NETWORKS/` | Governance | AI governance and traceability |

---

## Technology Subdomains (T-TECHNOLOGIES)

| Subdomain | Code | ATA Chapters | Technology Type |
|-----------|------|--------------|-----------------|
| Airframe & Cabins | A | 20, 25, 44, 50–57 | Standard |
| Mechanics | M | 27, 29, 32 | Standard |
| Environment | E1 | 21, 26, 30, 35–38, 47 | Standard |
| Data | D | 31, 45 | Standard |
| Information | I | 46 | Standard |
| Energy | E2 | 24, 49 | Standard |
| Electrics | E3 | 33, 39 | Standard |
| Logics | L1 | Reserved | Future |
| Links | L2 | 34 | Standard |
| Comms | C1 | 23 | Standard |
| **Cryogenic Cells** | **C2** | **28** | **Novel Technology** ⭐ |
| **Intelligence** | **I2** | **95, 97** | **Novel Technology** ⭐ |
| Avionics | A2 | 22, 42 | Standard |
| Operating Systems | O | 40 | Standard |
| **Propulsion** | **P** | **60–61, 71–80** | **Novel Technology** ⭐ |

⭐ **Novel Technology** = Full LC01–LC14 lifecycle activation with Special Conditions

---

## Organization Subdomains (O-ORGANIZATIONS)

| Subdomain | Code | ATA Chapters | Description |
|-----------|------|--------------|-------------|
| Authoritative | **A** | 00, 04, 05 | Agency, regulatory, and legal-derived requirements |
| Business Enforcement | **B** | 01, 02, 03 | Operator business policies and enforcement |

---

## Program Subdomains (P-PROGRAMS)

| Subdomain | Code | ATA Chapters | Description |
|-----------|------|--------------|-------------|
| Product Definition | **P** | 06, 08, 11 | What the product is — dimensions, weight, markings |
| Service Instruction | **S** | 07, 09, 10, 12 | How to handle it — lifting, towing, servicing |

---

## Infrastructure Subdomains (I-INFRASTRUCTURES)

| Subdomain | Code | Categories | Description |
|-----------|------|------------|-------------|
| Manufacturing Facilities | **M1** | ATA 85 | Production lines, test rigs, assembly benches |
| Maintenance Environments | **M2** | ATA 08I, 10I, 12I | In-line, hangars, shops |
| Operations & Service Structures | **O** | ATA 03I, ATA IN H2 GSE | Airport facilities, fuel logistics, ground services |

---

## Neural Network Subdomains (N-NEURAL_NETWORKS)

| Subdomain | Code | ATA / Scope | Description |
|-----------|------|-------------|-------------|
| Digital Thread & Traceability | **D** | ATA 96 | Ledger, DPP, hash chain, identifiers, schemas, audit packs |
| AI Governance & Assurance | **A** | Governance | Certification pathway, ethics, human authority protocols, explainability |
| Program Reserved | **P*** | ATA 98 | Expansion slot for future systems |

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

- **5** Top-Level Domains (O, P, T, I, N)
- **25** Sub-Domains Total:
  - **2** Organization Sub-Domains (O/A, O/B)
  - **2** Program Sub-Domains (P/P, P/S)
  - **15** Technology Sub-Domains (T/A, T/M, T/E1, T/D, T/I, T/E2, T/E3, T/L1, T/L2, T/C1, T/C2⭐, T/I2⭐, T/A2, T/O, T/P⭐)
  - **3** Infrastructure Sub-Domains (I/M1, I/M2, I/O)
  - **3** Neural Network Sub-Domains (N/D, N/A, N/P*)
- **3** Novel Technology Designations (⭐): T/C2, T/I2, T/P
- **66** ATA Chapter Directories
- **14** Lifecycle Phases (LC01–LC14)
- **63** Artifact Type Codes
- **3** Exclusive Baselines (FBL, DBL, PBL)

---

## Related Documents

| Document | Path | Description |
|----------|------|-------------|
| **CV-003 Specification** | `docs/specifications/AMPEL360_CV_003_CONTROLLED_VOCABULARY.md` | Complete controlled vocabulary and identifier grammar |
| **Artifact Types Registry** | `schemas/ampel360_artifact_types.yaml` | 63 artifact types with package origins |
| **Metadata Schema** | `schemas/ampel360_metadata_record.schema.json` | JSON Schema for artifact metadata |
| **TLI v2.1 Registry** | `lifecycle/LC_PHASE_REGISTRY.yaml` | Canonical lifecycle phase definitions |
| **T-Subdomain Activation** | `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml` | Technology subdomain lifecycle rules |
| **Python Module** | `src/aerospacemodel/ampel360/` | Identifier grammar and PBS/WBS utilities |

---

*Refer to main [OPT-IN_FRAMEWORK README](README.md) for detailed information.*
