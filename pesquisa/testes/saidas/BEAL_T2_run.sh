#!/bin/sh
cd /tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/work
for args in "box 5 8000" "box 7 5000" "slice 5 10000000" "slice 7 1000000"; do
  set -- $args
  t0=$(date +%s)
  nice -n 10 timeout 900 ./BEAL_T2_sfc $args > T2_$1_$2_$3.out 2>&1
  echo "rc=$? TEMPO $(( $(date +%s) - t0 )) s" >> T2_$1_$2_$3.out
done
echo FIM > T2_done
