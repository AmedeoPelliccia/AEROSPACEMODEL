# LC03 — AAM_UAM_BASE

**Path:** `04_PRODUCTS/AAM_UAM_EVTOL/variants/AAM_UAM_BASE/lifecycle/LC03_ARCHITECTURE/README.md`
**Lifecycle Phase:** LC03
**Status:** ACTIVE_BASELINE

---

## Architecture Definition

This phase defines the system architecture of the AAM/UAM eVTOL, capturing the shared technology nodes that form the basis for technology inheritance with the AMPEL360 Q100 BWB programme.

## Shared Technology Base — AAM/UAM eVTOL ↔ AMPEL360 Q100 BWB

The following five technology nodes are shared between the AAM/UAM eVTOL and the AMPEL360 Q100 BWB programme. Resolving KNOTs in either programme reduces uncertainty in the other via KNOT spillover (coefficient A = 0.50).

| ATA/Standard          | Technology Node                             | AAM/UAM Specifics              | Q100 BWB Specifics         |
|-----------------------|---------------------------------------------|--------------------------------|----------------------------|
| ATA 61 + 71           | Distributed electric propulsion             | 4–18 rotors, tilt              | Open-fan, BWB              |
| ATA 24                | Power management + peak buffering           | Battery-dominant               | H₂ FC primary              |
| ATA 24 + 96           | Battery thermal management + DPP            | Runaway containment, SoH       | Buffer + cryogenic         |
| DO-178C / DO-254      | Motor controller DAL A/B assurance          | FBW + autonomous               | FBW + AI monitoring        |
| SC-VTOL / CS-25 + SC  | First-of-kind certification pathway         | SC-VTOL (2026–27)              | CS-25 + SC (2030+)         |

## KNOT Spillover

- **Coefficient A = 0.50**
- Resolving AAM/UAM battery KNOTs (KNOT-AAMUAM-LC03-0002, KNOT-AAMUAM-LC03-0003) reduces AMPEL360 Q100 buffer battery uncertainty at a 50% spillover rate, and vice versa.
- TT rewards flow bidirectionally via TOKENOMICS spillover.

## Status Summary

| Item                | Status |
|---------------------|--------|
| KNOTS defined       | ✔      |
| KNUs planned        | ✔      |
| Evidence collected  | ☐      |
| Audit complete      | ☐      |
| Phase closed        | ☐      |
