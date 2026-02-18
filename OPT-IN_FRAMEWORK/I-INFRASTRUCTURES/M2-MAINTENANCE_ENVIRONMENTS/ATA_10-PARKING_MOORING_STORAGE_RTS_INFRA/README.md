# ATA 10 — Parking, Mooring, Storage, and RTS Infrastructure

**Domain:** I-INFRASTRUCTURES / M2  
**ATA Chapter:** 10 — Parking, Mooring, Storage and Return to Service  
**Directory:** `ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA/`  
**Program:** AMPEL360 Q100  
**Authority:** ASIT

---

## Scope

The **ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA** directory covers all ground infrastructure required for the safe parking, mooring, and storage of the AMPEL360 Q100 aircraft, as well as the facilities and procedures enabling its return to service (RTS) after scheduled or unscheduled maintenance.

Key capabilities:
- Dedicated aircraft parking bays with hydrogen-compatible infrastructure
- Mooring and tie-down systems rated for AMPEL360 Q100 gross weight
- Short-term and long-term storage facilities
- Return-to-service (RTS) tooling and inspection infrastructure

---

## ATA Chapter Decomposition

| Sub-Section | Description |
|---|---|
| 10-10 | Parking — bay configuration, wheel chocks, GPU/APU connection |
| 10-20 | Mooring — tie-down patterns, anchor load requirements |
| 10-30 | Storage — indoor and outdoor storage, preservation procedures |
| 10-40 | Return to Service — RTS inspection infrastructure, signoff equipment |

---

## Novel Technology Aspects ⭐

The AMPEL360 Q100 LH₂ propulsion system introduces special requirements for parking and storage:

- **⭐ H₂ bay classification:** Parking bays where the aircraft rests with LH₂ aboard are classified as H₂ occupancy areas (NFPA 2); ventilation, detection, and electrical classification are mandatory.
- **⭐ Boil-off management during storage:** Extended storage (> 4 h) with LH₂ aboard requires either a boil-off recovery line connection or controlled venting procedure; the bay must have an outdoor vent stack.
- **⭐ Extended RTS checks after H₂ refueling:** RTS checklist includes LH₂ isolation valve verification, vent line reconnection, and H₂ detector functional test before engine start.
- **⭐ Tie-down load accounting for LH₂:** Tie-down calculations must use maximum gross weight including full LH₂ load; LH₂ density temperature correction applies to weight estimation.

---

## Cross-References

| Domain | Interface |
|---|---|
| T/C2-CIRCULAR_CRYOGENIC_CELLS (ATA 28) | LH₂ boil-off management interfaces with ATA 10 bay infrastructure |
| T/P-PROPULSION (ATA 71) | Fuel cell standby mode during storage |
| I/O/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN | H₂ GSE bay safety requirements for parking zones |
| P/S-SERVICE_INSTRUCTION/ATA_10 | Aircraft-side parking, mooring, and RTS procedures |

---

## Document Index

| File | Section | Description |
|---|---|---|
| `README.md` ← *this file* | 1 — Overview & Scope | Scope, ATA decomposition, cross-refs |
| `01_REQUIREMENTS.md` | 2 — Normative Requirements | Regulations and standards |
| `02_DESIGN_SPEC.md` | 3 — Design Specification | Bay design and mooring load specifications |
| `03_EQUIPMENT.md` | 4 — Equipment | Hardware inventory (chocks, tie-downs, GPU, etc.) |
| `04_OPERATIONS.md` | 5 — Operations | Operational procedures for parking, mooring, RTS |
| `05_SAFETY_RISKS.md` | 6 — Safety & Risk Assessment | Hazards, mitigations, failure modes |
| `06_CASE_STUDIES.md` | 7 — Case Studies | Reference implementations and lessons learned |

See [`../CROSSWALK.md`](../CROSSWALK.md) for the full 7-section summary crosswalk.

---

*End of ATA 10 — Parking, Mooring, Storage, and RTS Infrastructure README*
