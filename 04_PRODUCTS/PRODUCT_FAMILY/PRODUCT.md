# PRODUCT_FAMILY — Product Definition

**Path:** `04_PRODUCTS/PRODUCT_FAMILY/PRODUCT.md`  
**Authority:** ASIT  
**Status:** DRAFT

---

## Purpose

This file defines the product family governed under AEROSPACEMODEL.

Replace `PRODUCT_FAMILY` with the actual product family name.

## Product Taxonomy

The AEROSPACEMODEL product taxonomy distinguishes first between **crewed craft**,
**uncrewed craft**, and **stations**. There are three primary operational families:

| Craft class    | Family     | Description                                               |
| -------------- | ---------- | --------------------------------------------------------- |
| CRAFT_CREWED   | **AMPEL**    | Family of crewed aerospace craft                          |
| CRAFT_UNCREWED | **ROBBBO-T** | Family of uncrewed aerospace craft                        |
| STATIONS       | **GAIA**     | Family of stations and fixed/semi-fixed infrastructure    |

### Taxonomy levels

1. **Product type** — What is it? (`CRAFT_CREWED`, `CRAFT_UNCREWED`, `STATIONS`)
2. **Family/framework identity** — To which main family does it belong? (`AMPEL`, `ROBBBO-T`, `GAIA`)
3. **Programme** — Which concrete programme is it? (e.g., Q100, AQUA-V, orbital node)
4. **Execution structure** — How is the work organized? (work packages, deliverables, etc.)

### Canonical path template

```text
04_PRODUCTS/PRODUCT_FAMILY/{CRAFT_CREWED|CRAFT_UNCREWED|STATIONS}/{AMPEL|ROBBBO-T|GAIA}/programmes/{PROGRAMME}/work_packages/
```

## Product Family Description

<Product family description.>

## Variants

See `variants/` for product variant instances.

## Programmes

Programmes are organized by craft class and family identity:

- `CRAFT_CREWED/AMPEL/programmes/` — crewed craft programmes
- `CRAFT_UNCREWED/ROBBBO-T/programmes/` — uncrewed craft programmes
- `STATIONS/GAIA/programmes/` — station programmes
