# Engineering SSOT & Custom Information Data Sheet

> **Location:** `OPT-IN_FRAMEWORK/ENGINEERING_SSOT/`  
> **Authority:** ASIT (Aircraft Systems Information Transponder)  
> **Program:** AMPEL360 Q100

---

## Purpose

This directory is the designated front-end posting location for completed
**Engineering SSOT** (Single Source of Truth) entries and
**Custom Information Data Sheets** within the OPT-IN_FRAMEWORK.

All engineering knowledge that reaches SSOT status — whether generated through
the ASIGT pipeline or authored directly — is registered and accessible from
this location.

---

## Contents

| File | Purpose |
|------|---------|
| `index.html` | Interactive front-end for browsing SSOT entries and generating Custom Information Data Sheets |
| `README.md` | This file — directory documentation |
| `00_SSOT_REGISTRY.yaml` | Machine-readable registry of all posted SSOT entries |

---

## What Is Engineering SSOT?

**Engineering SSOT** (Single Source of Truth) is the authoritative, validated
engineering knowledge for the AMPEL360 Q100 program. It represents content that
has passed through the ASIT governance process:

1. **Authored** in the Knowledge Database (KDB)
2. **Validated** against BREX rules and lifecycle gates
3. **Baselined** under an approved baseline (FBL, DBL, or PBL)
4. **Posted** here as the canonical reference

### SSOT Data Flow

```
KDB (Engineering Knowledge)
        │
        ▼
ASIT Governance (Contract + Baseline + BREX)
        │
        ▼
OPT-IN_FRAMEWORK/ENGINEERING_SSOT/  ← You are here
        │
        ▼
ASIGT Pipeline (S1000D generation)
        │
        ▼
IDB (Operational Publications)
```

---

## What Is a Custom Information Data Sheet?

A **Custom Information Data Sheet** (CIDS) is a structured engineering data
entry that captures specific technical information outside the standard
publication pipeline. Use cases include:

- Novel technology specifications (C2, P, I2 domains)
- Special condition compliance evidence
- Cross-domain interface definitions
- Ad-hoc engineering data for review and approval

Each CIDS is generated in YAML format using the `index.html` front-end and
follows the SSOT traceability structure.

---

## Usage

### Viewing the Front-End

Open `index.html` in any web browser to access:
- **SSOT Registry** — browse all posted engineering SSOT entries
- **Custom Information Data Sheet** — generate structured data sheets
- **OPT-IN Domains** — navigate the framework domains
- **Governance** — compliance and reference links

### Generating a Data Sheet

1. Open `index.html`
2. Navigate to the "Custom Information Data Sheet" section
3. Fill in the required fields (ID, title, ATA chapter, domain, etc.)
4. Click "Generate YAML Data Sheet"
5. Copy the output and save as a `.yaml` file in the appropriate KDB location

---

## Governance

- **BREX Compliance:** All SSOT entries must pass BREX validation
- **Baseline Control:** Entries must reference an approved baseline
- **Contract Binding:** Content generation governed by KITDM contracts
- **Safety Escalation:** Safety-critical entries require STK_SAF approval
- **Audit Trail:** All entries logged with 7-year retention

---

## Related Documents

| Document | Path |
|----------|------|
| SSOT Master Index | `ASIT/INDEX/SSOT_INDEX.yaml` |
| Master BREX Authority | `ASIT/GOVERNANCE/master_brex_authority.yaml` |
| LC Phase Registry | `lifecycle/LC_PHASE_REGISTRY.yaml` |
| T-Subdomain Activation | `lifecycle/T_SUBDOMAIN_LC_ACTIVATION.yaml` |
| OPT-IN Framework README | `OPT-IN_FRAMEWORK/README.md` |
| ATA 28 C2 Documentation | `docs/ATA_28_C2_AMPEL360_Q100.md` |

---

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0.0 | 2026-02-14 | ASIT | Initial ENGINEERING_SSOT front-end creation |

---

*End of ENGINEERING_SSOT README*
