# Traceability Rules — AEROSPACEMODEL

**Path:** `00_META/conventions/traceability_rules.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Invariant Traceability Chain

Every governed object must support the following chain:

```
requirement → lifecycle phase → KNOT → KNU → evidence → compliance status → audit signoff → baseline state
```

A missing link constitutes an orphan and is a nonconformance.

## Rules

1. Every KNU must reference at least one KNOT.
2. Every KNOT must reference at least one obligation source (clause, requirement, or governance rule).
3. Every active KNU must have at least one evidence reference or an explicit PENDING status with a target date.
4. Orphan KNUs must be either mapped or explicitly exempted with authority signoff.
5. Cross-standard trace links must be recorded in `cross_standard_trace.csv`.
6. The digital thread must be maintained across lifecycle phase transitions.
