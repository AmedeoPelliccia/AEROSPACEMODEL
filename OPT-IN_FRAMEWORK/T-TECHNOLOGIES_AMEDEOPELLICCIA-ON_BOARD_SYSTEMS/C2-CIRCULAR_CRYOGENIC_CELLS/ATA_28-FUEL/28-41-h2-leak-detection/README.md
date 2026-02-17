# 28-41 — H₂ Leak Detection (LH₂ Circular Cryogenic Cells)

**ATA Section:** 28-41
**System:** AMPEL360 Q100 — C2 Circular Cryogenic Cells
**Compliance:** S1000D Issue 5.0, CS-25 Special Conditions, ARP4754A, ARP4761

## Scope

This section covers the **h₂ leak detection system** subsystem for liquid hydrogen (LH₂) circular cryogenic cells:

- Multi-sensor hydrogen leak detection
- Electrochemical, thermal conductivity, and optical sensors
- Sensor placement and coverage for all potential leak points
- Leak detection integration with emergency shutdown

## Area of Responsibility

| Role | Stakeholder |
|------|-------------|
| Design authority | C2 Systems Team (STK_ENG) |
| Safety oversight | STK_SAF |
| Configuration management | STK_CM |

## Boundaries

- Upstream: GENESIS/ (uncertainty discovery layer)
- Downstream: Subject folders under `28-41-00-h2-leak-detection-general/`
- Interface: ATA 28-10 (storage), ATA 71 (fuel cell interface)

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `GENESIS/` | Uncertainty discovery — O-KNOTs and Y-KNOTs |
| `28-41-00-h2-leak-detection-general/` | Subject-level lifecycle artifacts (KDB, IDB, CONTRACTS) |
| `SECTION_INDEX.yaml` | Section-level artifact index and metrics |
