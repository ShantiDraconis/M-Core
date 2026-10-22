#!/bin/bash
# Roda o E prover em cada problema TPTP; espera "SZS status Theorem".
cd "$(dirname "$0")"; ok=0
for f in *.p; do
  r=$(eprover --auto --cpu-limit=60 -s "$f" 2>/dev/null | grep "SZS status" | head -1)
  echo "$f: $r"
  echo "$r" | grep -q "Theorem" || ok=1
done
exit $ok
