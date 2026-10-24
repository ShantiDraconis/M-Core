import json, sys
from fractions import Fraction as F
plan=json.load(open(sys.argv[1]))
outdir=sys.argv[2]
def q(x):
    x=F(x)
    return f"({x.numerator} / {x.denominator} : ℚ)" if x.denominator!=1 else f"({x.numerator} : ℚ)"
def R(x): return f"(({q(x)[1:-5]} : ℚ) : ℝ)" if False else f"(({F(x).numerator}{'' if F(x).denominator==1 else ' / '+str(F(x).denominator)} : ℚ) : ℝ)"
DEL="((1 / 50 : ℚ) : ℝ)"
leaves=[]; nodes=[]
cnt=[0]
def stmt(s0,s1,a,b): return f"∀ z ∈ ret {R(s0)} {R(s1)} {R(a)} {R(b)}, {DEL} ≤ ‖riemannZeta z‖"
def walk(t,s0,s1,a,b,pref):
    if 'leaf' in t:
        L=t['leaf']; cnt[0]+=1; name=f"{pref}_{cnt[0]}"
        args=f"""(s0 := {q(L['s0'])}) (s1 := {q(L['s1'])}) (a := {q(L['a'])}) (b := {q(L['b'])}) (r := (2 / 5 : ℚ))
    (B := {q(L['B'])}) (hs := {q(L['hs'])}) (ht := {q(L['ht'])}) (h := {q(L['h'])}) (δ := (1 / 50 : ℚ))
    (v := {q(L['v'])}) (R := {q(L['R'])}) (d := {q(L['d'])}) (ns := {L['ns']}) (nt := {L['nt']})
    (Nc := {L['Nc']}) (Mc := {L['Mc']}) (Ne := {L['Ne']}) (Me := 8) (K := 16) (nT := 24) (p := 32)"""
        nn=" ".join(["(by norm_num)"]*18)
        body=f"""set_option maxRecDepth 100000 in
/-- Peça `[{L['s0']}, {L['s1']}] × [{L['a']}, {L['b']}]`: {L['ns']}×{L['nt']} centros. -/
theorem {name} : {stmt(L['s0'],L['s1'],L['a'],L['b'])} :=
  peca_ret {args}
    {nn}
    (by decide +kernel) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by decide +kernel)
"""
        leaves.append((name,body,L['ns']*L['nt']*L['Ne']))
        return name
    kind='re' if 're' in t else 'im'
    mid=F(t[kind])
    if kind=='re':
        l=walk(t['l'],s0,mid,a,b,pref); r=walk(t['r'],mid,s1,a,b,pref)
        lem=f"ret_split_re (sm := {R(mid)})"
    else:
        l=walk(t['l'],s0,s1,a,mid,pref); r=walk(t['r'],s0,s1,mid,b,pref)
        lem=f"ret_split_im (tm := {R(mid)})"
    cnt[0]+=1; name=f"{pref}_{cnt[0]}"
    nodes.append((name,f"theorem {name} : {stmt(s0,s1,a,b)} :=\n  {lem} {l} {r}\n"))
    return name
strips=[]
for k,st in enumerate(plan):
    leaves.clear(); nodes.clear(); cnt[0]=0
    a,b=F(st['a']),F(st['b'])
    top=walk(st['tree'],F(1,2),F(1),a,b,f"P{k}")
    strips.append(dict(k=k,a=a,b=b,top=top,leaves=list(leaves),nodes=list(nodes),w=sum(x[2] for x in leaves)))
# distribute strips to files
nf=int(sys.argv[3])
groups=[[] for _ in range(nf)]; ws=[0]*nf
for st in sorted(strips,key=lambda s:-s['w']):
    i=ws.index(min(ws)); groups[i].append(st); ws[i]+=st['w']
print("pesos",ws)
for i,g in enumerate(groups):
    g.sort(key=lambda s:s['k'])
    parts=[f"""import ATK.ZeroClasses.FaixaGeral

/-!
# Peças da faixa sem zeros, arquivo {i+1} de {nf} (rodada 29)

Retângulos `[s0, s1] × [a, b]` dentro de `[½, 1] × [43/50, 13]`, cada um certificado por `peca_ret` com `δ = 1/50`
(todas as avaliações de `ζ` nos centros verificadas pelo kernel com `decide +kernel`).
-/

open Complex

namespace ATK.ZeroClasses.Faixa
"""]
    for st in g:
        parts.append(f"\n/-! ## Faixa `{st['a']} ≤ t ≤ {st['b']}` -/\n")
        for name,body,_ in st['leaves']: parts.append("\n"+body)
        for name,body in st['nodes']: parts.append("\n"+body)
        parts.append(f"\n/-- **A faixa `[½, 1] × [{st['a']}, {st['b']}]`.** -/\ntheorem faixa_{st['k']} : {stmt(F(1,2),F(1),st['a'],st['b'])} :=\n  {st['top']}\n")
    parts.append("\nend ATK.ZeroClasses.Faixa\n")
    open(f"{outdir}/FaixaPecas{i+1}.lean","w").write("".join(parts))
json.dump([dict(k=s['k'],a=str(s['a']),b=str(s['b']),arquivo=[i+1 for i,g in enumerate(groups) if s in g][0],
                leaves=len(s['leaves']),centros=sum(x[2] for x in s['leaves'])//1) for s in strips],open(f"{outdir}/faixa_meta.json","w"))
