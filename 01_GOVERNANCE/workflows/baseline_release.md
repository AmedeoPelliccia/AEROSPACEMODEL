# Baseline Release Workflow — AEROSPACEMODEL

**Path:** `01_GOVERNANCE/workflows/baseline_release.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Steps

1. Prepare release candidate branch
2. Run CI validation (`validate_structure.yml`, `validate_mappings.yml`, `validate_evidence.yml`)
3. Generate compliance dashboard
4. ASIT review of dashboard
5. QA Authority sign-off
6. Certification Authority sign-off (if applicable)
7. Tag release in repository
8. Update `CHANGELOG.md`
9. Archive baseline snapshot
