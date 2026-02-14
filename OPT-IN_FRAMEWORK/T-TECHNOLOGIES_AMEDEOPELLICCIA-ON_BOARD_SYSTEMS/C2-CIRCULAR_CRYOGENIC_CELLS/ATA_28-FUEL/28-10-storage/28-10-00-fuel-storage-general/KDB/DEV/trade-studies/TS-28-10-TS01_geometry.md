# TS-28-10-TS01 — Geometry: Circular vs Non-Circular Cryogenic Tanks

| Key | Value |
|-----|-------|
| Trade Study ID | TS-28-10-TS01 |
| ATA Code | 28-10-00 |
| Technology Domain | C2 — Circular Cryogenic Cells |
| Aircraft Programme | AMPEL360 Q100 |
| Lifecycle Phase | LC04 (Design Definition) |
| Status | Preliminary |
| Author | STK_ENG |
| Date | 2026-02-14 |

## Objective

Determine optimal tank cross-section for structural efficiency,
cryogenic thermal stability, integration within BWB centerbody,
and certification feasibility.

---

## Options Considered

| Option | Name | Structural Efficiency | Thermal Behaviour | Integration | Certification Risk |
|--------|------|-----------------------|-------------------|-------------|--------------------|
| A | Circular Cylinder | High | Optimal | Moderate | Low |
| B | Elliptical | Medium | Moderate | High | Medium |
| C | Conformal / Multi-lobed | Low–Medium | Complex | Very High | High |

### Option A — Circular Cylinder

- **Stress model:** Uniform hoop stress — σ\_hoop = P·r / t
- **Stress concentration:** Minimal
- **Insulation layering:** Simplified
- **Heritage:** NASA, Airbus ZEROe concepts
- **Mass efficiency:** HIGH

### Option B — Elliptical

- **Stress distribution:** Non-uniform
- **Reinforcement:** Required at major axis
- **Thermal gradient risk:** Curvature transitions
- **Mass penalty:** +4–8 % estimated

### Option C — Conformal / Multi-lobed

- **Load paths:** Complex
- **Weld length:** Increased
- **Sloshing complexity:** High
- **Vent routing:** Complex
- **Certification uncertainty:** High

---

## Preliminary Selection

**Selected Option:** A — Circular Cylinder
**Baseline Name:** Circular Cryogenic Cell (CCC)

### Rationale

- Lowest structural risk
- Predictable cryogenic behaviour
- Deterministic modelling compatibility (5D addressable tank states)
- Compatible with modular distributed storage (zones 610–640)

---

## Feeds

| Lifecycle | Artifact |
|-----------|----------|
| LC03 | Safety FHA update |
| LC05 | Finite element comparative analysis (A vs B geometries) |

## Traceability

- **Derives from:** WP-28-03
