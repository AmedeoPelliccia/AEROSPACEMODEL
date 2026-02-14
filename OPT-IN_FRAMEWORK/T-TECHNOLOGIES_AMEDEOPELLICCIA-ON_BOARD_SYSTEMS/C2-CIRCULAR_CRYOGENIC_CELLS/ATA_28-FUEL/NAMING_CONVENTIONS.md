# ATA 28 – Naming Conventions

> ID grammar rules for all ATA 28 Fuel System (LH₂) artifacts.

---

## 1. SSOT ID

Single Source of Truth identifier for configuration items.

```
SSOT-Q100-C2-NNN
```

- `Q100` – Aircraft programme (AMPEL360 Q100)
- `C2` – Technology domain (Circular Cryogenic Cells)
- `NNN` – Sequential number (001–999)

## 2. Requirement ID

```
REQ-Q100-C2-NNN
```

Requirements are linked 1:1 to an SSOT item and traced through the lifecycle.

## 3. KNOT ID (Knowledge Node of Technology)

```
KNOT-ATA28-yy-zz-NNN
```

- `yy` – Sub-system code (e.g., 11 = LH₂ Storage Tanks)
- `zz` – Unit/assembly code (e.g., 00 = general)
- `NNN` – Sequential number

## 4. KNU ID (Knowledge Node Unit)

```
KNU-ATA28-yy-zz-NNN-KK
```

- Inherits the parent KNOT prefix
- `KK` – Unit index within the KNOT (01–99)

## 5. Data Module Code (S1000D)

```
DMC-Q100-A-28-yy-zz-00A-xxxA-A
```

| Segment | Meaning |
|---------|---------|
| `Q100` | Model identification code |
| `A` | System difference code |
| `28` | System code (ATA 28 – Fuel) |
| `yy` | Sub-system code |
| `zz` | Sub-sub-system / unit code |
| `00A` | Assembly code + variant |
| `xxx` | Information code (e.g., 040 = description, 520 = removal) |
| `A` | Information code variant |
| `A` | Item location code |

## 6. Change Control IDs

| Type | Format | Example |
|------|--------|---------|
| ECR | `ECR-Q100-C2-YYYYMMDD-NN` | ECR-Q100-C2-20250715-01 |
| ECO | `ECO-Q100-C2-YYYYMMDD-NN` | ECO-Q100-C2-20250715-01 |

## 7. Controlled Vocabulary

Use these standard abbreviations consistently across all artifacts:

| Abbreviation | Meaning |
|--------------|---------|
| LH₂ | Liquid Hydrogen |
| BOG | Boil-Off Gas |
| MLI | Multi-Layer Insulation |
| PEM | Proton Exchange Membrane |
| AFDX | Avionics Full-Duplex Switched Ethernet |
| PPE | Personal Protective Equipment |
| FHA | Functional Hazard Assessment |
| FMEA | Failure Mode and Effects Analysis |

## 8. Slug Format Rules

For file names, folder names, and URL-safe identifiers:

- **Lowercase only** – `lh2-storage-tank`, not `LH2_Storage_Tank`
- **Hyphens as separators** – `boil-off-management`, not `boil_off_management`
- **No spaces** – never use spaces in identifiers
- **No special characters** – alphanumeric and hyphens only
- **ATA prefix** – folders use `28-yy-description` (e.g., `28-10-storage`)

---

*All identifiers are immutable once baselined. Changes require an ECR/ECO.*
