# Acceptance Criteria — ATA 28-10-00 Fuel Storage General

Each ASIT pipeline run must satisfy **all** criteria below to produce a
releasable IDB artifact.

| # | Criterion | Threshold | Pass/Fail |
|---|-----------|-----------|-----------|
| 1 | BREX compliance | 100 % — zero violations | |
| 2 | S1000D schema validation | All DMs pass XSD validation | |
| 3 | Trace coverage | ≥ 95 % of input artifacts traced to output | |
| 4 | Hydrogen safety warnings | All mandatory H₂ warnings included | |
| 5 | Cryogenic safety warnings | All mandatory cryogenic warnings included | |

## Failure Handling

If any criterion fails, the pipeline **halts**. The run is logged as
`FAILED` in `ASIT/runs/` and no artifacts are promoted to IDB.

Corrective action requires a new ASIT run after the root cause is resolved.
