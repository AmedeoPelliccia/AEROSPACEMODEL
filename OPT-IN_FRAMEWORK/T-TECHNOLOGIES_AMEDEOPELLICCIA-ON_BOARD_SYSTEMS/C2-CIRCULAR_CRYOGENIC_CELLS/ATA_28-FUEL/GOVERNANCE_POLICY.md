# ATA 28 – Governance Policy

> Default baseline policy for ATA 28 Fuel System (LH₂) configuration management.

---

## 1. Baseline Types

| Baseline | Acronym | Established At | Contents |
|----------|---------|----------------|----------|
| Functional Baseline | FBL | LC02 – Requirements Review | Approved requirements set |
| Design Baseline | DBL | LC04 – Critical Design Review | Approved design package |
| Product Baseline | PBL | LC10 – Production Readiness | Approved production configuration |

Each baseline is immutable once established. Changes require a formal ECR/ECO
approved by the appropriate authority.

## 2. Change Authority

| Scope | Authority | Approval Mechanism |
|-------|-----------|-------------------|
| Baseline changes (FBL, DBL, PBL) | CCB (Configuration Control Board) | ECR → impact assessment → CCB vote |
| Safety-critical changes | STK_SAF (Safety Engineer) | Mandatory safety review before CCB |
| Non-baseline editorial changes | STK_CM (Configuration Manager) | Direct approval, logged |

All changes to baselined artifacts follow the ECR/ECO process:

1. **ECR** – Engineering Change Request (identifies the change need)
2. **Impact Assessment** – technical, safety, schedule, cost evaluation
3. **CCB Decision** – approve, reject, or defer
4. **ECO** – Engineering Change Order (implements the approved change)

## 3. Approval Gates

| Gate | Lifecycle Phase | Key Reviews |
|------|----------------|-------------|
| PDR | LC03 – Preliminary Design | Requirements completeness, trace coverage |
| CDR | LC04 – Detailed Design | Design maturity, FHA/FMEA alignment |
| TRR | LC06 – Verification | Test readiness, test-to-requirement trace |
| FRR | LC08 – Certification | Flight readiness, all evidence packages |

Gate passage requires:
- All mandatory traces satisfied (see TRACEABILITY_CONVENTIONS.md)
- No open critical/major findings
- BREX compliance verification passed

## 4. Hydrogen-Specific Escalation

Due to the safety-critical nature of hydrogen fuel systems:

| Trigger | Escalation Target | Timeout |
|---------|-------------------|---------|
| Any H₂ anomaly (leak, pressure, thermal) | STK_SAF | 72 hours |
| Cryogenic procedure change | STK_SAF | 72 hours |
| H₂ safety content generation | STK_SAF | 72 hours |
| Undefined safety condition | STK_CM → CCB | HALT until resolved |

All H₂-related anomalies **must** be escalated to STK_SAF within 72 hours.
Failure to escalate is a **BREX Safety Violation** (SAFETY-H2-001).

## 5. BREX Contract Requirement

All content generation, transformation, and publication for ATA 28 requires
an active BREX contract:

- **Contract:** `KITDM-CTR-LM-CSDB_ATA28`
- **H₂-specific:** `KITDM-CTR-LM-CSDB_ATA28_H2`
- **Enforcement:** AUTHOR-002 (block without contract)

No ATA 28 content may be produced without a valid, ASIT-approved contract.

## 6. Audit and Retention

| Item | Retention Period | Format |
|------|-----------------|--------|
| Baseline records | 7 years minimum | Controlled repository |
| ECR/ECO records | 7 years minimum | Controlled repository |
| Safety assessments | 7 years minimum | Controlled repository |
| Audit logs | 7 years minimum | Timestamped, immutable |
| Trace matrices | 7 years minimum | CSV or structured data |

Audit log format:
```
{timestamp} | RULE {rule_id} | {rule_name} | {status} | {context}
```

---

*Governed by ASIT. This policy is subject to CCB approval for any modification.*
