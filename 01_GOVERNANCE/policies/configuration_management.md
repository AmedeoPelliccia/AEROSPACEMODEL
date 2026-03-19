# Configuration Management Policy — AEROSPACEMODEL

**Path:** `01_GOVERNANCE/policies/configuration_management.md`  
**Authority:** ASIT  
**Status:** ACTIVE

---

## Purpose

Defines the rules for configuration management within AEROSPACEMODEL.

## Scope

All configuration items (CIs) under repository governance.

## Rules

1. All CIs must be registered in the product variant's `configuration/configuration_baseline.yaml`.
2. Changes to baselined CIs require a formal Change Request (CR).
3. Effectivity rules must be defined in `configuration/effectivity_rules.yaml`.
4. All changes must be logged in `configuration/change_log.csv`.
5. Baseline types (AS_DESIGNED, AS_VERIFIED, AS_BUILT, AS_CERTIFIED, AS_OPERATED) must be formally declared.
