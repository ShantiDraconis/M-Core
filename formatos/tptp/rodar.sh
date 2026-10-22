#!/bin/bash
# Prova cada problema TPTP com o primeiro provador disponível que responder:
# Vampire (release do GitHub), SPASS (-TPTP) e E. Espera "SZS status Theorem" ou "Proof found".
# (O E 3.0.03 do Ubuntu é um build DEBUG que aborta no init do SAT.)
cd "$(dirname "$0")"; ok=0
VAMP=${VAMPIRE:-$(command -v vampire || true)}
for f in *.p; do
  r=""; quem=""
  if [ -n "$VAMP" ] && [ -x "$VAMP" ]; then
    out=$("$VAMP" --mode casc -t 60 "$f" 2>&1); r=$(echo "$out" | grep -m1 "SZS status"); quem="vampire"
  fi
  if ! echo "$r" | grep -q "Theorem" && command -v SPASS > /dev/null; then
    out=$(SPASS -TPTP -TimeLimit=60 "$f" 2>&1); r=$(echo "$out" | grep -m1 -E "Proof found|Completion found"); quem="SPASS"
  fi
  if ! echo "$r" | grep -q -E "Theorem|Proof found" && command -v eprover > /dev/null; then
    out=$(eprover --tptp3-format --cpu-limit=60 "$f" 2>&1); r=$(echo "$out" | grep -m1 "SZS status"); quem="eprover"
  fi
  echo "$f: ${r:-sem status} [$quem]"
  if ! echo "$r" | grep -q -E "Theorem|Proof found"; then ok=1; echo "$out" | tail -4; fi
done
exit $ok
