# Compliance Propagation Policy — AEROSPACEMODEL

**Path:** `01_GOVERNANCE/policies/compliance_propagation.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Purpose

Defines how compliance status propagates through the traceability chain.

## Rules

1. Compliance status propagates upward: KNU → KNOT → Clause → Phase.
2. A KNOT is COMPLIANT only when all linked KNUs are COMPLIANT.
3. A Phase is COMPLIANT only when all governing KNOTs are COMPLIANT.
4. Partial compliance must be explicitly declared with scope definition.
5. CI validates compliance propagation automatically.
