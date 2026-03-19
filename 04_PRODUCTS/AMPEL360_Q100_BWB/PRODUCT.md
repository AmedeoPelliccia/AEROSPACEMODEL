# AMPEL360_Q100_BWB — Product Definition

**Path:** `04_PRODUCTS/AMPEL360_Q100_BWB/PRODUCT.md`
**Authority:** ASIT
**Status:** ACTIVE_BASELINE

---

## Purpose

Defines the AMPEL360 Q100 Blended Wing Body (BWB) aircraft governed under AEROSPACEMODEL.

## Product Family Description

The AMPEL360 Q100 BWB is a next-generation 100-passenger blended wing body transport aircraft with distributed electric propulsion powered by hydrogen fuel cell (H₂ FC) primary power. It inherits a shared technology base from the AAM/UAM eVTOL programme, particularly in battery thermal management, power electronics, motor controller assurance (DO-178C/DO-254), and certification pathway precedents.

## Key Performance Parameters

| Parameter              | Value                                  |
|------------------------|----------------------------------------|
| Configuration          | Blended Wing Body (BWB)                |
| Propulsion             | Open-fan distributed electric + H₂ FC |
| Primary power          | Hydrogen Fuel Cell (H₂ FC)            |
| Seating                | ~100 passengers                        |
| Target certification   | CS-25 + Special Conditions (2030+)     |

## Technology Inheritance from AAM/UAM

The following shared technology nodes connect this programme to the AAM/UAM eVTOL:

| Shared Node                              | AAM Specific         | Q100 Specific          |
|------------------------------------------|----------------------|------------------------|
| Distributed electric propulsion ATA 61+71| 4–18 rotors, tilt    | Open-fan, BWB          |
| Power management + peak buffering ATA 24 | Battery-dominant     | H₂ FC primary          |
| Battery thermal management ATA 24+96     | Runaway containment  | Buffer + cryogenic     |
| DO-178C / DO-254 motor controller        | FBW + autonomous     | FBW + AI monitoring    |
| First-of-kind certification pathway      | SC-VTOL (2026–27)    | CS-25 + SC (2030+)     |

- **KNOT spillover coefficient A = 0.50**
- TT rewards flow bidirectionally via TOKENOMICS spillover

## Variants

| Variant ID       | Description                     | Status          |
|------------------|---------------------------------|-----------------|
| Q100_BWB_BASE    | Q100 BWB base configuration     | ACTIVE_BASELINE |

## Applicable Standards

- CS-25 + Special Conditions (EASA, 2030+ target)
- ARP4754A — Systems Development
- ARP4761A — Safety Assessment
- DO-178C — Software Assurance
- DO-254 — Hardware Assurance
- EU Battery Regulation 2023/1542 (buffer battery DPP)
