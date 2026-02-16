# Constitutional Pre-Commit Hooks

This directory contains enforcement hooks for the Model Digital Constitution.

## Purpose

These hooks transform the Digital Constitution from aspirational text into **executable constraint**. They enforce constitutional principles at the atomic unit of change—the commit—making violations visible, traceable, and blockable at the point of creation.

## Hooks

### 1. `constitutional_commit_validator.py`

**Constitutional Articles:** 4 (Commit as Unit of Legitimacy), 7 (Explicit Purpose)

**Purpose:** Validates that every commit message contains required sections declaring:
- **INTENT**: What the commit aims to improve
- **RATIONALE**: Why this change is necessary
- **HUMAN_IMPACT**: Effect on people (workers, users, operators)
- **REVERSIBILITY**: How to degrade/pause/escalate if harm occurs
- **AUTHOR**: Accountable human agent

**Enforcement:**
- Blocks commits missing required sections
- Detects Article 8 violations (workforce reduction without reabsorption)
- Validates Article 6 requirements (harm-mitigation paths)

**Sample Compliant Commit Message:**
```
INTENT: Add pre-commit hooks for constitutional enforcement
RATIONALE: Operationalize Model Digital Constitution by enforcing structure at commit time. Currently no automated validation of constitutional principles exists.
HUMAN_IMPACT: Positive - increases developer accountability and visibility of decisions. Requires 2-3 minutes additional time per commit for documentation. No workforce reduction.
REVERSIBILITY: Hooks can be bypassed with --no-verify flag in emergency. Can be disabled by removing .pre-commit-config.yaml. If harm detected, escalate to repository steward for review.
AUTHOR: Constitutional Governance Team
```

**Testing:**
```bash
# Test with valid message
echo "INTENT: Test
RATIONALE: Testing validator
HUMAN_IMPACT: No impact on workforce
REVERSIBILITY: Can be reverted via git revert, escalate to steward if issues
AUTHOR: Test User" > /tmp/test_msg.txt
python3 constitutional_commit_validator.py /tmp/test_msg.txt

# Test with invalid message (missing sections)
echo "Just a regular commit message" > /tmp/test_msg_invalid.txt
python3 constitutional_commit_validator.py /tmp/test_msg_invalid.txt
# Should fail with clear error message
```

### 2. Labor Reabsorption Pattern Scanner

**Constitutional Articles:** 1 (Human Labor Foundation), 8 (No Exclusion by Efficiency)

**Purpose:** Scans for patterns indicating labor displacement:
- "remove role"
- "eliminate position"
- "workforce reduction"
- "job elimination"
- "autonomous override"

**Enforcement:**
- Flags commits containing these patterns
- Requires documentation in `LABOR_REABSORPTION_PLAN.md` or justification in commit `HUMAN_IMPACT`
- Does not block commits (warning only) but triggers human review requirement

**Pattern Detection Examples:**
```bash
# Will trigger warning
echo "This change will remove operator role to improve efficiency" > changes.md
git add changes.md
git commit -m "..."
# Output: ⚠️ LABOR PATTERN DETECTED - reabsorption documentation required

# Compliant (with reabsorption)
echo "Workforce reduction: 2 operators. Reabsorption: transition to supervisory roles with 6-month training program" > HUMAN_IMPACT
```

### 3. Constitutional Pylint Plugin

**Constitutional Articles:** 3 (Technology as Servant), 6 (Human Harm Precedence)

**Purpose:** Detects safety-critical code paths lacking constitutional safeguards.

**Checks:**
- Safety-critical functions missing harm-mitigation logic (`escalate_to_human`, `degrade_mode`, `pause_operation`)
- Autonomous overrides without accountability mechanisms (logging, audit trails)
- Critical decisions without traceability

**Example - Non-Compliant:**
```python
def safety_critical_flight_control(altitude, speed):
    """Safety-critical flight control logic."""
    if altitude < 1000:
        # Direct action without human confirmation
        return "emergency_descent"
    return "nominal"
```

**Example - Compliant:**
```python
def safety_critical_flight_control(altitude, speed):
    """Safety-critical flight control logic."""
    if altitude < 1000:
        # Article 6: Escalate to human authority
        escalate_to_human("Low altitude detected", {"altitude": altitude})
        # Article 6: Degrade to safe mode
        return degrade_mode("safe_altitude_hold")
    return "nominal"
```

**Testing:**
```bash
# Check a Python file
PYTHONPATH=.github/plugins:$PYTHONPATH pylint \
  --load-plugins=constitutional_pylint_plugin \
  --disable=all \
  --enable=constitution-violation-harm-precedence,constitution-violation-autonomous-override \
  your_file.py
```

## Installation

### Prerequisites
```bash
pip install pre-commit
# For Pylint plugin (optional but recommended)
pip install pylint astroid
```

### Setup
```bash
# Install git hooks
pre-commit install

# Install commit-msg hook specifically
pre-commit install --hook-type commit-msg

# Test installation
pre-commit run --all-files
```

## Usage

### Normal Workflow

Hooks run automatically on `git commit`. Example:

