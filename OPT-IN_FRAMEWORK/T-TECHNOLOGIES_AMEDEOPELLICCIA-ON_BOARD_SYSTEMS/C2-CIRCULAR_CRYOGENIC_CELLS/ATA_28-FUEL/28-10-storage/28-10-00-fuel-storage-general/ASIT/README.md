# ASIT — ATA 28-10-00 Fuel Storage General

## Purpose

The Aircraft Systems Information Transponder (ASIT) automates the
KDB→IDB pipeline for this subject. It validates contracts, executes
transformations, enforces BREX rules, and records every run as an
immutable audit entry.

## Structure

| Path | Description |
|------|-------------|
| `asit_config.yaml` | Global ASIT configuration for this subject |
| `pipelines/` | Pipeline definitions (CSDB generation, export, IETP) |
| `rules/` | BREX and validation rule sets |
| `runs/` | Immutable run records (one directory per execution) |

## Run Lifecycle

1. ASIT reads `asit_config.yaml` and resolves the referenced contract.
2. Contract is validated (existence, version, approval status).
3. Pipeline steps execute in order; each step is logged.
4. Validation gates (BREX, schema, trace, H₂ safety, cryogenic safety)
   are evaluated.
5. On success, artifacts are promoted to `IDB/PUB/`. On failure, the run
   is marked `FAILED` and no artifacts are promoted.

Each run produces an immutable record in `runs/` for audit retention.
