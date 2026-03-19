#!/usr/bin/env python3
"""
validate_knots.py — AEROSPACEMODEL KNOT validator
Path: 02_LIFECYCLE_OS/validators/validate_knots.py
Authority: ASIT
"""

import csv
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KNOT_ID_PATTERN = re.compile(r'^KNOT-[A-Z0-9]+-LC\d{2}-\d{4}$')

REQUIRED_FIELDS = ['knot_id', 'title', 'lifecycle_phase', 'obligation_source', 'status', 'owner', 'created_date']


def validate_knots_csv(filepath, errors):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            for field in REQUIRED_FIELDS:
                if field not in row or not row[field].strip():
                    errors.append(f'{filepath}:{i} Missing required field: {field}')
            knot_id = row.get('knot_id', '').strip()
            if knot_id and not KNOT_ID_PATTERN.match(knot_id):
                errors.append(f'{filepath}:{i} Invalid KNOT ID format: {knot_id}')


def main():
    errors = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f == 'KNOTS.csv':
                validate_knots_csv(os.path.join(root, f), errors)

    if errors:
        print('KNOT VALIDATION FAILED:')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)
    else:
        print('KNOT VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
