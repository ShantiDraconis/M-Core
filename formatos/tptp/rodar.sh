#!/bin/bash
# Roda o E prover em cada problema TPTP (sintaxe TPTP-3); espera "SZS status Theorem".
# O E 3.0.03 do Ubuntu (build DEBUG) aborta no init do SAT com --auto; tentamos variantes sem ele.
cd "$(dirname "$0")"; ok=0
eprover --version 2>&1 | head -1
for f in *.p; do
  r=""
  for opts in "--tptp3-format" "--tptp3-format -xAuto -tAuto" "--auto --tptp3-format"; do
    out=$(eprover $opts --cpu-limit=60 "$f" 2>&1)
    r=$(echo "$out" | grep "SZS status" | head -1)
    [ -n "$r" ] && { r="$r   [eprover $opts]"; break; }
  done
  echo "$f: ${r:-sem status}"
  if ! echo "$r" | grep -q "Theorem"; then ok=1; echo "$out" | tail -5; fi
done
exit $ok
