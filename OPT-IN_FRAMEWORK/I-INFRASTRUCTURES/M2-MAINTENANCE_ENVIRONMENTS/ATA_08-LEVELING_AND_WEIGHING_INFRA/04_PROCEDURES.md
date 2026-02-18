# ATA 08 — Leveling and Weighing Infrastructure: Procedures

**Section:** 5 — Procedures  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

---

## Overview

This document captures the step-by-step operational procedures for leveling and weighing the AMPEL360 Q100 aircraft. It supplements the aircraft AMM ATA 08 procedures with infrastructure-specific steps for the maintenance facility.

> **Safety prerequisite:** Read [`05_SAFETY_RISKS.md`](05_SAFETY_RISKS.md) before starting any procedure.

---

## Procedure 08-PRO-001 — Aircraft Weighing (Standard)

### Prerequisites
- [ ] Aircraft is defueled to dry operating weight or known fuel state recorded.
- [ ] All removable equipment accounted for or removed per AMM.
- [ ] Weighing bay cleared of non-essential personnel.
- [ ] Platform scales calibrated (certificate current — see `03_EQUIPMENT.md`).
- [ ] Aircraft maintenance log available.

### Steps
1. Position platform scales under each jack-point per AMM ATA 07 jacking diagram.
2. Connect aircraft bonding cable to bay earthing point.
3. Connect weighing data terminal to scales.
4. Jack aircraft to weighing position per AMM ATA 08.
5. Verify aircraft is level in both longitudinal and lateral axes (tolerance per AMM).
6. Record scale readings for all three points simultaneously.
7. Apply tare correction for jacks, adapters, and scales per AMM instructions.
8. Enter data into weighing terminal; verify CG is within CS-25.27 envelope.
9. Print and sign weighing report per AC 43.13-1B format.
10. Lower aircraft to ground; remove jacks and scales.
11. File completed weighing report in aircraft technical record.

---

## Procedure 08-PRO-002 — Aircraft Weighing with LH₂ Aboard ⭐

> **⭐ Special Condition:** This procedure applies when the AMPEL360 Q100 has liquid hydrogen in any tank during weighing (e.g., weighing to verify loading CG).

### Additional Prerequisites
- [ ] H₂ fixed detection system confirmed operational (test within 24 h).
- [ ] Forced ventilation confirmed running at ≥ 10 ACH.
- [ ] All personnel equipped with personal H₂ portable detectors.
- [ ] LH₂ tank isolation valves confirmed closed (verified by crew).
- [ ] Fuel temperature sensor reading recorded (for density correction).

### LH₂ Density Correction Step (inserted after Step 6 above)
6a. Record fuel temperature (T, in K) from LH₂ tank sensor.  
6b. Record fuel level (volume V, in L) from quantity indication system.  
6c. Calculate LH₂ mass: M = ρ(T) × V, where ρ(T) is per NIST Standard Reference Database 69 (LH₂ density vs temperature).  
6d. Enter corrected LH₂ mass in weighing terminal.

---

## Procedure 08-PRO-003 — Weighing Equipment Calibration Check (Pre-Use)

1. Zero scales with no load.
2. Place reference calibration weight (from `03_EQUIPMENT.md`) on each platform.
3. Verify reading is within ±0.1% of reference weight.
4. Record results in calibration check log.
5. If any scale fails: remove from service, tag out, and contact Metrology Lab.

---

## Procedure References

| Procedure | AMM Reference | Infrastructure File |
|---|---|---|
| Standard weighing | AMM ATA 08, Task 08-00-00-880-001 | This document |
| Jacking for weighing | AMM ATA 07, Task 07-11-00-480-001 | `03_EQUIPMENT.md` |
| LH₂ density correction | SC-28-H2-001 compliance | This document §08-PRO-002 |
| Scale calibration | ISO 17025, OIML R 76 | `03_EQUIPMENT.md`, `01_REQUIREMENTS.md` |

---

*End of ATA 08 — Procedures*
