diff --git a/Kiss-scaffold/src/config_loader.py b/Kiss-scaffold/src/config_loader.py
index abc1234..a9f4d21 100644
--- a/Kiss-scaffold/src/config_loader.py
+++ b/Kiss-scaffold/src/config_loader.py
@@ -1,11 +1,28 @@
 from __future__ import annotations
 
 from pathlib import Path
-from typing import Any, Dict, List, Tuple
+from typing import Any, Dict, Tuple
 import yaml
 
+CANONICAL_ORDER = [
+    "LC01_PROBLEM_STATEMENT",
+    "LC02_SYSTEM_REQUIREMENTS",
+    "LC03_SAFETY_RELIABILITY",
+    "LC04_DESIGN_DEFINITION",
+    "LC05_ANALYSIS_MODELS",
+    "LC06_VERIFICATION",
+    "LC07_QA_PROCESS",
+    "LC08_CONFIGURATION",
+    "LC09_ESG_SUSTAINABILITY",
+    "LC10_INDUSTRIAL_SUPPLY",
+    "LC11_OPERATIONS_CUSTOMIZATION",
+    "LC12_MAINTENANCE_REPAIR",
+    "LC13_MAINTENANCE_SOURCE",
+    "LC14_END_OF_LIFE",
+]
+
 class ConfigError(Exception):
     pass
 
+
 def _read_yaml(path: Path) -> Dict[str, Any]:
     if not path.exists():
         raise ConfigError(f"Config file not found: {path}")
@@ -13,29 +30,40 @@ def _read_yaml(path: Path) -> Dict[str, Any]:
     if not isinstance(data, dict):
         raise ConfigError(f"Invalid YAML object at root: {path}")
     return data
 
