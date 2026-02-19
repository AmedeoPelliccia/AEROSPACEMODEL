# ATA 26 – Naming Conventions

> ID grammar rules for all ATA 26 Fire Protection artifacts.

---

## 1. SSOT ID

Single Source of Truth identifier for configuration items.

```
SSOT-Q100-E1-NNN
```

- `Q100` – Aircraft programme (AMPEL360 Q100)
- `E1` – Technology domain (Environment)
- `NNN` – Sequential number (001–999)

## 2. Requirement ID

```
REQ-Q100-E1-NNN
```

Requirements are linked 1:1 to an SSOT item and traced through the lifecycle.

## 3. KNOT ID (Knowledge Node of Technology)

```
KNOT-ATA26-yy-zz-NNN
```

- `yy` – Sub-system code (e.g., 11 = Fire Detection)
- `zz` – Unit/assembly code (e.g., 00 = general)
- `NNN` – Sequential number

## 4. KNU ID (Knowledge Node Unit)

```
KNU-ATA26-yy-zz-NNN-KK
```

- Inherits the parent KNOT prefix
- `KK` – Unit index within the KNOT (01–99)

## 5. Data Module Code (S1000D)

```
DMC-Q100-A-26-yy-zz-00A-xxxA-A
```

| Segment | Meaning |
|---------|---------|
| `Q100` | Model identification code |
| `A` | System difference code |
| `26` | System code (ATA 26 – Fire Protection) |
| `yy` | Sub-system code |
| `zz` | Sub-sub-system / unit code |
| `00A` | Assembly code + variant |
| `xxx` | Information code (e.g., 040 = description, 520 = removal) |
| `A` | Information code variant |
| `A` | Item location code |

## 6. Change Control IDs

| Type | Format | Example |
|------|--------|---------|
| ECR | `ECR-Q100-E1-YYYYMMDD-NN` | ECR-Q100-E1-20260215-01 |
| ECO | `ECO-Q100-E1-YYYYMMDD-NN` | ECO-Q100-E1-20260215-01 |

## 7. Controlled Vocabulary

Use these standard abbreviations consistently across all artifacts:

| Abbreviation | Meaning |
|--------------|---------|
| H₂ | Hydrogen |
| FD | Fire Detection |
| OH | Overheat |
| AESS | Aircraft Equipment and System Supplying |
| LOX | Liquid Oxygen |
| PPE | Personal Protective Equipment |
| FHA | Functional Hazard Assessment |
| FMEA | Failure Mode and Effects Analysis |

## 8. Slug Format Rules

For file names, folder names, and URL-safe identifiers:

- **Lowercase only** – `fire-detection`, not `Fire_Detection`
- **Hyphens as separators** – `cargo-suppression`, not `cargo_suppression`
- **No spaces** – never use spaces in identifiers
- **No special characters** – alphanumeric and hyphens only
- **ATA prefix** – folders use `26-yy-description` (e.g., `26-11-fire-detection`)

---

*All identifiers are immutable once baselined. Changes require an ECR/ECO.*
