# ATA 26 – Fire Protection

> **Aircraft:** AMPEL360 Q100 Hydrogen-Electric  
> **Technology Domain:** E1-ENVIRONMENT  
> **ATA Chapter:** 26 – Fire Protection  
> **Authority:** ASIT / BREX Profile AEROSPACEMODEL-PRJ-01  
> **Compliance:** S1000D Issue 5.0, DO-160, CS-25, ARP4754A, ARP4761

---

## 1. Mission

Provide a comprehensive fire detection, prevention, and suppression system for the AMPEL360 Q100 hydrogen-electric aircraft. The system protects critical aircraft zones including cargo compartments, lavatories, engine nacelles, and hydrogen fuel system interfaces against fire hazards.

## 2. Scope

| Area | Coverage |
|------|----------|
| Fire Detection | Smoke, heat, and flame detection in all protected zones (26-11, 26-21) |
| Fire Suppression | Extinguishing systems for cargo, engine, and APU compartments (26-30, 26-40) |
| H₂ Safety Integration | Fire protection for hydrogen fuel system interfaces (26-41) |
| Portable Equipment | Hand-held fire extinguishers and protective equipment (26-50) |
| Indication & Warning | Flight deck and cabin crew alerting systems (26-60) |
| Testing & Maintenance | System integrity checks and periodic testing (26-70) |

## 3. Navigation

| Folder | Contents |
|--------|----------|
| [WBS/](WBS/) | Work Breakdown Structure and task packages |
| [GOVERNANCE/](GOVERNANCE/) | Baseline policy, change authority, approval gates |
| [INDEX/](INDEX/) | Master index of KNOTs, KNUs, requirements, and data modules |
| [26-00-general/](26-00-general/) | Fire Protection — General |
| [26-11-fire-detection/](26-11-fire-detection/) | Fire/smoke detection systems |
| [26-21-overheat-detection/](26-21-overheat-detection/) | Overheat detection and warning |
| [26-30-cargo-suppression/](26-30-cargo-suppression/) | Cargo compartment fire suppression |
| [26-40-engine-suppression/](26-40-engine-suppression/) | Engine/APU fire suppression |
| [26-41-h2-fire-protection/](26-41-h2-fire-protection/) | Hydrogen system fire protection |
| [26-50-portable-equipment/](26-50-portable-equipment/) | Portable fire extinguishers |
| [26-60-indication-warning/](26-60-indication-warning/) | Fire warning and indication systems |
| [26-70-system-testing/](26-70-system-testing/) | Fire protection system testing |

## 4. Key Contacts

| Role | Stakeholder Code | Responsibility |
|------|-------------------|----------------|
| Program Manager | STK_PM | Schedule, budget, deliverables |
| Systems Engineer | STK_SE | System design and integration |
| Safety Engineer | STK_SAF | Safety assessment, fire hazard review |
| Configuration Manager | STK_CM | Baseline control, change management |

## 5. Special Conditions

| ID | Title | Description |
|----|-------|-------------|
| SC-26-H2-001 | Hydrogen Fire Protection | Special conditions for fire protection in H₂ environments |
| SC-26-DETECT-002 | Detection Response Time | Enhanced detection requirements for H₂-related fire hazards |
| SC-26-SUPP-003 | Suppression Agent Compatibility | Suppression agent compatibility with hydrogen systems |
| SC-26-MATERIAL-004 | Fire-Resistant Materials | Material flammability requirements for H₂ aircraft |

These special conditions apply in addition to CS-25 standard requirements.

## 6. Technology Domain

- **Domain:** E1-ENVIRONMENT
- **Classification:** Standard Technology with H₂ Adaptations
- **Lifecycle Activation:** Full LC01 – LC14
- **BREX Contract:** KITDM-CTR-LM-CSDB_ATA26
- **Determinism Level:** STRICT

All content generation, transformation, and publication for this ATA chapter is
governed by BREX decision rules. No free-form autonomy is permitted.

## 7. Applicable Standards

| Standard | Application |
|----------|-------------|
| S1000D Issue 5.0 | Technical data structure and exchange |
| DO-160 | Environmental qualification |
| ARP4754A | System development assurance |
| ARP4761 | Safety assessment (FHA, FMEA, FTA) |
| CS-25 + Special Conditions | Airworthiness certification |
| NFPA 2 | Hydrogen technologies code — aircraft fire protection |
| SAE AS8026 | Minimum performance standard for fire detectors |
| SAE AS8031 | Minimum performance standard for fire extinguishing agents |
| ISO 2685 | Aircraft – Environmental test procedures |

## 8. Quick Reference

```
System Code:    26
Sub-systems:    00, 11, 21, 30, 40, 41, 50, 60, 70
DMC prefix:     DMC-Q100-A-26-
SSOT prefix:    SSOT-Q100-E1-
KNOT prefix:    KNOT-ATA26-
```

---

*Governed by ASIT. All changes require CCB approval per GOVERNANCE_POLICY.md.*
