#!/bin/bash
# Roda o E prover em cada problema TPTP (sintaxe TPTP-3); espera "SZS status Theorem".
cd "$(dirname "$0")"; ok=0
eprover --version 2>&1 | head -1
for f in *.p; do
  out=$(eprover --auto --tptp3-format --cpu-limit=60 "$f" 2>&1)
  r=$(echo "$out" | grep "SZS status" | head -1)
  echo "$f: ${r:-sem status}"
  if ! echo "$r" | grep -q "Theorem"; then ok=1; echo "$out" | tail -5; fi
done
exit $ok
