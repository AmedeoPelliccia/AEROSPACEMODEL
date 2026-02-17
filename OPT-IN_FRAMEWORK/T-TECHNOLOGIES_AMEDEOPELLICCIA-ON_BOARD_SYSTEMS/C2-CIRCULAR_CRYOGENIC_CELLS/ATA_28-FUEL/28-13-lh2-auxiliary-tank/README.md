# 28-13 — LH₂ Auxiliary Tank (LH₂ Circular Cryogenic Cells)

**ATA Section:** 28-13
**System:** AMPEL360 Q100 — C2 Circular Cryogenic Cells
**Compliance:** S1000D Issue 5.0, CS-25 Special Conditions, ARP4754A, ARP4761

## Scope

This section covers the **lh₂ auxiliary storage tank** subsystem for liquid hydrogen (LH₂) circular cryogenic cells:

- Auxiliary/extended-range cryogenic storage tank
- Auxiliary tank structural design and certification
- Integration with primary tank fuel management
- Auxiliary tank insulation and thermal performance

## Area of Responsibility

| Role | Stakeholder |
|------|-------------|
| Design authority | C2 Systems Team (STK_ENG) |
| Safety oversight | STK_SAF |
| Configuration management | STK_CM |

## Boundaries

- Upstream: GENESIS/ (uncertainty discovery layer)
- Downstream: Subject folders under `28-13-00-lh2-auxiliary-tank-general/`
- Interface: ATA 28-10 (storage), ATA 71 (fuel cell interface)

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `GENESIS/` | Uncertainty discovery — O-KNOTs and Y-KNOTs |
| `28-13-00-lh2-auxiliary-tank-general/` | Subject-level lifecycle artifacts (KDB, IDB, CONTRACTS) |
| `SECTION_INDEX.yaml` | Section-level artifact index and metrics |
