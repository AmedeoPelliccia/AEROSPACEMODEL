# M2 — Maintenance Environments

**Maintenance Ecosystem Infrastructure: Hangars, Line Stations, Component Shops**

---

## Scope

The M2-MAINTENANCE_ENVIRONMENTS subdomain covers the ground-based infrastructure required to maintain, service, and return aircraft to service. This includes leveling and weighing facilities, parking and mooring infrastructure, storage environments, and all servicing equipment and fluid-handling systems.

For AMPEL360 Q100 novel-technology aircraft (hydrogen fuel cell propulsion, cryogenic systems), these environments include **⭐ Special Condition** infrastructure items beyond the conventional MRO baseline.

---

## Subdomain Structure

The M2 subdomain is organized into three ATA-aligned infrastructure categories:

### ATA 08 – Leveling and Weighing Infrastructure
Facilities and equipment for aircraft leveling operations and precise weighing. Includes jacking pads, weighing platforms, optical leveling systems, and center-of-gravity computation infrastructure.

### ATA 10 – Parking, Mooring, Storage, and RTS Infrastructure
Ground infrastructure for aircraft parking, mooring, and long-term storage, including return-to-service (RTS) checks. Special conditions apply for H₂ aircraft storage environments.

### ATA 12 – Servicing Infrastructure
Full-spectrum servicing infrastructure: ground power, pneumatic start, hydraulic servicing, potable water, waste, tire inflation, and **⭐ cryogenic hydrogen (LH₂) fueling systems**.

---

## ATA Chapter Directories

| ATA | Directory | Description |
|-----|-----------|-------------|
| 08 | `ATA_08-LEVELING_AND_WEIGHING_INFRA/` | Leveling and weighing facilities and equipment |
| 10 | `ATA_10-PARKING_MOORING_STORAGE_RTS_INFRA/` | Parking, mooring, storage, and RTS infrastructure |
| 12 | `ATA_12-SERVICING_INFRA/` | Servicing equipment, fluid handling, and H₂ fueling ⭐ |

---

## Novel Technology Infrastructure

### ⭐ Special Conditions

The AMPEL360 Q100 introduces special maintenance environment requirements not present in conventional aircraft:

- **Hydrogen Safety Zones**: All maintenance areas must comply with ATEX/IECEx zoning for hydrogen (H₂ concentration 4–75% flammable range).
- **Cryogenic Handling**: LH₂ fueling infrastructure at -253°C requires dedicated cryogenic-rated equipment, PPE, and trained personnel.
- **Weight Variability**: LH₂ density varies significantly with temperature; center-of-gravity computation must account for fuel state.
- **Extended Storage**: Long-term storage of H₂ aircraft requires boil-off management and pressure monitoring.

---

## Lifecycle Applicability

| LC Phase | Applicability | Notes |
|----------|--------------|-------|
| LC04 | Infrastructure design and specification | Equipment design, facility layout |
| LC06 | Infrastructure verification | Commissioning, acceptance tests |
| LC08 | Certification (where applicable) | Regulatory approval for novel infra |
| LC10 | Deployment | Production/operational deployment |
| LC11 | Customer integration | Airline facility adaptation |
| LC12 | Maintenance | Infrastructure upkeep and upgrades |

---

## Cross-References

| System | Reference |
|--------|-----------|
| ATA 28 – H₂ Cryogenic Fuel Systems | `T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/` |
| ATA 71 – Fuel Cell Power Plant | `T-TECHNOLOGIES_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/` |
| O-OPERATIONS (ATA IN – H₂ GSE) | `O-OPERATIONS_SERVICE_STRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN/` |
| I-INFRASTRUCTURES Main README | `../README.md` |

---

## Related Documents

- [I-INFRASTRUCTURES README](../README.md)
- [I-INFRASTRUCTURES Index](../00_INDEX.md)
- [ATA 28 H₂ Cryogenic Instructions](../../../.github/instructions/ata28_h2_cryogenic.instructions.md)
- [ATA 71 Fuel Cell Instructions](../../../.github/instructions/ata71_fuel_cell.instructions.md)

---

*⭐ = Novel Technology Special Condition infrastructure for hydrogen/fuel-cell aircraft*
