# TS-28-10-TS02 — Distributed Small Cells vs Single Large Tank

| Key | Value |
|-----|-------|
| Trade Study ID | TS-28-10-TS02 |
| ATA Code | 28-10-00 |
| Technology Domain | C2 — Circular Cryogenic Cells |
| Aircraft Programme | AMPEL360 Q100 |
| Lifecycle Phase | LC04 (Design Definition) |
| Status | Preliminary |
| Author | STK_ENG |
| Date | 2026-02-14 |

## Objective

Evaluate storage architectures for LH₂ fuel system comparing
single-tank, dual-symmetric, and multi-cell distributed
configurations for CG stability, redundancy, structural impact,
and safety.

---

## Options Considered

| Option | Name | CG Stability | Redundancy | Structural Impact | Safety |
|--------|------|--------------|------------|-------------------|--------|
| A | Single Large Tank | Stable (central) | Low | Heavy reinforcement | Medium |
| B | Dual Symmetric Tanks | Very Good | Medium | Balanced | Good |
| C | Multi-Cell Distributed | Excellent | High | Load distributed | Very High |

### Option C — Multi-Cell Distributed (detailed analysis)

- **Zonal isolation:** Fire / leak containment
- **Selective venting:** Yes
- **Survivability:** Improved
- **BWB compatibility:** Compatible with BWB volume distribution
- **Boil-off management:** Simplified hydrogen boil-off management
- **Mass trade-off:** +2–5 % plumbing complexity
- **Safety gain:** Significant

---

## Preliminary Selection

**Selected Option:** C — Multi-Cell Distributed
**Baseline Name:** Distributed Circular Cryogenic Cells

### Rationale

- Aligned with ZNNN 600–699 hazard zoning
- Aligned with modular propulsion architecture (500–599)
- Deterministic isolation logic (5D system state s-dimension)

---

## Feeds

| Lifecycle | Artifact |
|-----------|----------|
| LC03 | Safety FHA update (ATA 28 + 26 crosslink) |
| LC05 | Mass model update (WBS level 3) |

## Traceability

- **Derives from:** WP-28-03
