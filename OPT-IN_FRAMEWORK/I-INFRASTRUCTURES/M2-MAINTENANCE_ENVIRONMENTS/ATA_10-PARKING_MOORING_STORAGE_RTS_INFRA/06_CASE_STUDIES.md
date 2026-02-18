# ATA 10I — Parking, Mooring, Storage, and RTS Infrastructure: Case Studies

**Domain:** I-INFRASTRUCTURES / M2-MAINTENANCE_ENVIRONMENTS / ATA_10  
**Document Type:** Case Studies and Lessons Learned  
**Revision:** 0.1.0

---

## 1. Purpose

This document captures case studies and lessons learned relevant to parking, mooring, storage, and RTS infrastructure for novel-technology aircraft.

---

## 2. Case Study: H₂ Aircraft Storage — Industry Reference Programs

### Background
The ZEROe and FTLAB programs (Airbus/industry) identified that long-term storage of H₂ aircraft with LH₂ aboard is impractical beyond 7 days due to LH₂ boil-off and the associated need for active BOG management infrastructure. Programs have moved toward a standard of defueling H₂ aircraft for storage periods exceeding one week.

### Lesson Learned
- Infrastructure for H₂ aircraft must include BOG vent infrastructure at parking positions.
- Storage > 7 days with LH₂ aboard requires continuous active monitoring.
- Long-term storage requires LH₂ defueling, introducing additional infrastructure for ground defueling operations.

### ⭐ AMPEL360 Q100 Action
- REQ-10I-046 mandates defueling for storage > 7 days.
- 02_DESIGN_SPEC.md includes BOG vent connection design.
- 03_OPERATIONS.md and 04_PROCEDURES.md reflect storage monitoring requirements.

---

## 3. Case Study: Inadequate Parking Zone Separation — Near-Miss Reference

### Background
An industry near-miss event (anonymized) occurred when an H₂ aircraft (research) was parked adjacent to a conventional aircraft without adequate separation. A minor H₂ leak during overnight parking was not detected because the position lacked H₂ monitoring. The concentration was identified by personnel the following morning.

### Lesson Learned
- H₂ detection must be at the parking position level, not just at refueling stations.
- Aircraft-type-specific parking positions must be enforced by facility procedure.
- Minimum 15 m separation from H₂ aircraft to other aircraft or buildings.

### ⭐ AMPEL360 Q100 Action
- REQ-10I-044 requires 15 m separation for H₂ aircraft.
- REQ-10I-043 and REQ-10I-045 require H₂ zone classification and detection at parking position.
- 05_SAFETY_RISKS.md captures RISK-10I-013 (H₂ aircraft in non-rated position).

---

## 4. Case Study: RTS Error After Storage — Industry Reference

### Background
Multiple industry events have involved aircraft released to service after storage without completing all RTS checks (particularly ground safety pin removal, tire pressure, and deferred defect review). These events highlight the importance of structured RTS procedures with independent verification.

### Lesson Learned
- RTS checklist must include explicit removal of all ground safety devices.
- Deferred defect review is mandatory — cannot be waived.
- Part-145 release must be signed only after completion of all items.

### AMPEL360 Q100 Action
- 04_PROCEDURES.md Section 5 provides comprehensive RTS checklist.
- ⭐ LH₂ system check is explicitly included for H₂ aircraft RTS.

---

## 5. Lessons Learned Summary

| ID | Lesson | Implemented In |
|----|--------|---------------|
| LL-10I-001 | H₂ storage > 7 days requires LH₂ defueling | REQ-10I-046, 04_PROCEDURES.md |
| LL-10I-002 | H₂ detection required at each H₂ parking position | REQ-10I-045, 02_DESIGN_SPEC.md |
| LL-10I-003 | 15 m separation mandatory for H₂ aircraft | REQ-10I-044, 02_DESIGN_SPEC.md |
| LL-10I-004 | Structured RTS with Part-145 approval mandatory | REQ-10I-052, 04_PROCEDURES.md |
| LL-10I-005 | BOG vent infrastructure required at H₂ parking positions | REQ-10I-042, 02_DESIGN_SPEC.md |

---

## 6. Related Documents

- [ATA 10I Safety Risks](05_SAFETY_RISKS.md)
- [ATA 10I Operations](03_OPERATIONS.md)
- [ATA 08I Case Studies](../ATA_08-LEVELING_AND_WEIGHING_INFRA/06_CASE_STUDIES.md)
- [ATA 12I Case Studies](../ATA_12-SERVICING_INFRA/06_CASE_STUDIES.md)
