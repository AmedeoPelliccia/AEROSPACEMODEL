#!/usr/bin/env python3
"""
scaffold_product_variant.py — Scaffold a new product variant
Path: 08_AUTOMATION/scripts/scaffold_product_variant.py
Usage: python3 scaffold_product_variant.py <PRODUCT_FAMILY> <VARIANT> [<CRAFT_CLASS> <FAMILY>]

If CRAFT_CLASS and FAMILY are provided, a programme template is also
scaffolded under the corresponding craft-class/family path.

Valid CRAFT_CLASS values: CRAFT_CREWED, CRAFT_UNCREWED, STATIONS
Valid FAMILY values:      AMPEL, ROBBBO-T, GAIA
"""

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LC_PHASES = [
    'LC01_PROBLEM_STATEMENT', 'LC02_REQUIREMENTS', 'LC03_ARCHITECTURE',
    'LC04_DESIGN_DEFINITION', 'LC05_ANALYSIS_AND_SIMULATION',
    'LC06_VERIFICATION_AND_VALIDATION', 'LC07_QUALITY_AND_ASSURANCE',
    'LC08_INDUSTRIALIZATION_AND_PRODUCTION', 'LC09_CERTIFICATION_AND_COMPLIANCE',
    'LC10_ENTRY_INTO_SERVICE', 'LC11_OPERATIONS',
    'LC12_MAINTENANCE_AND_CONTINUED_AIRWORTHINESS',
    'LC13_MODIFICATIONS_AND_RETROFIT', 'LC14_RETIREMENT_AND_END_OF_LIFE',
]

VALID_CRAFT_CLASSES = {'CRAFT_CREWED', 'CRAFT_UNCREWED', 'STATIONS'}
CRAFT_FAMILY_MAP = {
    'CRAFT_CREWED': 'AMPEL',
    'CRAFT_UNCREWED': 'ROBBBO-T',
    'STATIONS': 'GAIA',
}


def scaffold_variant(product_family, variant):
    base = os.path.join(REPO_ROOT, '04_PRODUCTS', product_family, 'variants', variant)
    for phase in LC_PHASES:
        phase_dir = os.path.join(base, 'lifecycle', phase)
        os.makedirs(os.path.join(phase_dir, 'evidence'), exist_ok=True)
        for fname, content in [
            ('README.md', f'# {phase[:4]} — {variant}\n\n**Status:** DRAFT\n'),
            ('KNOTS.csv', 'knot_id,title,lifecycle_phase,obligation_source,status,owner,created_date,description,clause_refs,knu_refs,compliance_status,notes\n'),
            ('KNU_PLAN.csv', 'knu_id,title,lifecycle_phase,knot_ref,knu_class,status,owner,created_date,description,evidence_refs,compliance_status,start_date,end_date,notes\n'),
        ]:
            fpath = os.path.join(phase_dir, fname)
            if not os.path.exists(fpath):
                with open(fpath, 'w') as f:
                    f.write(content)

    print(f'Variant {variant} scaffolded under {product_family}')


def scaffold_programme(product_family, craft_class, family, programme):
    """Scaffold a programme template under the craft-class/family path."""
    base = os.path.join(
        REPO_ROOT, '04_PRODUCTS', product_family,
        craft_class, family, 'programmes', programme,
    )
    for subdir in ['governance', 'interfaces', 'milestones', 'roadmap', 'work_packages']:
        d = os.path.join(base, subdir)
        os.makedirs(d, exist_ok=True)
        gitkeep = os.path.join(d, '.gitkeep')
        if not os.path.exists(gitkeep):
            with open(gitkeep, 'w') as f:
                pass

    prog_md = os.path.join(base, 'PROGRAMME.md')
    if not os.path.exists(prog_md):
        with open(prog_md, 'w') as f:
            f.write(f'# {programme} — Programme Definition ({family})\n\n')
            f.write(f'**Path:** `04_PRODUCTS/{product_family}/{craft_class}/{family}/programmes/{programme}/PROGRAMME.md`\n')
            f.write('**Authority:** ASIT\n**Status:** DRAFT\n')

    print(f'Programme {programme} scaffolded under {product_family}/{craft_class}/{family}')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: scaffold_product_variant.py <PRODUCT_FAMILY> <VARIANT> [<CRAFT_CLASS> <FAMILY> [<PROGRAMME>]]')
        sys.exit(1)

    scaffold_variant(sys.argv[1], sys.argv[2])

    if len(sys.argv) >= 5:
        craft_class = sys.argv[3]
        family = sys.argv[4]
        programme = sys.argv[5] if len(sys.argv) > 5 else 'PROGRAMME'

        if craft_class not in VALID_CRAFT_CLASSES:
            print(f'ERROR: Invalid craft class "{craft_class}". Must be one of: {", ".join(sorted(VALID_CRAFT_CLASSES))}')
            sys.exit(1)

        expected_family = CRAFT_FAMILY_MAP.get(craft_class)
        if expected_family and family != expected_family:
            print(f'WARNING: Craft class {craft_class} is normally paired with family {expected_family}, got {family}')

        scaffold_programme(sys.argv[1], craft_class, family, programme)
