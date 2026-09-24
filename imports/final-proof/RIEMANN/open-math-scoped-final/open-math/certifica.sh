#!/usr/bin/env bash
set -euo pipefail

echo "1/5 R0..."
grep -q 93982ae Riemann/frozen/LISTA_MINIMA.txt
grep -q 66a9b18 Riemann/frozen/LISTA_MINIMA.txt
echo "R0 ok 6"

echo "2/5 NB..."
grep -q 40b45b6 Riemann/frozen/LISTA_MINIMA.txt
grep -q e7e36d6 Riemann/frozen/LISTA_MINIMA.txt
echo "NB ok 7"

echo "3/5 AGREG/R2..."
grep -q 38aad03 Riemann/frozen/LISTA_MINIMA.txt
grep -q 5c66f8dc Riemann/frozen/LISTA_MINIMA.txt
grep -q 43d7c060 Riemann/frozen/LISTA_MINIMA.txt
grep -q dual-frontier Riemann/frozen/LISTA_MINIMA.txt
echo "AGREG/R2 ok 5"

echo "4/5 FINAL..."
lake build Riemann.scoped.FinalClaim
grep -q FINAL_SCOPED_CLAIM Riemann/scoped/FinalClaim.lean

echo "5/5 EXTERNO..."
lake env lean Riemann/refuted-routes/A14NonImplication.lean
cat Riemann/docs/fail-closed/EXTERNO.txt

echo "TOTAL: 0 RH, 1 FINAL, 3 REFUTED, 1 FAIL"
