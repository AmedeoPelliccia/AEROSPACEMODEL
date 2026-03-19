# Model Release Policy — AEROSPACEMODEL

**Path:** `01_GOVERNANCE/policies/model_release_policy.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Purpose

Defines the process for releasing model versions and baselines.

## Rules

1. Releases follow semantic versioning: MAJOR.MINOR.PATCH.
2. All releases must pass CI validation gates defined in `08_AUTOMATION/ci/release_gates.yaml`.
3. Releases must be tagged in the repository.
4. Release notes must be recorded in `CHANGELOG.md`.
5. ASIT sign-off is required for MAJOR releases.
