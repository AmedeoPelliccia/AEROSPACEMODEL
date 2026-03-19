#!/usr/bin/env python3
"""
validate_structure.py — AEROSPACEMODEL structural validator
Path: 02_LIFECYCLE_OS/validators/validate_structure.py
Authority: ASIT
"""

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

MANDATORY_ROOT_FILES = [
    'README.md',
    'AEROSPACEMODEL.md',
    'MODEL_DIGITAL_CONSTITUTION.md',
    'CHANGELOG.md',
    'LICENSE',
    '.gitignore',
]

MANDATORY_DIRS = [
    '00_META',
    '01_GOVERNANCE',
    '02_LIFECYCLE_OS',
    '03_SHARED_SERVICES',
    '04_PRODUCTS',
    '05_STANDARDS_LIBRARY',
    '06_PRODUCT_DATA_MODEL',
    '07_TECHNICAL_PUBLICATIONS',
    '08_AUTOMATION',
    '09_AUDIT_AND_ASSURANCE',
    '10_REPORTING',
    '11_INTEGRATIONS',
]

MANDATORY_META_FILES = [
    '00_META/schemas/evidence_model.yaml',
    '00_META/schemas/lc_alias.yaml',
]

MANDATORY_LOS_FILES = [
    '02_LIFECYCLE_OS/registries/KNOT_REGISTRY.csv',
    '02_LIFECYCLE_OS/registries/KNU_CLASS_REGISTRY.csv',
]

MANDATORY_CI_FILES = [
    '08_AUTOMATION/ci/pipeline.yaml',
    '.github/workflows/validate_structure.yml',
]


def check_file(path, errors):
    full_path = os.path.join(REPO_ROOT, path)
    if not os.path.isfile(full_path):
        errors.append(f'MISSING FILE: {path}')


def check_dir(path, errors):
    full_path = os.path.join(REPO_ROOT, path)
    if not os.path.isdir(full_path):
        errors.append(f'MISSING DIR: {path}')


def main():
    errors = []

    for f in MANDATORY_ROOT_FILES:
        check_file(f, errors)

    for d in MANDATORY_DIRS:
        check_dir(d, errors)

    for f in MANDATORY_META_FILES:
        check_file(f, errors)

    for f in MANDATORY_LOS_FILES:
        check_file(f, errors)

    for f in MANDATORY_CI_FILES:
        check_file(f, errors)

    if errors:
        print('STRUCTURE VALIDATION FAILED:')
        for e in errors:
            print(f'  {e}')
        sys.exit(1)
    else:
        print('STRUCTURE VALIDATION PASSED')
        sys.exit(0)


if __name__ == '__main__':
    main()
