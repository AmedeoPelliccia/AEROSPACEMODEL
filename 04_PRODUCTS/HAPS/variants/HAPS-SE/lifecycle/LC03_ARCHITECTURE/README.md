# LC03 — HAPS-SE Architecture

**Path:** `04_PRODUCTS/HAPS/variants/HAPS-SE/lifecycle/LC03_ARCHITECTURE/README.md`  
**Lifecycle Phase:** LC03  
**Variant:** HAPS-SE  
**Status:** IN_PROGRESS

---

## Phase Purpose

Define and baseline the system architecture for HAPS-SE, including the functional and physical decomposition, interface definitions, and ATA chapter assignments.

## Status Summary

| Item | Status |
|------|--------|
| KNOTS defined | ☑ |
| KNUs planned | ☑ |
| Evidence collected | ☐ |
| Audit complete | ☐ |
| Phase closed | ☐ |

## Architecture Overview

```
Airframe (ATA 51–57) — Ultra-high AR, twin-boom, composite
├── Wing (ATA 57)          → Solar array substrate, AR > 25, flex spar
│                             feeds into ↓
├── Energy (ATA 24+28)     → Solar cells + battery buffer; day/night cycle management
├── Propulsion (ATA 61+71) → 4× distributed electric propellers
├── Payload (ATA 46)       → Comms / EO / ISR
└── Tail (ATA 55)          → Twin-boom, H-tail
```
