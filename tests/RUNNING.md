# M-Core test runner

The CI has two independent gates.

## Python audit

```bash
python -m pip install pytest pyyaml
python -m pytest tests/python -vv
```

A pass means executable audit witnesses/regressions passed. It does not promote an OPEN mathematical obligation to PROVED.

## Lean formal gate

```bash
lake update
lake build
```

The CI additionally rejects `sorry` and `admit` in `MCore/**/*.lean` and `MCore.lean`.

## Combined

```bash
make all
```

Status policy:
- Python green: `HARNESS PASS`.
- Lean green with no placeholders: the exact compiled Lean statements may be marked `PROVED`.
- Calibration (`Phi`, `epsilon0`, numerical samples) remains `NUMERICAL_EVIDENCE` unless a separate theorem derives it.
- Obligation 20 is intentionally outside the current 15–19 closure gate.
