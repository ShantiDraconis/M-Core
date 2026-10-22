"""Controle de implementação: entradas G(i,j) do código C (dd) vs Vasyunin em mpmath e vs integração
direta (quando lcm(h,k) é pequeno). Uso: python3 RH_Gram_checkG.py dumpG.txt"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from math import gcd
import RH_Gram_verify as V   # reaproveita direct() e vas() (executa os testes do módulo ao importar)
mp.mp.dps = 40
for line in open(sys.argv[1]):
    if not line.startswith("G "): continue
    _, i, j, val = line.split(); i, j = int(i), int(j)
    c = mp.mpf(val)
    vv = V.vas(i, j)
    d = gcd(i, j); L = i * j // d // d
    dr = V.direct(i // d, j // d, M=12, nterms=50) / d if L <= 13000 else None
    print(f"({i},{j}) C-dd={mp.nstr(c,20)} |C-Vas_mpmath|={mp.nstr(abs(c-vv),3)} rel={mp.nstr(abs(c-vv)/vv,3)}"
          + (f" |Vas-direto|={mp.nstr(abs(vv-dr),3)}" if dr is not None else " (direto: lcm grande)"))
