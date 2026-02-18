# M2 — Maintenance Environments

**Domain:** I-INFRASTRUCTURES / M2  
**ATA Designations:** ATA 08 (Leveling & Weighing), ATA 10 (Parking/Mooring/Storage/RTS), ATA 12 (Servicing)  
**Program:** AMPEL360 Q100  
**Authority:** ASIT (Aircraft Systems Information Transponder)

---

## Purpose

The **M2-MAINTENANCE_ENVIRONMENTS** subdomain organises the ground-based maintenance infrastructure—from line stations through heavy-maintenance hangars to component shops—required to keep the AMPEL360 Q100 airworthy throughout its operational life.

M2 establishes the infrastructure baseline for:
- Aircraft leveling and weighing facilities (ATA 08)
- Parking, mooring, storage, and return-to-service (RTS) ground handling (ATA 10)
- Scheduled and unscheduled servicing equipment and fluid handling (ATA 12)

---

## Subdomain Structure

| ATA Directory | Code | Description | Key Standards/Regulations |
|---|---|---|---|
| `ATA_08-LEVELING_AND_WEIGHING_INFRA` | 08I | Leveling jacks, weighing platforms, and calibration equipment | EASA Part-M, FAA AC 43.13-1B, CS-25 |
| `ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA` | 10I | Tow bars, chocks, tie-down gear, ground power, storage bays, RTS checklist infrastructure | EASA Part-M, Part-145, FAA AC 43.13-1B |
| `ATA_12-SERVICING_INFRA` | 12I | Fluid servicing carts, special tools, hydrogen-compatible servicing equipment | EASA Part-145, FAA Part 43, NFPA 2 |

---

## Directory Conventions

Each ATA subdirectory contains seven canonical section files plus a crosswalk:

| File | Section | Content |
|---|---|---|
| `README.md` | 1 — Overview & Scope | ATA scope, cross-refs, special conditions |
| `01_REQUIREMENTS.md` | 2 — Normative Requirements | Regulatory and standard requirements |
| `02_DESIGN_SPEC.md` | 3 — Design Specification | Infrastructure design and performance specs |
| `03_EQUIPMENT.md` / `03_SERVICES.md` | 4 — Equipment / Services | Hardware list or service portfolio (per ATA) |
| `04_PROCEDURES.md` / `04_OPERATIONS.md` | 5 — Procedures / Operations | Step-by-step maintenance or operational procedures |
| `05_SAFETY_RISKS.md` | 6 — Safety & Risk Assessment | Hazard identification, mitigations, ARP4761 failure modes |
| `06_CASE_STUDIES.md` | 7 — Case Studies | Reference implementations and lessons learned |

See [`CROSSWALK.md`](CROSSWALK.md) for the detailed mapping of each executive-summary section to the corresponding file(s).

---

## Novel Technology Aspects

Where the AMPEL360 Q100 hydrogen propulsion system introduces special conditions, content is tagged **⭐ Special Condition**:

- **LH₂-compatible servicing equipment** (ATA 12): Hydrogen-rated hoses, cryogenic connectors, boil-off management lines
- **H₂ leak detection in maintenance bays** (ATA 08/10/12): Multi-sensor detection, ventilation interlocks
- **Extended RTS procedures after H₂ refueling** (ATA 10): Purge verification, isolation valve checks
- **Weighing after LH₂ loading** (ATA 08): Density correction procedures for cryogenic fuel mass

---

## Lifecycle Integration

M2 primarily activates during:

### LC10 — Industrial & Supply Chain
- Infrastructure procurement and installation
- Tooling and special equipment qualification

### LC12 — Continued Airworthiness & MRO
- Line-maintenance servicing
- Heavy-maintenance facility operations
- Weighing and re-certification after modifications

### LC14 — End of Life
- Aircraft decommissioning and storage infrastructure
- LH₂ system safe defueling and inerting

---

## Traceability to Other Domains

| Domain | Interface |
|---|---|
| T/C2-CIRCULAR_CRYOGENIC_CELLS (ATA 28) | LH₂ servicing and leak-detection interfaces |
| T/P-PROPULSION (ATA 71) | Fuel cell maintenance tooling and procedures |
| I/M1-MANUFACTURING_FACILITIES | Quality standards shared with MRO operations |
| O/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN | Airport-side H₂ supply chain coordination |
| N/A-AI_GOVERNANCE_ASSURANCE | AI-assisted predictive maintenance tools |

---

## Governance

- **Owner:** ASIT (Aircraft Systems Information Transponder)
- **Responsible Stakeholder:** STK_MRO (MRO Manager), STK_SAF (Safety Officer)
- **Change Control:** ECR/ECO via Configuration Control Board (CCB)
- **Baseline Authority:** `ASIT/GOVERNANCE/master_brex_authority.yaml`
- **Lifecycle Activation Rules:** `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml`

---

## Related Documents

| Document | Path | Purpose |
|---|---|---|
| I-INFRASTRUCTURES Index | `../00_INDEX.md` | Parent domain index |
| M2 Crosswalk | `CROSSWALK.md` | 7-section summary → file mapping |
| ATA 08 | `ATA_08-LEVELING_AND_WEIGHING_INFRA/README.md` | Leveling & Weighing scope |
| ATA 10 | `ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA/README.md` | Parking, Mooring & Storage scope |
| ATA 12 | `ATA_12-SERVICING_INFRA/README.md` | Servicing infrastructure scope |
| ATA 28 H2 Cryogenic Instructions | `../../../.github/instructions/ata28_h2_cryogenic.instructions.md` | Hydrogen safety procedures |

---

## Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0.0 | 2026-02-18 | ASIT | Initial M2 subdomain structure for AMPEL360 Q100 maintenance |

---

*End of M2 — Maintenance Environments README*
