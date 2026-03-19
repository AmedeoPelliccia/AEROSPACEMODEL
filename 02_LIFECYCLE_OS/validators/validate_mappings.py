#!/usr/bin/env python3
"""
validate_mappings.py — AEROSPACEMODEL mapping validator
Path: 02_LIFECYCLE_OS/validators/validate_mappings.py
Authority: ASIT
"""

import csv
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

REQUIRED_CLAUSE_FIELDS = ['mapping_id', 'standard', 'clause_id', 'clause_title', 'lifecycle_phase', 'compliance_status']


def validate_clause_to_knu_csv(filepath, errors):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            for field in REQUIRED_CLAUSE_FIELDS:
                if field not in row or not row[field].strip():
                    errors.append(f'{filepath}:{i} Missing required field: {field}')


def main():
    errors = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f == 'clause_to_knu_matrix.csv':
                validate_clause_to_knu_csv(os.path.join(root, f), errors)

    if errors:
        print('MAPPING VALIDATION FAILED:')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)
    else:
        print('MAPPING VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
