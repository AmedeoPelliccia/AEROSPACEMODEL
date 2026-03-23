# LC03 — Q100_BWB_BASE

**Path:** `04_PRODUCTS/AMPEL360_Q100_BWB/variants/Q100_BWB_BASE/lifecycle/LC03_ARCHITECTURE/README.md`
**Lifecycle Phase:** LC03
**Status:** ACTIVE_BASELINE

---

## Architecture Definition

This phase defines the system architecture of the AMPEL360 Q100 BWB, capturing the technology nodes shared with the AAM/UAM eVTOL programme (KNOT spillover coefficient A = 0.50).

## Shared Technology Base

| ATA/Standard      | Technology Node                          | Q100 BWB Specific             | AAM/UAM Specific         |
|-------------------|------------------------------------------|-------------------------------|--------------------------|
| ATA 61 + 71       | Distributed electric propulsion          | Open-fan, BWB                 | 4–18 rotors, tilt        |
| ATA 24            | Power management + peak buffering        | H₂ FC primary                 | Battery-dominant         |
| ATA 24 + 96       | Battery thermal management + DPP         | Buffer + cryogenic            | Runaway containment, SoH |
| DO-178C / DO-254  | Motor controller DAL A/B assurance       | FBW + AI monitoring           | FBW + autonomous         |
| CS-25 + SC        | First-of-kind certification pathway      | CS-25 + SC (2030+)            | SC-VTOL (2026–27)        |

## KNOT Spillover

- **Coefficient A = 0.50**
- SC-VTOL type certificate precedent from AAM/UAM eVTOL programme establishes certification basis for Q100 CS-25 + Special Conditions.
- Battery KNOTs are bidirectionally linked — resolving Q100 buffer battery KNOTs reduces AAM/UAM battery uncertainty.

## Status Summary

| Item                | Status |
|---------------------|--------|
| KNOTS defined       | ✔      |
| KNUs planned        | ✔      |
| Evidence collected  | ☐      |
| Audit complete      | ☐      |
| Phase closed        | ☐      |
