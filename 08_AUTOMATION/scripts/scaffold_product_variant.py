#!/usr/bin/env python3
"""
scaffold_product_variant.py — Scaffold a new product variant
Path: 08_AUTOMATION/scripts/scaffold_product_variant.py
Usage: python3 scaffold_product_variant.py <PRODUCT_FAMILY> <VARIANT>
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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: scaffold_product_variant.py <PRODUCT_FAMILY> <VARIANT>')
        sys.exit(1)
    scaffold_variant(sys.argv[1], sys.argv[2])
