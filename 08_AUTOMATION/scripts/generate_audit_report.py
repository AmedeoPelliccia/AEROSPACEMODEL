#!/usr/bin/env python3
"""
generate_audit_report.py — Generate audit report from audit records
Path: 08_AUTOMATION/scripts/generate_audit_report.py
"""

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def main():
    print('Audit Report Generator')
    print('======================')
    audit_dirs = []
    for root, dirs, files in os.walk(REPO_ROOT):
        if 'audit' in os.path.basename(root).lower():
            for f in files:
                if f.endswith('.yaml') or f.endswith('.csv'):
                    audit_dirs.append(os.path.join(root, f))

    print(f'Found {len(audit_dirs)} audit record files')
    for f in audit_dirs:
        print(f'  {f}')


if __name__ == '__main__':
    main()
