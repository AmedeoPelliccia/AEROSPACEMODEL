#!/usr/bin/env python3
"""
validate_audit_records.py — AEROSPACEMODEL audit record validator
Path: 02_LIFECYCLE_OS/validators/validate_audit_records.py
Authority: ASIT
"""

import os
import sys

try:
    import yaml
except ImportError:
    print('WARNING: PyYAML not available; audit record validation skipped')
    sys.exit(0)

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

REQUIRED_FIELDS = ['audit_id', 'audit_type', 'scope', 'lead_auditor', 'date', 'status']


def validate_audit_yaml(filepath, errors):
    with open(filepath, encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f'{filepath}: YAML parse error: {e}')
            return
    if not isinstance(data, dict):
        return
    if 'audit_id' in data:
        for field in REQUIRED_FIELDS:
            if field not in data or not data[field]:
                errors.append(f'{filepath}: Missing required field: {field}')


def main():
    errors = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f.endswith('.yaml') and 'audit' in f.lower():
                validate_audit_yaml(os.path.join(root, f), errors)

    if errors:
        print('AUDIT RECORD VALIDATION FAILED:')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)
    else:
        print('AUDIT RECORD VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
