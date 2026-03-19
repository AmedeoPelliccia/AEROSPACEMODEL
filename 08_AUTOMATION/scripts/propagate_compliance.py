#!/usr/bin/env python3
"""
propagate_compliance.py — Propagate compliance status through the traceability chain
Path: 08_AUTOMATION/scripts/propagate_compliance.py
"""

import csv
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def get_knot_compliance(knot_id, knu_plan_files):
    knu_statuses = []
    for kfile in knu_plan_files:
        with open(kfile, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('knot_ref', '').strip() == knot_id:
                    knu_statuses.append(row.get('compliance_status', 'NOT_STARTED').strip())

    if not knu_statuses:
        return 'NOT_STARTED'
    if 'NON_COMPLIANT' in knu_statuses:
        return 'NON_COMPLIANT'
    if 'IN_PROGRESS' in knu_statuses or 'NOT_STARTED' in knu_statuses:
        return 'IN_PROGRESS'
    if all(s in ('COMPLIANT', 'EXEMPT') for s in knu_statuses):
        return 'COMPLIANT'
    return 'PARTIAL'


def main():
    knu_plan_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f == 'KNU_PLAN.csv':
                knu_plan_files.append(os.path.join(root, f))

    for root, dirs, files in os.walk(REPO_ROOT):
        for f in files:
            if f == 'KNOTS.csv':
                filepath = os.path.join(root, f)
                rows = []
                with open(filepath, newline='', encoding='utf-8') as cf:
                    reader = csv.DictReader(cf)
                    fieldnames = reader.fieldnames
                    for row in reader:
                        knot_id = row.get('knot_id', '').strip()
                        if knot_id:
                            row['compliance_status'] = get_knot_compliance(knot_id, knu_plan_files)
                        rows.append(row)

                with open(filepath, 'w', newline='', encoding='utf-8') as cf:
                    writer = csv.DictWriter(cf, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

    print('Compliance propagation complete')


if __name__ == '__main__':
    main()
