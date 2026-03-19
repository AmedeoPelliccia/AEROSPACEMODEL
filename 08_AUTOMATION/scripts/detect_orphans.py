#!/usr/bin/env python3
"""
detect_orphans.py — Detect orphan KNUs and KNOTs
Path: 08_AUTOMATION/scripts/detect_orphans.py
"""

import csv
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def main():
    knot_ids = set()
    knu_knot_refs = set()
    orphan_knus = []

    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f == 'KNOTS.csv':
                with open(os.path.join(root, f), newline='', encoding='utf-8') as cf:
                    for row in csv.DictReader(cf):
                        kid = row.get('knot_id', '').strip()
                        if kid:
                            knot_ids.add(kid)
            if f == 'KNU_PLAN.csv':
                filepath = os.path.join(root, f)
                with open(filepath, newline='', encoding='utf-8') as cf:
                    for row in csv.DictReader(cf):
                        knu_id = row.get('knu_id', '').strip()
                        knot_ref = row.get('knot_ref', '').strip()
                        if knu_id and not knot_ref:
                            orphan_knus.append((knu_id, filepath))
                        if knot_ref:
                            knu_knot_refs.add(knot_ref)

    if orphan_knus:
        print('ORPHAN KNUs DETECTED:')
        for knu_id, path in orphan_knus:
            print(f'  {knu_id} in {path}')
        sys.exit(1)
    else:
        print('No orphan KNUs detected')
        sys.exit(0)


if __name__ == '__main__':
    main()
