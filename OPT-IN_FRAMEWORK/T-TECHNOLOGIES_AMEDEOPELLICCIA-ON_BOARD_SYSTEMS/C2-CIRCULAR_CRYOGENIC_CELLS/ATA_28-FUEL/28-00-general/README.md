# 28-00 — General (LH₂ Circular Cryogenic Cells)

**ATA Section:** 28-00
**System:** AMPEL360 Q100 — C2 Circular Cryogenic Cells
**Compliance:** S1000D Issue 5.0, CS-25 Special Conditions, ARP4754A, ARP4761

## Scope

This section covers the **h₂ cryogenic fuel — general** subsystem for liquid hydrogen (LH₂) circular cryogenic cells:

- System-level fuel system description and overview
- Cross-reference between sub-systems
- General fuel system safety and compliance
- System integration with ATA 71 (Fuel Cell) and ATA 24 (Electrical)

## Area of Responsibility

| Role | Stakeholder |
|------|-------------|
| Design authority | C2 Systems Team (STK_ENG) |
| Safety oversight | STK_SAF |
| Configuration management | STK_CM |

## Boundaries

- Upstream: GENESIS/ (uncertainty discovery layer)
- Downstream: Subject folders under `28-00-00-general-general/`
- Interface: ATA 28-10 (storage), ATA 71 (fuel cell interface)

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `GENESIS/` | Uncertainty discovery — O-KNOTs and Y-KNOTs |
| `28-00-00-general-general/` | Subject-level lifecycle artifacts (KDB, IDB, CONTRACTS) |
| `SECTION_INDEX.yaml` | Section-level artifact index and metrics |
