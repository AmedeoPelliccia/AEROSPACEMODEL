# IETP Runtime — AMM

## ATA 28-10-00 Fuel Storage General

Interactive Electronic Technical Publication deployment for the AMM.

## Structure

| Directory | Description |
|-----------|-------------|
| `app/` | IETP viewer application code and assets |
| `data/` | Pre-processed S1000D content optimised for interactive delivery |
| `operators/` | Operator-specific configuration overlays and branding |

## Deployment

The IETP runtime is packaged by the `KITDM-CTR-LM-IETP_ATA28-10-00`
contract. Content in `data/` is derived from `CSDB/` data modules and
must pass all BREX and safety validation gates before packaging.
