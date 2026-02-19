# Filing Strategy — AQUA-V Patent Portfolio

**Portfolio:** AQUA-V (QAPD + QAOS)  
**Authority:** ASIT / CCB  
**Version:** 1.0  
**Date:** 2026-02-19

---

## 1. Strategic Objective

Secure broad, defensible patent protection for the AQUA-V architecture in the jurisdictions most relevant to aerospace certification (EU/EASA, US/FAA) and future commercial deployment, while managing cost and prosecution risk.

---

## 2. Jurisdiction Analysis

### 2.1 Primary Jurisdictions

| Jurisdiction | Rationale | Filing Vehicle |
|---|---|---|
| **United States** | Largest aerospace market; USPTO allows method + system + CRM claims in single application | US Provisional → US Non-Provisional |
| **European Patent Office (EPO)** | EASA-aligned market; single grant covering 38+ EPC states | PCT → EP national phase |
| **United Kingdom** | Post-Brexit UKIPO; separate filing required; Airbus, Rolls-Royce key partners | PCT → UK national phase |

### 2.2 Secondary Jurisdictions (Phase 2)

| Jurisdiction | Rationale | Timeline |
|---|---|---|
| **Canada** | Bombardier; growing aerospace cluster | Month 30 via PCT |
| **Japan** | JAXA partnerships; Mitsubishi aerospace | Month 30 via PCT |
| **South Korea** | KAI; Samsung aerospace division | Month 30 via PCT |
| **Australia** | Growing space/aerospace sector | Month 30 via PCT |

---

## 3. Recommended Filing Path

### Phase 1 — Priority Establishment (Months 0–1)

**Step 1.1: US Provisional for P0 (Month 0)**
- File a US Provisional Application covering the full AQUA-V parent architecture
- Establishes a 12-month priority date for all child applications
- Cost: ~$3,500 (attorney fees + USPTO fees)
- Provisional need not contain formal claims — technical disclosure sufficient

**Step 1.2: US Provisionals for C1.2 + C2.1 (Month 0–1)**
- C1.2 (Deterministic Reproducibility): strongest novel claim, file within 7 days of P0
- C2.1 (Resource Orchestrator): backed by existing QAOS.py implementation
- Both can reference P0 provisional for continuity

### Phase 2 — PCT Umbrella (Month 12)

**Step 2.1: PCT Application (one or combined)**
- File PCT application(s) claiming priority from Phase 1 provisionals
- Designates all PCT member states (~157 countries)
- International Search Report (ISR) from EPO as International Searching Authority
- 18-month publication from priority date
- Cost: ~$5,000–$8,000 per PCT filing

**Step 2.2: Recommended structure**
- Option A: Single PCT for P0 (broadest claims) → continuation strategy for children
- Option B: Separate PCTs for P0, C1.2, C2.1 (stronger protection, higher cost)
- **Recommendation: Option A for cost efficiency; file C1.2 and C2.1 as children of PCT P0**

### Phase 3 — National Phase Entry (Month 30)

**Priority entries:**
1. US Non-Provisional (claim benefit of Provisional + PCT)
2. EP application via EPO (designate DE, FR, GB, NL, ES)
3. UK national phase (separate post-Brexit)

### Phase 4 — Continuation-in-Part (Ongoing)

- C3.1 (LH₂ Tank Topology): file as CIP when BWB-H₂ structural design matures
- C3.2 (Flight Energy Optimisation): file as CIP after first simulation validation
- C4.x: file as divisionals or independents as commercial interest develops

---

## 4. PCT vs EP-First vs US-Provisional Decision Matrix

| Factor | US Provisional First | EP-First | PCT Umbrella |
|---|---|---|---|
| **Cost at Month 0** | Low (~$3.5k) | High (~$15k) | Medium (~$8k) |
| **Coverage at Month 0** | US only (1 year) | EP states only | Global (pending) |
| **Flexibility** | High — 12 months to refine claims | Low — EP claims fixed earlier | High — 18 months |
| **ISR quality** | USPTO (variable) | EPO (high quality) | EPO (if selected as ISA) |
| **Recommended for AQUA-V** | ✅ Phase 1 entry point | ❌ Too expensive too early | ✅ Phase 2 |

**Decision: US Provisional first → PCT at month 12 → EP + US national phase at month 30.**

---

## 5. EPO-Specific Considerations

### Technical Effect Requirement (Art. 52 EPC)
AQUA-V claims must demonstrate a **technical effect** beyond the mental act. Key framing:
- "Deterministic cryptographic evidence record enabling bit-exact reconstruction" — technical, not abstract
- "Latency-bounded backend selection for safety-critical real-time workloads" — measurable technical constraint
- Avoid framing as business method or mathematical method per se

### Software/AI Claims (EPO Guidelines, G 1/19)
- Method claims that produce a "technical effect going beyond the normal physical interactions between a program and the computer" are allowable
- Frame as: "A computer-implemented method for controlling a quantum processing system to…" rather than "A method of optimising…"

---

## 6. US-Specific Considerations

### § 101 Eligibility (Alice/Mayo)
- Claims must be directed to specific technological implementations, not abstract ideas
- Key safe harbour: tie claims to specific hardware (QPU, cryptographic module, SSOT database)
- Avoid method claims that read on pure mental steps

### Continuation Strategy
- US allows broad continuation practice — file continuation applications to pursue claims not granted in parent
- Keep P0 alive as continuation base for all C1–C4 children

---

## 7. Freedom-to-Operate (FTO) Considerations

**Key risks identified:**
1. D-Wave / IBM / Google quantum computing method patents — avoid apparatus-agnostic method claims
2. Siemens / PTC digital twin patents — differentiate on the certification evidence linkage
3. Airbus / Boeing aerospace optimisation patents — differentiate on hybrid QUBO with cryogenic constraints

**FTO clearance should be completed before national phase entry.**

---

## 8. Provisional Application Strategy

A US Provisional application should include:
1. Technical description matching P0 Invention Disclosure
2. Representative drawings (block diagrams of AQUA-V architecture)
3. At least informal claims (to preserve scope)
4. Code listings from QAOS.py and QUBO encoding modules as supporting disclosure

---

*All filing decisions require CCB approval per BREX rule BL-002. Escalate to STK_CM for undefined conditions.*
