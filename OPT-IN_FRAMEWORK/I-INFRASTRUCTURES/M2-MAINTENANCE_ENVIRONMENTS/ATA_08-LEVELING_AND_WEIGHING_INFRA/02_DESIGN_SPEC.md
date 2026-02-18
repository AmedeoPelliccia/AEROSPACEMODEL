# ATA 08 — Leveling and Weighing Infrastructure: Design Specification

**Section:** 3 — Design Specification  
**Parent:** [`README.md`](README.md) | **Crosswalk:** [`../CROSSWALK.md`](../CROSSWALK.md)

---

## Facility Design Requirements

### Weighing Bay Layout
- **Floor loading capacity:** ≥ 3 × maximum take-off weight of AMPEL360 Q100 distributed over jack-point footprint.
- **Bay dimensions:** Sufficient to accommodate aircraft with wings unfolded (if applicable) plus 3 m clearance on all sides.
- **Floor levelness:** ≤ ±2 mm over 3 m span (per OIML R 76 site requirements).
- **Drainage:** Impermeable floor with drain capable of containing hydraulic fluid and water volumes per Part-145 environmental requirements.

### Leveling Jack Points
- **Jack pad material:** Aluminium alloy 7075-T6 or equivalent; compatible with AMPEL360 Q100 jacking diagram.
- **Jack capacity:** Each jack rated ≥ 125% of maximum expected jack-point load.
- **Hydraulic jack fluid:** Aircraft-compatible hydraulic fluid; compatibility verified with aircraft manufacturer's approved material list (AML).

### Hydrogen Safety Design ⭐
- **Bay classification:** Zone 2 hazardous area (IEC 60079-10-1) for the floor level within 3 m of LH₂ vent ports during weighing with LH₂ aboard.
- **Forced ventilation:** Minimum 10 air changes per hour; interlock with H₂ detection system to increase to 20 ACH on H₂ alarm.
- **H₂ detection threshold:** Pre-alarm at 10% LEL; evacuation alarm at 25% LEL.
- **Bonding and grounding:** Dedicated earthing points at aircraft nose-gear and main-gear positions; resistance ≤ 1 Ω.
- **Electrical equipment:** All electrical equipment within Zone 2 to be ATEX/IECEx rated.

---

## Weighing Equipment Specifications

### Platform Scales
- **Measurement range:** 0–30,000 kg per platform (or greater, depending on aircraft MTOW).
- **Resolution:** ≤ 1 kg.
- **Accuracy class:** OIML Class III (minimum); Class II preferred for certification weighing.
- **Operating temperature range:** −10°C to +50°C.
- **Calibration interval:** 12 months or after any repair/overload event.

### Portable Load Cells (alternative to platform scales)
- **Rated capacity:** 150% of maximum jack-point load.
- **Combined error:** ≤ 0.1% of full scale.
- **Environmental rating:** IP65 minimum (jet fuel and water ingress protection).

### Data Acquisition System
- **Interface:** RS-232 / USB / Ethernet to laptop or dedicated weighing terminal.
- **Output format:** PDF report compliant with AC 43.13-1B weighing record format.
- **Timestamp resolution:** 1 second; synchronised to UTC via NTP.

---

## Calibration Infrastructure

- **Reference standard:** Dead-weight test set traceable to national metrology institute (e.g., PTB, NIST, NPL).
- **Calibration chain:** BIPM → national laboratory → accredited calibration laboratory (ISO 17025) → in-service equipment.
- **Calibration record retention:** Minimum 10 years.

---

*End of ATA 08 — Design Specification*
