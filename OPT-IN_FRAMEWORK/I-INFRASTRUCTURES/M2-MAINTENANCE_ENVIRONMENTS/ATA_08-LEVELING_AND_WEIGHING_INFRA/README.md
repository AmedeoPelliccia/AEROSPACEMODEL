# ATA 08 — Leveling and Weighing Infrastructure

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS  
**ATA Code:** 08I (Infrastructure variant of ATA 08)  
**Lifecycle Profile:** Standard  
**Novel Technology:** ⭐ Special Condition for H₂/fuel-cell aircraft weight variability

---

## Scope

This directory covers all ground-based infrastructure required to support **leveling and weighing operations** for the AMPEL360 Q100 aircraft. Weighing and leveling are performed to determine aircraft weight, center-of-gravity (CG), and moment data as required during manufacturing, maintenance, and scheduled checks.

### Coverage

- Weighing platform systems (electronic, hydraulic, mechanical)
- Jacking infrastructure and jack pad locations
- Optical and laser leveling equipment
- Weight and balance computation systems
- Calibration and traceability infrastructure
- **⭐ LH₂ fuel state compensation** for cryogenic hydrogen aircraft

---

## ATA Cross-References

| ATA Chapter | System | Relationship |
|-------------|--------|--------------|
| ATA 06 | Dimensions and Areas | Provides zonal reference data for weighing |
| ATA 08 (P-PROGRAMS) | Leveling and Weighing (Product) | On-board procedures; this file covers facilities |
| ATA 28 | Hydrogen Cryogenic Fuel | LH₂ density and mass correction for CG computation |
| ATA 32 | Landing Gear | Jack pad locations, tire pressure effects |

---

## Regulatory References

| Standard | Title |
|----------|-------|
| CS-25.1519 | Weight and Center of Gravity |
| CS-25.25 | Weight Limits |
| EASA Part-145 | MRO Approval Requirements |
| CAT.POL.A.100 | Load and Mass Data |
| JAR-OPS 1.605 | Mass and Balance — General |

---

## File Structure

| File | Purpose |
|------|---------|
| `README.md` | This file — scope, ATA reference, cross-references |
| `01_REQUIREMENTS.md` | Normative requirements |
| `02_DESIGN_SPEC.md` | Facility and equipment design specifications |
| `03_EQUIPMENT.md` | Equipment catalog |
| `04_PROCEDURES.md` | Weighing and leveling procedures |
| `05_SAFETY_RISKS.md` | Safety risks and mitigations |
| `06_CASE_STUDIES.md` | Case studies and lessons learned |

---

## Related Documents

- [M2-MAINTENANCE_ENVIRONMENTS README](../README.md)
- [M2-MAINTENANCE_ENVIRONMENTS Index](../00_INDEX.md)
- [I-INFRASTRUCTURES README](../../README.md)
- [P-PROGRAMS ATA 08 Product Definition](../../../P-PROGRAMS/P-PRODUCT_DEFINITION/ATA_08-LEVELING_AND_WEIGHING/)
