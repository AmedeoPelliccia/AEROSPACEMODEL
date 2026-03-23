# HAPS-SE — Variant Definition

**Path:** `04_PRODUCTS/HAPS/variants/HAPS-SE/HAPS-SE.md`  
**Authority:** ASIT  
**Status:** ACTIVE_BASELINE

---

## Purpose

This file defines the HAPS Solar Electric (HAPS-SE) product variant governed under AEROSPACEMODEL.

HAPS-SE is the baseline solar-electric configuration of the High Altitude Platform Station product family. It is optimised for persistent stratospheric station-keeping using distributed electric propulsion powered entirely by solar energy with battery buffering for night operations.

## Configuration Summary

| Parameter | Value |
|-----------|-------|
| Variant ID | HAPS-SE |
| Product family | HAPS |
| Configuration class | Solar Electric — Solar Array Wing |
| Airframe | Ultra-high aspect ratio, twin-boom, composite |
| Wing aspect ratio | AR > 25 |
| Wing structure | Flex spar with integral solar array substrate |
| Energy system | Solar cells (ATA 24) + battery buffer (ATA 28) |
| Propulsion | 4× distributed electric propellers (ATA 61+71) |
| Tail | Twin-boom, H-tail (ATA 55) |
| Payload | Comms / EO / ISR (ATA 46) |
| Operating altitude | 18–22 km (stratosphere) |
| Endurance target | Weeks to months aloft |
| Baseline status | AS_DESIGNED |

## Configuration

See `configuration/configuration_baseline.yaml` for the controlled baseline record.

## Lifecycle

See `lifecycle/` for phase-by-phase lifecycle records.

| Phase | Code | Status |
|-------|------|--------|
| Problem Statement | LC01 | IN_PROGRESS |
| Requirements | LC02 | IN_PROGRESS |
| Architecture | LC03 | IN_PROGRESS |
| Design Definition | LC04 | OPEN |
| Analysis and Simulation | LC05 | OPEN |
| Verification and Validation | LC06 | OPEN |
| Quality and Assurance | LC07 | OPEN |
| Industrialization and Production | LC08 | OPEN |
| Certification and Compliance | LC09 | OPEN |
| Entry Into Service | LC10 | OPEN |
| Operations | LC11 | OPEN |
| Maintenance and Continued Airworthiness | LC12 | OPEN |
| Modifications and Retrofit | LC13 | OPEN |
| Retirement and End of Life | LC14 | OPEN |

## System Architecture

The HAPS-SE architecture is organised around five primary subsystems:

```
Airframe (ATA 51–57)
├── Wing (ATA 57)          → solar array substrate, AR > 25, flex spar
│   └── feeds →
├── Energy (ATA 24+28)     → solar cells + battery buffer, day/night management
├── Propulsion (ATA 61+71) → 4x electric propellers
├── Payload (ATA 46)       → Comms / EO / ISR
└── Tail (ATA 55)          → twin-boom, H-tail
```

## Mission Definition Parameters

| Parameter | Description | Key Design Drivers |
|-----------|-------------|-------------------|
| Endurance | Weeks – months aloft | Solar harvest sizing, structural fatigue |
| Station-keeping | Wind field, geofence | Propulsion authority, guidance law |
| Energy balance | Solar harvest vs. load | Array area, battery capacity |
| Payload budget | Mass, power, thermal | Wing loading, power margin |
| Altitude selection | 18–22 km optimum | Wind minimum, solar irradiance, regulation |
| Regulatory | ICAO gap, ITU spectrum | UA type certificate, spectrum coordination |
| Structural life | Flutter, UV, thermal | Material selection, fatigue budget |
| Launch / recovery | Transit, ground ops | Portability, launch envelope |
| Data architecture | Downlink, latency | Link margin, processing latency |
