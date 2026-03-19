#!/usr/bin/env python3
"""
scaffold_standard.py — Scaffold a new standard binding in 05_STANDARDS_LIBRARY
Path: 08_AUTOMATION/scripts/scaffold_standard.py
Usage: python3 scaffold_standard.py <STANDARD_ID>
"""

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def scaffold_standard(standard_id):
    base = os.path.join(REPO_ROOT, '05_STANDARDS_LIBRARY', standard_id)
    dirs = [
        base,
        os.path.join(base, 'source'),
        os.path.join(base, 'interpretations'),
        os.path.join(base, 'lifecycle_os', 'mappings'),
        os.path.join(base, 'lifecycle_os', 'evidence'),
        os.path.join(base, 'lifecycle_os', 'audit'),
        os.path.join(base, 'lifecycle_os', 'schemas'),
        os.path.join(base, 'lifecycle_os', 'validators'),
        os.path.join(base, 'lifecycle_os', 'reports'),
        os.path.join(base, 'registers'),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        gitkeep = os.path.join(d, '.gitkeep')
        if not os.listdir(d):
            open(gitkeep, 'w').close()

    # Create AEROSPACEMODEL.md
    amd_path = os.path.join(base, 'AEROSPACEMODEL.md')
    with open(amd_path, 'w') as f:
        f.write(f'# AEROSPACEMODEL — {standard_id}\n\n')
        f.write(f'**Standard:** {standard_id}  \n')
        f.write('**Authority:** ASIT  \n')
        f.write('**Status:** DRAFT\n')

    print(f'Standard {standard_id} scaffolded at {base}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: scaffold_standard.py <STANDARD_ID>')
        sys.exit(1)
    scaffold_standard(sys.argv[1])
