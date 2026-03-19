#!/usr/bin/env python3
"""
dag_scheduler.py — AEROSPACEMODEL DAG-based lifecycle scheduler
Path: 02_LIFECYCLE_OS/schedulers/dag_scheduler.py
Authority: ASIT
"""

import yaml
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DEPENDENCY_RULES = os.path.join(os.path.dirname(__file__), 'dependency_rules.yaml')


def load_rules():
    with open(DEPENDENCY_RULES, encoding='utf-8') as f:
        return yaml.safe_load(f)


def topological_sort(phases, dependencies):
    visited = set()
    order = []

    def visit(phase_id):
        if phase_id in visited:
            return
        visited.add(phase_id)
        for dep in dependencies.get(phase_id, []):
            visit(dep)
        order.append(phase_id)

    for phase in phases:
        visit(phase)
    return order


def main():
    rules = load_rules()
    phases = [p['id'] for p in rules.get('phases', [])]
    dependencies = {p['id']: p.get('depends_on', []) for p in rules.get('phases', [])}
    order = topological_sort(phases, dependencies)
    print('Execution order:')
    for i, phase in enumerate(order, start=1):
        print(f'  {i}. {phase}')


if __name__ == '__main__':
    main()