+
 def load_configs(config_dir: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
     lifecycle = _read_yaml(config_dir / "lifecycle.yaml")
     atdp = _read_yaml(config_dir / "atdp.yaml")
 
     phases = lifecycle.get("phases")
-    if not isinstance(phases, dict) or len(phases) != 14:
-        raise ConfigError("lifecycle.yaml must define exactly 14 LC phases in 'phases'.")
+    if not isinstance(phases, dict):
+        raise ConfigError("lifecycle.yaml 'phases' must be an object.")
+
+    got = set(phases.keys())
+    exp = set(CANONICAL_ORDER)
+    if got != exp:
+        missing = sorted(exp - got)
+        extra = sorted(got - exp)
+        raise ConfigError(f"Lifecycle keys mismatch. Missing={missing} Extra={extra}")
 
     required_phase_keys = {"phase_type", "canonical_name", "ssot_dir"}
     for lc_id, spec in phases.items():
         if not isinstance(spec, dict):
             raise ConfigError(f"{lc_id} spec must be an object.")
         missing = required_phase_keys - set(spec.keys())
         if missing:
             raise ConfigError(f"{lc_id} missing keys: {sorted(missing)}")
+        if spec["phase_type"] not in {"PLM", "OPS"}:
+            raise ConfigError(f"{lc_id} phase_type must be PLM or OPS.")
 
     products = atdp.get("products")
     common_dirs = atdp.get("common_csdb_dirs")
     if not isinstance(products, list) or not all(isinstance(x, str) for x in products):
         raise ConfigError("atdp.yaml 'products' must be a list[str].")
     if not isinstance(common_dirs, list) or not all(isinstance(x, str) for x in common_dirs):
         raise ConfigError("atdp.yaml 'common_csdb_dirs' must be a list[str].")
 
+    lifecycle["_ordered_lc_ids"] = CANONICAL_ORDER[:]
     return lifecycle, atdp
diff --git a/Kiss-scaffold/src/generator.py b/Kiss-scaffold/src/generator.py
index abc1234..83fbf2a 100644
--- a/Kiss-scaffold/src/generator.py
+++ b/Kiss-scaffold/src/generator.py
@@ -1,6 +1,8 @@
 from __future__ import annotations
 
+import os
+import tempfile
 from dataclasses import dataclass
 from pathlib import Path
 from typing import Dict, Any, List
 import textwrap
@@ -19,18 +21,33 @@ class GenerationError(Exception):
 def _norm(content: str) -> str:
     return textwrap.dedent(content).lstrip("\n")
 
+def _atomic_write_text(path: Path, content: str) -> None:
+    path.parent.mkdir(parents=True, exist_ok=True)
+    fd, tmp_name = tempfile.mkstemp(dir=str(path.parent))
+    try:
+        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
+            f.write(content)
+        os.replace(tmp_name, path)
+    finally:
+        if os.path.exists(tmp_name):
+            os.unlink(tmp_name)
+
 def _write(ctx: GenContext, rel_path: str, content: str) -> None:
     p = ctx.base / rel_path
-    p.parent.mkdir(parents=True, exist_ok=True)
-
     if p.exists():
         if ctx.mode == "fail":
             raise GenerationError(f"Collision in mode=fail: {p}")
         if ctx.mode == "safe":
             return
 
-    p.write_text(_norm(content), encoding="utf-8", newline="\n")
+    _atomic_write_text(p, _norm(content))
     ctx.written.append(p)
 
+
 def gen_root(ctx: GenContext) -> None:
     _write(ctx, "00-00-general/README.md", f"""\
     # ATA 00-00 — KISS
@@ -71,7 +88,12 @@ def gen_ssot(ctx: GenContext, phases: Dict[str, Any]) -> None:
         f"# Execution\nExecution: {ctx.now_iso}\nStatus: DRAFT\n",
     )
 
-    for lc_id in sorted(phases.keys()):
+    ordered_ids = phases.get("_ordered_lc_ids")
+    if not isinstance(ordered_ids, list):
+        ordered_ids = sorted([k for k in phases.keys() if k.startswith("LC")])
+
+    for lc_id in ordered_ids:
+        if lc_id not in phases:
+            continue
         spec = phases[lc_id]
         _write(
             ctx,
diff --git a/Kiss-scaffold/src/validator.py b/Kiss-scaffold/src/validator.py
index abc1234..5a0dd61 100644
--- a/Kiss-scaffold/src/validator.py
+++ b/Kiss-scaffold/src/validator.py
@@ -15,6 +15,7 @@ class ValidationError(Exception):
 
 def validate_locked_rules_and_lifecycle(base: Path, phases: Dict[str, Any], atdp_cfg: Dict[str, Any]) -> Tuple[bool, List[str]]:
     errs: List[str] = []
+    phase_keys = {k for k in phases.keys() if k.startswith("LC")}
 
     genesis = base / "00-00-general" / "GENESIS"
     ssot = base / "00-00-general" / "SSOT"
@@ -23,6 +24,10 @@ def validate_locked_rules_and_lifecycle(base: Path, phases: Dict[str, Any], atdp
     for root in [genesis, ssot, pub]:
         if not root.exists():
             errs.append(f"Missing required root: {root}")
+
+    if errs:
+        return (False, errs)
+
     # Rule 1: no _executions in GENESIS
     if genesis.exists():
         for p in genesis.rglob("*"):
@@ -35,7 +40,7 @@ def validate_locked_rules_and_lifecycle(base: Path, phases: Dict[str, Any], atdp
                 errs.append(f"Locked Rule 2 violation: {p}")
 
     # Canonical LC set exact match
-    expected_lc = set(phases.keys())
+    expected_lc = phase_keys
     existing_lc = {d.name for d in ssot.iterdir() if d.is_dir() and d.name.startswith("LC")} if ssot.exists() else set()
     missing = expected_lc - existing_lc
     extra = existing_lc - expected_lc
diff --git a/Kiss-scaffold/tests/test_integration.py b/Kiss-scaffold/tests/test_integration.py
new file mode 100644
index 0000000..9e347f4
--- /dev/null
+++ b/Kiss-scaffold/tests/test_integration.py
@@ -0,0 +1,39 @@
+from pathlib import Path
+from src.generator import GenContext, gen_root, gen_genesis, gen_ssot, gen_csdb_pub, gen_0090
+from src.validator import validate_locked_rules_and_lifecycle
+
+def test_roundtrip_generation_and_validation(tmp_path: Path):
+    phases = {
+        "_ordered_lc_ids": [
+            "LC01_PROBLEM_STATEMENT","LC02_SYSTEM_REQUIREMENTS","LC03_SAFETY_RELIABILITY","LC04_DESIGN_DEFINITION",
+            "LC05_ANALYSIS_MODELS","LC06_VERIFICATION","LC07_QA_PROCESS","LC08_CONFIGURATION",
+            "LC09_ESG_SUSTAINABILITY","LC10_INDUSTRIAL_SUPPLY","LC11_OPERATIONS_CUSTOMIZATION",
+            "LC12_MAINTENANCE_REPAIR","LC13_MAINTENANCE_SOURCE","LC14_END_OF_LIFE"
+        ],
+        "LC01_PROBLEM_STATEMENT": {"phase_type": "PLM", "canonical_name": "Problem Statement", "ssot_dir": "x/LC01"},
+        "LC02_SYSTEM_REQUIREMENTS": {"phase_type": "PLM", "canonical_name": "System Requirements", "ssot_dir": "x/LC02"},
+        "LC03_SAFETY_RELIABILITY": {"phase_type": "PLM", "canonical_name": "Safety & Reliability", "ssot_dir": "x/LC03"},
+        "LC04_DESIGN_DEFINITION": {"phase_type": "PLM", "canonical_name": "Design Definition", "ssot_dir": "x/LC04"},
+        "LC05_ANALYSIS_MODELS": {"phase_type": "PLM", "canonical_name": "Analysis Models", "ssot_dir": "x/LC05"},
+        "LC06_VERIFICATION": {"phase_type": "PLM", "canonical_name": "Integration & Test", "ssot_dir": "x/LC06"},
+        "LC07_QA_PROCESS": {"phase_type": "PLM", "canonical_name": "QA & Process Compliance", "ssot_dir": "x/LC07"},
+        "LC08_CONFIGURATION": {"phase_type": "PLM", "canonical_name": "Certification", "ssot_dir": "x/LC08"},
+        "LC09_ESG_SUSTAINABILITY": {"phase_type": "PLM", "canonical_name": "ESG & Sustainability", "ssot_dir": "x/LC09"},
+        "LC10_INDUSTRIAL_SUPPLY": {"phase_type": "PLM", "canonical_name": "Industrial & Supply Chain", "ssot_dir": "x/LC10"},
+        "LC11_OPERATIONS_CUSTOMIZATION": {"phase_type": "OPS", "canonical_name": "Operations Customization", "ssot_dir": "x/LC11"},
+        "LC12_MAINTENANCE_REPAIR": {"phase_type": "OPS", "canonical_name": "Continued Airworthiness & MRO", "ssot_dir": "x/LC12"},
+        "LC13_MAINTENANCE_SOURCE": {"phase_type": "OPS", "canonical_name": "Maintenance Source Data", "ssot_dir": "x/LC13"},
+        "LC14_END_OF_LIFE": {"phase_type": "OPS", "canonical_name": "End of Life", "ssot_dir": "x/LC14"},
+    }
+    atdp = {"products": ["AMM", "IPC"], "common_csdb_dirs": ["DM", "PM"]}
+
+    ctx = GenContext(base=tmp_path, mode="overwrite", now_iso="2026-02-16T10:00:00Z", date_short="2026-02-16", written=[])
+    gen_root(ctx)
+    gen_genesis(ctx)
+    gen_ssot(ctx, phases)
+    gen_csdb_pub(ctx, atdp)
+    gen_0090(ctx, phases, atdp)
+
+    ok, errs = validate_locked_rules_and_lifecycle(tmp_path, phases, atdp)
+    assert ok, errs
diff --git a/Kiss-scaffold/.github/workflows/ci.yml b/Kiss-scaffold/.github/workflows/ci.yml
new file mode 100644
index 0000000..6ea93ad
--- /dev/null
+++ b/Kiss-scaffold/.github/workflows/ci.yml
@@ -0,0 +1,15 @@
+name: ci
+on:
+  push:
+  pull_request:
+jobs:
+  test:
+    runs-on: ubuntu-latest
+    steps:
+      - uses: actions/checkout@v4
+      - uses: actions/setup-python@v5
+        with:
+          python-version: "3.11"
+      - run: pip install -r requirements.txt
+      - run: pytest -q
+      - run: python Kiss-scaffold.py --base ./OUT --config-dir ./config --validate --manifest

Apply with:

git apply corrected-hardening.patch

Then verify:

pytest -q
python Kiss-scaffold.py --base ./OUT --config-dir ./config --validate --manifest