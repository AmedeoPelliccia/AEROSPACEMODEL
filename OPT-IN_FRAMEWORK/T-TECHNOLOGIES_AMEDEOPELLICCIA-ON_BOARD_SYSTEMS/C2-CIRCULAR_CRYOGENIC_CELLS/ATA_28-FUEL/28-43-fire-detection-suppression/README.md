# 28-43 — Fire Detection and Suppression (LH₂ Circular Cryogenic Cells)

**ATA Section:** 28-43
**System:** AMPEL360 Q100 — C2 Circular Cryogenic Cells
**Compliance:** S1000D Issue 5.0, CS-25 Special Conditions, ARP4754A, ARP4761

## Scope

This section covers the **fire detection and suppression** subsystem for liquid hydrogen (LH₂) circular cryogenic cells:

- H₂ fire detection system
- Fire suppression system (if required)
- Integration with ATA 26 — Fire Protection
- Hydrogen fire response procedures

## Area of Responsibility

| Role | Stakeholder |
|------|-------------|
| Design authority | C2 Systems Team (STK_ENG) |
| Safety oversight | STK_SAF |
| Configuration management | STK_CM |

## Boundaries

- Upstream: GENESIS/ (uncertainty discovery layer)
- Downstream: Subject folders under `28-43-00-fire-detection-suppression-general/`
- Interface: ATA 28-10 (storage), ATA 71 (fuel cell interface)

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `GENESIS/` | Uncertainty discovery — O-KNOTs and Y-KNOTs |
| `28-43-00-fire-detection-suppression-general/` | Subject-level lifecycle artifacts (KDB, IDB, CONTRACTS) |
| `SECTION_INDEX.yaml` | Section-level artifact index and metrics |
