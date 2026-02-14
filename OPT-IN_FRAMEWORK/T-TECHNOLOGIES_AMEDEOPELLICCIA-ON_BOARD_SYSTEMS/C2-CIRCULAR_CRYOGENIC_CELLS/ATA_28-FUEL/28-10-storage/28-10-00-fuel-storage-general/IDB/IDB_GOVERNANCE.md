# IDB Governance — ATA 28-10-00 Fuel Storage General

## Derivation Rule

The IDB is **derived** from the KDB — it is never authored directly.
All publication content originates in the Knowledge Database and is
transformed through ASIT pipelines under contract governance.

## Release Requirements

An IDB release requires:

1. **Contract execution** — a valid, approved contract must govern the
   transformation.
2. **BREX compliance** — 100 % pass rate, zero violations.
3. **Trace verification** — ≥ 95 % coverage from input to output artifacts.

## Change Control

IDB content may only change through:

- A **new ASIT run** that re-generates artifacts from updated KDB sources.
- An **approved ECO** (Engineering Change Order) processed through
  `GOVERNANCE/CHANGE_CONTROL/`.

Direct edits to IDB files are prohibited.
