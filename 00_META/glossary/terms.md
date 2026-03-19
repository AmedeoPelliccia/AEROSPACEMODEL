# Terms — AEROSPACEMODEL

**Path:** `00_META/glossary/terms.md`  
**Authority:** ASIT  
**Scope:** Repository-wide  
**Status:** ACTIVE

---

## System Terms

### AEROSPACEMODEL
The Lifecycle Operating System for Aerospace Products.  
A governed, machine-readable environment that structures, traces, validates, and audits aerospace product lifecycle control from concept to retirement.

### Lifecycle Operating System
An operational model that governs lifecycle states, transitions, dependencies, traceability, evidence, and compliance across the aerospace product lifecycle.

### Product
The primary governed object of the repository.  
A product may represent an aircraft, subsystem, equipment item, configuration family, or other controlled aerospace deliverable.

### Variant
A controlled configuration instance of a product family with defined effectivity, baseline state, and lifecycle records.

### Programme
The organized execution context within which one or more products or variants are developed, produced, certified, operated, or sustained.

---

## Governance Terms

### KNOT
A governing control node expressing an obligation, intent, constraint, decision point, or authoritative traceability anchor.

### KNU
A traceable implementation unit linked to one or more KNOTs.  
A KNU may represent an artefact, work item, record, analysis package, validation object, or other executable compliance unit.

### Authority
The recognized governing role empowered to define, approve, validate, or sign off a controlled object.

### ASIT
The authority role responsible for repository traceability integrity, structural consistency, and lifecycle operating coherence.

### Baseline
A formally controlled state of product definition, evidence, or compliance accepted as the reference for further work or operation.

### Effectivity
The rule set defining where, when, or to which configurations a controlled item applies.

### Controlled Object
Any file, record, mapping, evidence item, rule, or model subject to repository governance and validation.

---

## Lifecycle Terms

### Lifecycle Phase
A canonical stage in the evolution of a product represented by `LC01` through `LC14`.

### Lifecycle State
The current control condition of an artefact, obligation, or product object within a defined state model.

### Lifecycle Canon
The repository-wide reference model that defines the canonical lifecycle phases and their semantic purpose.

### Entry Into Service
The controlled transition from certified product state to operational use.

### Continued Airworthiness
The sustained condition in which an aircraft or aerospace product remains compliant and safe for operation after entry into service.

### Retirement
The controlled end-of-life process covering withdrawal, decommissioning, archival closure, and disposal where applicable.

---

## Traceability Terms

### Traceability
The ability to follow a controlled relationship between source obligation, implementation, evidence, compliance state, and signoff.

### Trace Link
A machine-resolvable relation between two controlled objects, such as requirement-to-test or clause-to-KNU.

### Mapping
A structured representation of controlled relationships between obligations, lifecycle phases, governance nodes, implementation units, and evidence.

### Orphan
A controlled object that lacks a required trace relationship, such as a KNU not linked to any governing clause or KNOT.

### Mapping Exempt
A declared state indicating that an object is intentionally outside a specific mapping rule while remaining governed under repository policy.

### Digital Thread
The connected chain of trace links spanning lifecycle phases, configurations, evidence, and governance objects.

---

## Compliance Terms

### Obligation
A requirement, control, or normative expectation imposed by a standard, authority, programme, or internal governance rule.

### Clause
A discrete normative provision within a standard or specification.

### Compliance Status
The controlled state representing the maturity of fulfilment for a mapped obligation.

### Objective Evidence
Verifiable artefact or record demonstrating that an obligation has been implemented, verified, reviewed, or accepted.

### Audit Signoff
A formal confirmation that evidence and control conditions have been reviewed and accepted by the authorized role.

### Nonconformance
Failure to meet a specified requirement, control expectation, or approved baseline condition.

### Corrective Action
Action taken to eliminate the cause of a detected nonconformance or other undesirable condition.

---

## Configuration and Product Data Terms

### Configuration Item
A product element designated for configuration control.

### Configuration Baseline
A formally approved configuration reference defining the accepted state of a product or subsystem at a point in time.

### Change Object
A governed record representing a proposed, approved, implemented, or closed change.

### As-Designed
The defined product state as captured in design data and approved configuration definition.

### As-Built
The realized product state as actually manufactured or assembled.

### As-Certified
The product state accepted for certification purposes based on demonstrated compliance.

### As-Operated
The product state as used in service, including actual operational modifications and constraints.

---

## Evidence Terms

### Evidence Type
A controlled category of objective evidence, such as procedure, test report, audit record, inspection log, or training record.

### Evidence Reference
An addressable identifier, path, or register key pointing to a concrete evidence object.

### Evidence Register
The controlled record of evidence objects available to the repository.
