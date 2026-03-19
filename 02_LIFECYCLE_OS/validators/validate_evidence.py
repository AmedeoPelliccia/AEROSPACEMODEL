#!/usr/bin/env python3
"""
validate_evidence.py — AEROSPACEMODEL evidence validator
Path: 02_LIFECYCLE_OS/validators/validate_evidence.py
Authority: ASIT
"""

import csv
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
EVIDENCE_REGISTER = os.path.join(REPO_ROOT, '03_SHARED_SERVICES', 'evidence', 'evidence_register.csv')

REQUIRED_FIELDS = ['oid', 'title', 'evidence_type', 'lifecycle_phase', 'knot_ref', 'knu_ref', 'status', 'created_date', 'author']


def validate_evidence_register(filepath, errors):
    if not os.path.isfile(filepath):
        errors.append(f'Evidence register not found: {filepath}')
        return
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            for field in REQUIRED_FIELDS:
                if field not in row or not row[field].strip():
                    errors.append(f'{filepath}:{i} Missing required field: {field}')


def main():
    errors = []
    validate_evidence_register(EVIDENCE_REGISTER, errors)

    if errors:
        print('EVIDENCE VALIDATION FAILED:')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)
    else:
        print('EVIDENCE VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
