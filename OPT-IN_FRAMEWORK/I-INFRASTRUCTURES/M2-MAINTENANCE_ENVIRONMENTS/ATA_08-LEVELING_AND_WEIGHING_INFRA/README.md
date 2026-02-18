# ATA 08 — Leveling and Weighing Infrastructure

**Domain:** I-INFRASTRUCTURES / M2  
**ATA Chapter:** 08 — Leveling and Weighing  
**Directory:** `ATA_08-LEVELING_AND_WEIGHING_INFRA/`  
**Program:** AMPEL360 Q100  
**Authority:** ASIT

---

## Scope

The **ATA_08-LEVELING_AND_WEIGHING_INFRA** directory covers all ground infrastructure required to perform aircraft leveling and weighing operations on the AMPEL360 Q100.

Key facilities and capabilities:
- Aircraft leveling jack points and jack-stand facilities
- Precision weighing platforms and load cell systems
- Calibration equipment and metrology infrastructure
- Recording and data-management systems for weight and balance reports

---

## ATA Chapter Decomposition

| Sub-Section | Description |
|---|---|
| 08-10 | Leveling – aircraft jacking points and jack pad infrastructure |
| 08-20 | Weighing – platform scales, portable load cells |
| 08-30 | Calibration – weighing equipment calibration and traceability |
| 08-40 | Recording – weight and balance data capture and archiving |

---

## Novel Technology Aspects ⭐

The AMPEL360 Q100 introduces liquid hydrogen (LH₂) as propellant, creating unique weighing infrastructure requirements:

- **⭐ LH₂ mass correction:** Weighing with partial or full LH₂ load requires cryogenic density correction to convert volume readings to mass equivalents.
- **⭐ H₂-safe weighing bay:** The weighing bay must be equipped with H₂ leak detection and forced ventilation per NFPA 2 and `ATA_IN_H2_GSE_AND_SUPPLY_CHAIN` interface requirements.
- **⭐ Post-LH₂-loading weighing sequence:** Standard weighing sequence is extended with LH₂ isolation valve checks and vapour purge verification before personnel enter the weighing zone.

---

## Cross-References

| Domain | Interface |
|---|---|
| T/C2-CIRCULAR_CRYOGENIC_CELLS (ATA 28) | LH₂ tank mass and CG data feed into weight & balance |
| T/P-PROPULSION (ATA 71) | Fuel cell stack mass contribution to weighing |
| I/O/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN | H₂ GSE bay safety requirements for weighing zone |
| P/S-SERVICE_INSTRUCTION/ATA_08 | Aircraft-side leveling and weighing procedures |

---

## Document Index

| File | Section | Description |
|---|---|---|
| `README.md` ← *this file* | 1 — Overview & Scope | Scope, ATA decomposition, cross-refs |
| `01_REQUIREMENTS.md` | 2 — Normative Requirements | Regulations and standards |
| `02_DESIGN_SPEC.md` | 3 — Design Specification | Equipment performance and facility design |
| `03_EQUIPMENT.md` | 4 — Equipment | Tool and equipment inventory |
| `04_PROCEDURES.md` | 5 — Procedures | Step-by-step operational procedures |
| `05_SAFETY_RISKS.md` | 6 — Safety & Risk Assessment | Hazards, mitigations, failure modes |
| `06_CASE_STUDIES.md` | 7 — Case Studies | Reference implementations and lessons learned |

See [`../CROSSWALK.md`](../CROSSWALK.md) for the full 7-section summary crosswalk.

---

*End of ATA 08 — Leveling and Weighing Infrastructure README*
