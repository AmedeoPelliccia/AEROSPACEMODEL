# SSTO_BASELINE — Variant Definition

**Path:** `04_PRODUCTS/SSTO_SPACEPLANE/variants/SSTO_BASELINE/SSTO_BASELINE.md`
**Authority:** ASIT
**Status:** DRAFT

---

## Purpose

Defines the SSTO_BASELINE product variant: the baseline integrated
airframe-propulsion spaceplane configuration for orbital SSTO access.

This assessment addresses the orbital SSTO mission only. It does not treat
hypersonic point-to-point transport as an equivalent mission class.

## Vehicle Description

Reusable integrated airframe-propulsion orbital vehicle with cryogenic
LH₂/LOX propellant architecture, metallic/Ceramic Matrix Composite (CMC)
TPS, and horizontal runway take-off and landing.

### System Breakdown (ATA References)

| System                     | ATA Chapter | Key Characteristics                          |
|----------------------------|-------------|----------------------------------------------|
| Forebody                   | ATA 53      | Shock pre-compression; Peak TPS: 1 600+ K    |
| Wing                       | ATA 57      | Low AR delta / strake; lifting body blend     |
| Propulsion                 | ATA 71–78   | Combined-cycle or rocket (LH₂/LOX)           |
| Thermal Protection System  | ATA 51      | Metallic / CMC, active cooling               |
| Cryogenic Tanks            | ATA 28      | LH₂ + LOX, integral structure               |

### Mission Trajectory Phases

| Phase       | Mach Range      | Notes                                         |
|-------------|-----------------|-----------------------------------------------|
| Takeoff     | M 0–0.9         |                                               |
| Transonic   | M 0.9–1.5       |                                               |
| Supersonic  | M 1.5–5         |                                               |
| Hypersonic  | M 5–25          |                                               |
| Orbit/apex  | M 25+ / coast   |                                               |
| Re-entry    | TPS critical    |                                               |
| Return      | Subsonic glide  | Powered approach + runway landing             |

### Reference Assessment Targets

| Parameter         | Target                              |
|-------------------|-------------------------------------|
| Payload to LEO    | 5–10 metric tons                    |
| Orbit             | ~200 km circular LEO                |
| Reusability       | Full vehicle reuse, no discard      |
| Turnaround        | ≤ 48 hours (aspiration)             |
| Cost target       | < USD 10M/mission (stress-test)     |

## Configuration

See `configuration/configuration_baseline.yaml`.

## Lifecycle

See `lifecycle/` for phase-by-phase lifecycle records.

## Dashboard

See `dashboards/spaceplane_config_analysis.html` for the interactive
spaceplane configuration analysis and certification KNOT explorer.