```bash
git add file.py
git commit
# Your editor opens for commit message
# Write message using constitutional template:

INTENT: Fix issue #123
RATIONALE: Bug causing incorrect calculation
HUMAN_IMPACT: No workforce impact. Improves operator safety by correcting false alerts.
REVERSIBILITY: Can be reverted via git revert. If issues detected, escalate to STK_SAF for review.
AUTHOR: Jane Developer

# Save and exit
# Hooks run automatically and validate message
```

### Bypass (Emergency Only)

In emergencies, hooks can be bypassed:

```bash
git commit --no-verify
```

**Warning:** Bypassing hooks requires justification in the commit or a follow-up constitutional commit per Article 11.

### Manual Validation

Run hooks manually without committing:

```bash
# Test all hooks
pre-commit run --all-files

# Test specific hook
pre-commit run constitutional-commit-msg --all-files

# Test commit message validator directly
python3 .github/hooks/constitutional_commit_validator.py <commit-msg-file>
```

## Edge Cases and `.constitution-ignore`

For legitimate edge cases (e.g., automated bot commits, merge commits), create `.constitution-ignore`:

```yaml
# .constitution-ignore
# Constitutional hook exceptions with required justification

exceptions:
  - pattern: "^Merge pull request"
    reason: "GitHub merge commits lack human-authored content"
    justification: "Merge commits reference PRs which contain constitutional documentation"
    approved_by: "Repository Steward"
    
  - pattern: "^dependabot"
    reason: "Automated dependency updates"
    justification: "Dependency updates reviewed in PR process, minimal human impact"
    approved_by: "Security Team"
```

**Important:** All exceptions trigger audit log entries.

## Limitations and Human Review

### What Hooks Enforce
✅ **Structure**: Required sections exist  
✅ **Patterns**: Known violation patterns detected  
✅ **Code patterns**: Safety-critical paths identified  

### What Hooks Cannot Enforce
❌ **Truth**: Hooks can't verify honesty of `HUMAN_IMPACT` statements  
❌ **Quality**: Can't assess if reabsorption plans are credible  
❌ **Intent**: Can't detect deliberate circumvention  

### Mitigation Strategy

**Constitution Steward Role** (documented in `GOVERNANCE.md`):
- Reviews all commits flagged by hooks
- Assesses substantive compliance
- Authority to reject non-compliant changes
- Escalation path for conflicts

**Audit Trail:**
- All hook violations logged
- Exception usage tracked
- Steward reviews documented

## Constitutional Enforcement Flow

```
┌─────────────────┐
│  Developer      │
│  git commit     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  Pre-Commit Hook 1:         │
│  Commit Message Validator   │
│  Articles 4, 7              │
└────────┬────────────────────┘
         │ ✅ Valid
         ▼
┌─────────────────────────────┐
│  Pre-Commit Hook 2:         │
│  Labor Pattern Scanner      │
│  Articles 1, 8              │
└────────┬────────────────────┘
         │ ⚠️  Warning (if patterns detected)
         ▼
┌─────────────────────────────┐
│  Pre-Commit Hook 3:         │
│  Constitutional Pylint      │
│  Articles 3, 6              │
└────────┬────────────────────┘
         │ ✅ Pass / ⚠️ Warning
         ▼
┌─────────────────────────────┐
│  Commit Created             │
│  Git History Updated        │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  [Optional]                 │
│  Human Steward Review       │
│  (for flagged commits)      │
└─────────────────────────────┘
```

## Maintenance

### Adding New Patterns

To add new labor-displacement patterns:

1. Edit `.pre-commit-config.yaml`, section `labor-reabsorption-check`
2. Add pattern to grep expression
3. Test with sample text
4. Document in this README

### Extending Pylint Checks

To add new constitutional code checks:

1. Edit `.github/plugins/constitutional_pylint_plugin.py`
2. Add new message code (C900X)
3. Implement detection logic in `ConstitutionalChecker`
4. Test with sample Python code
5. Document in this README

### Version Updates

When updating pre-commit hook versions:

```bash
pre-commit autoupdate
git add .pre-commit-config.yaml
git commit  # (with constitutional message format)
```

## Troubleshooting

### Hook Not Running

```bash
# Verify installation
pre-commit --version

# Reinstall hooks
pre-commit uninstall
pre-commit install
pre-commit install --hook-type commit-msg

# Check hook configuration
pre-commit run --all-files --verbose
```

### Validator Script Permission Denied

```bash
chmod +x .github/hooks/constitutional_commit_validator.py
```

### Pylint Plugin Not Found

```bash
# Verify PYTHONPATH includes plugin directory
export PYTHONPATH=.github/plugins:$PYTHONPATH
pylint --load-plugins=constitutional_pylint_plugin --help
```

### False Positives

If a hook incorrectly flags valid code:

1. Review the pattern causing false positive
2. Document in `.constitution-ignore` with justification
3. File issue for hook refinement
4. Constitution Steward must approve exception

## References

- [Model Digital Constitution](../../Model_Digital_Constitution.md)
- [GOVERNANCE.md](../../GOVERNANCE.md)
- [Pre-commit Framework](https://pre-commit.com/)
- [Pylint](https://pylint.pycqa.org/)

---

*"Legitimacy accumulates through committed responsibility, not outputs alone."*  
— Model Digital Constitution, Article 4
