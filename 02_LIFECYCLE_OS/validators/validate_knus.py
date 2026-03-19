#!/usr/bin/env python3
"""
validate_knus.py — AEROSPACEMODEL KNU validator
Path: 02_LIFECYCLE_OS/validators/validate_knus.py
Authority: ASIT
"""

import csv
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KNU_ID_PATTERN = re.compile(r'^KNU-[A-Z0-9]+-LC\d{2}-\d{4}$')

REQUIRED_FIELDS = ['knu_id', 'title', 'lifecycle_phase', 'knot_ref', 'knu_class', 'status', 'owner', 'created_date']


def validate_knu_plan_csv(filepath, errors):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            for field in REQUIRED_FIELDS:
                if field not in row or not row[field].strip():
                    errors.append(f'{filepath}:{i} Missing required field: {field}')
            knu_id = row.get('knu_id', '').strip()
            if knu_id and not KNU_ID_PATTERN.match(knu_id):
                errors.append(f'{filepath}:{i} Invalid KNU ID format: {knu_id}')


def main():
    errors = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f == 'KNU_PLAN.csv':
                validate_knu_plan_csv(os.path.join(root, f), errors)

    if errors:
        print('KNU VALIDATION FAILED:')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)
    else:
        print('KNU VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
