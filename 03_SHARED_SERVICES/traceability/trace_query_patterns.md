# Trace Query Patterns — AEROSPACEMODEL

**Path:** `03_SHARED_SERVICES/traceability/trace_query_patterns.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Standard Query Patterns

1. **Forward trace**: Requirement → KNOT → KNU → Evidence
2. **Backward trace**: Evidence → KNU → KNOT → Requirement
3. **Compliance coverage**: Clause → all linked KNUs → compliance status
4. **Orphan detection**: All KNUs without a KNOT reference
5. **Phase completeness**: All KNOTs in phase without COMPLIANT status
