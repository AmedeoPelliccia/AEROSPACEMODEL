# Contracts — ATA 28-10-00 Fuel Storage General

## Contract-First Governance

All KDB→IDB transformations in this subject execute **only** under an approved
contract. No pipeline may produce publication artifacts without a valid,
version-controlled contract on file.

## Available Contract Types

| Type | Description |
|------|-------------|
| **CSDB Publication** | KDB→CSDB S1000D data module generation |
| **Export** | CSDB→PDF/HTML rendering |
| **IETP** | CSDB→Interactive Electronic Technical Publication packaging |
| **Service Bulletin** | SB issuance and distribution |
| **Repair** | Repair authorization and disposition |
| **Query** | Technical query resolution |
| **COC** | Certificate of Conformance generation |

## Enforcement

ASIT validates the referenced contract before any pipeline step executes.
If the contract is missing, expired, or unapproved, the pipeline **halts**
and raises a contract violation.

See `CONTRACT_APPROVAL_LOG.csv` for current approval status.
