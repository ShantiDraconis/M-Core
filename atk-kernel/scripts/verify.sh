#!/usr/bin/env bash
# Reproduz localmente o portão do CI (.github/workflows/atk-kernel.yml), na mesma ordem:
#   1. Mathlib já compilada (cache oficial);
#   2. lake build de todo o atk-kernel;
#   3. auditoria por arquivo: cada ATK/*.lean recompilado sozinho, com a saída de `#print axioms`;
#   4. scripts/check_axioms.py: só certifica um teorema esperado que compila, depende apenas de
#      propext / Classical.choice / Quot.sound e vem de fonte sem sorry / admit / axiom; o ensaio do
#      portão confere que sorry, axioma próprio, enunciado trocado por True, sombra do enunciado,
#      hipótese no teorema terminal, arquivo ausente e erro de compilação deixam a linha vermelha.
# Sai com 0 só se todos os teoremas esperados forem certificados. Não altera nenhuma flag:
# CLOSED_MATH só pode ser computado pelo portão (ATK/ClosedMathGate.lean).
set -uo pipefail
cd "$(dirname "$0")/.."
mkdir -p reports

lake exe cache get || { lake update && lake exe cache get; } || exit 1

lake build 2>&1 | tee reports/build.log
echo "lake build saiu com ${PIPESTATUS[0]}"

: > reports/file_status.txt
for f in ATK/*.lean ATK/Conditional/*.lean ATK/Terminal/*.lean; do
  [ -e "$f" ] || continue
  m=${f#ATK/}; m=${m%.lean}; m=${m//\//_}
  if lake env lean "$f" > "reports/audit_${m}.log" 2>&1; then
    echo "$f OK" >> reports/file_status.txt
  else
    echo "$f FAIL" >> reports/file_status.txt
    { grep -E "error" "reports/audit_${m}.log" || true; } | head -2 | sed "s|^|$f: |"
  fi
done
grep -c " OK$" reports/file_status.txt | sed 's/$/ arquivos OK/'
grep " FAIL$" reports/file_status.txt || true
cp lake-manifest.json reports/ || true

python3 scripts/check_axioms.py > reports/check_axioms.out
code=$?
grep -m1 -E "CERTIFIED|PARTIAL|NOT_CERTIFIED" reports/report.md || true
exit $code
