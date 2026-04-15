# AAM_UAM_EVTOL — Product Definition

**Path:** `04_PRODUCTS/AAM_UAM_EVTOL/PRODUCT.md`
**Authority:** ASIT
**Status:** ACTIVE_BASELINE

---

## Purpose

Defines the Advanced Air Mobility / Urban Air Mobility (AAM/UAM) eVTOL product family governed under AEROSPACEMODEL.

## Product Family Description

The AAM/UAM eVTOL product family covers electric Vertical Take-Off and Landing aircraft designed for metro and regional air mobility missions. The mission is defined by the **network**, not the vehicle alone — a single eVTOL has no utility without vertiport pairs, airspace corridors, charging infrastructure, and UTM integration. The "system" being certified is the entire operation.

## Operational Concept

- **Flight profile:** Vertical climb → Transition → Cruise (150–300 m AGL, U-space corridor) → Decelerate → Vertical descent
- **Typical metro mission:** 30–80 km, 12–25 min gate-to-gate
- **Cruise:** 150–250 km/h TAS, 150–300 m AGL in U-space corridor
- **Vertiport pair:** Origin (Vertiport A) → Destination (Vertiport B)

## Key Performance Parameters

| Parameter         | Value                  |
|-------------------|------------------------|
| Range             | 30–150 km              |
| Passengers        | 1–6 pax                |
| Gate-to-gate      | 12–35 min              |
| Turnaround        | 5–10 min               |

## Variants

See `variants/` for product variant instances.

| Variant ID      | Description                      | Status          |
|-----------------|----------------------------------|-----------------|
| AAM_UAM_BASE    | Base eVTOL configuration         | ACTIVE_BASELINE |

## Technology Inheritance

This product family shares a technology base with the AMPEL360 Q100 BWB programme.
See `variants/AAM_UAM_BASE/domains/P-PROPULSION/technology_inheritance.yaml` for the shared technology nodes and KNOT spillover model.

## Applicable Standards

- SC-VTOL (EASA Special Condition for VTOL, 2026–2027 target)
- ARP4754A — Systems Development
- ARP4761A — Safety Assessment
- DO-178C — Software Assurance
- DO-254 — Hardware Assurance
- EUROCAE ED-269 / ASTM F3411 — UTM/UAS Traffic Management
