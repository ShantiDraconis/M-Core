#!/usr/bin/env python3
"""Classifica os 2.440 teoremas do FINAL_PROOF_STRUCTURE (inventários do kernel).

Para cada teorema dos 7 inventários (PUBLICATION/MASTER/inventories/<lane>/PROOF_INVENTORY.json):
  * localiza o arquivo do módulo no commit exato que o CI verificou (sources.json);
  * extrai a assinatura (binders + conclusão) do código-fonte nesse commit;
  * classifica a forma: ENDPOINT, CONDICIONAL→alvo, EQUIVALÊNCIA, REFUTAÇÃO/NEGAÇÃO,
    STATUS/REGISTRO, ESTRUTURAL;
  * associa a obrigação do livro-razão (O1–O8, B1–B7, L1–L5) por palavras-chave;
  * tenta descarregar as hipóteses dos condicionais usando os PRÓPRIOS 2.440 teoremas
    (tipo normalizado idêntico, sem hipóteses).

Uso: thm2440.py <M-Core dir> <dir com clones> <saida.json>
"""
import json, os, re, subprocess, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import proof_scan as ps
import hyp_map as hm

REPO_DIR = {"m-core-riemann": "m-core-riemann", "m-core-p-vs-np": "m-core-p-vs-np",
            "navier-stokes-critical-barrier-audit": "navier-stokes-critical-barrier-audit",
            "m-core-hodge": "m-core-hodge", "m-core-bsd": "m-core-bsd",
            "m-core-yang-mills": "m-core-yang-mills", "m-core-beal": "m-core-beal"}

# obrigação do livro-razão -> padrões (nome ou conclusão)
OBLIG = [
    ("O1", "riemann", r"FiniteSpanApproximatesChi|UniformLogBound|ConcreteUniformLogDNBound|LogMajorant|VanishingUpperBound|DNLimit|DNToZero|OfficialSpecRH|RiemannHypothesis|ExplicitGramRate"),
    ("O2", "beal", r"BealConjecture|GCDLowerBound|BealUniversal|ScientificFrontier|ReducedCandidate|NoPrimitiveEquation|GlobalElimination"),
    ("O3", "navier-stokes", r"ClayStatementA|ActualNS|G1Bridge|SignedGain|EnstrophyAPriori|NavierStokesStabilization|GlobalSmooth|Regularity"),
    ("O4", "pvsnp", r"PneqNP|PneNP|SATNotInP|UniversalSATFailure|UniversalFailure|G21Pointwise|MachinePneqNP|FINAL_PROOF_RESIDUAL|MinimalSeparation"),
    ("O5", "hodge", r"HodgeConjecture|ConcreteAlgebraicityPayload|HodgeRealization|AlgebraicCycle"),
    ("O6", "bsd", r"BSDRank|RankOpen|RankResidual|RankPart|BSDRealizable"),
    ("O7", "bsd", r"BSDFull|RefinedOpen|Refined|LeadingCoefficient|Sha\b|Regulator"),
    ("O8", "yang-mills", r"ClayYM|YangMillsMassGap|MassGap|YangMills4DGap|ConstructiveYM4D|B60ConcretePhysicalAdapter|OsterwalderSchrader"),
]
OBLIG_RX = [(o, p, re.compile(rx)) for o, p, rx in OBLIG]
STATUS_RX = re.compile(r"\.(openMath|proved|closed|open|blocked|green|red|pending|fail|certified)\b|=\s*(true|false)\b|"
                       r"\b(state|status|credit|count|Count|registry|Registry|ledger|Ledger)\b")


def git(repo, *a, inp=None):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, input=inp).stdout


def norm(t):
    return hm.norm(t)


def find_decl(code, fullname):
    last = fullname.split(".")[-1]
    pref = ".".join(fullname.split(".")[:-1])
    rx = re.compile(r"^[ \t]*(?:@\[[^\]]*\][ \t]*\n?[ \t]*)?(?:(?:private|protected|noncomputable)\s+)*"
                    r"(theorem|lemma)\s+((?:[\w'.!?]+\.)?" + re.escape(last) + r")(?=[\s(:{\[⦃])", re.M)
    best = None
    for m in rx.finditer(code):
        dotted = m.group(2)
        score = 2 if fullname.endswith(dotted) else 1
        if best is None or score > best[0]:
            best = (score, m)
    if not best:
        return None
    m = best[1]
    rest = code[m.end():]
    # cabeçalho até ':=' / 'where' / '|' de nível zero
    depth, i, head = 0, 0, None
    while i < len(rest):
        ch = rest[i]
        if ch in "([{⦃⟨": depth += 1
        elif ch in ")]}⦄⟩": depth -= 1
        elif depth == 0 and rest.startswith(":=", i):
            head = rest[:i]; break
        elif depth == 0 and re.match(r"\n\s*\|", rest[i:i+40]) and i > 0:
            head = rest[:i]; break
        elif depth == 0 and rest.startswith(" where", i):
            head = rest[:i]; break
        i += 1
    if head is None:
        head = rest[:600]
    head = " ".join(head.split())
    binders, concl = ps.split_signature(head)
    hyps = []
    for opener, inner in hm.top_binders(binders):
        if opener != "(": continue
        names, typ = hm.binder_type(inner)
        if typ: hyps.append(norm(typ))
    inst = len(re.findall(r"\[[^\]]*\]", binders))
    return {"kind": m.group(1), "binders": binders.strip()[:400], "conclusion": norm(concl)[:400],
            "hyps": hyps, "line": code[:m.start()].count("\n") + 1}


def shape(sig, name):
    c = sig["conclusion"]
    core = re.sub(r"^(Nonempty\s*\(?|\(\s*)+", "", c)
    t = ps.TARGET_RX.search(core)
    is_neg = c.startswith("¬") or c.startswith("Not ") or c.endswith("→False") or c == "False" \
        or re.search(r"refuted|_false$|impossible|not_", name)
    if "↔" in c:
        return "EQUIVALENCIA"
    if is_neg:
        return "REFUTACAO_OU_NEGACAO"
    if t and not sig["hyps"] and ps.TARGET_RX.match(core):
        return "ENDPOINT_OU_ALVO_SEM_HIPOTESE"
    if t and (sig["hyps"] or "→" in c):
        return "CONDICIONAL_PARA_ALVO"
    if STATUS_RX.search(c):
        return "STATUS_OU_REGISTRO"
    if sig["hyps"] or "→" in c:
        return "IMPLICACAO_ESTRUTURAL"
    return "ESTRUTURAL"


def main(mcore, clones, outp):
    master = os.path.join(mcore, "PUBLICATION", "MASTER")
    sources = {p["id"]: p for p in json.load(open(os.path.join(master, "sources.json")))["problems"]}
    rows, missing = [], []
    for lane, src in sources.items():
        inv = json.load(open(os.path.join(master, "inventories", lane, "PROOF_INVENTORY.json")))
        repo = os.path.join(clones, REPO_DIR[src["repository"].split("/")[1]])
        commit = src["commit"]
        files = [l for l in git(repo, "ls-tree", "-r", "--name-only", commit).decode().splitlines()
                 if l.endswith(".lean")]
        cache = {}
        for th in inv["theorems"]:
            mod = th["module"]
            suffix = mod.replace(".", "/") + ".lean"
            cands = [f for f in files if f == suffix or f.endswith("/" + suffix)]
            sig = None
            for f in cands:
                if f not in cache:
                    cache[f] = ps.strip_comments(git(repo, "show", f"{commit}:{f}").decode("utf-8", "replace"))
                sig = find_decl(cache[f], th["name"])
                if sig:
                    sig["path"] = f; break
            if not sig:  # procura em qualquer arquivo (módulos agregadores / nomes gerados)
                last = th["name"].split(".")[-1]
                for f in files:
                    if f not in cache:
                        cache[f] = ps.strip_comments(git(repo, "show", f"{commit}:{f}").decode("utf-8", "replace"))
                    if last in cache[f]:
                        sig = find_decl(cache[f], th["name"])
                        if sig:
                            sig["path"] = f; break
            if not sig:  # campo Prop de structure/class (projeção: hipótese empacotada, não prova)
                parts = th["name"].split(".")
                if len(parts) >= 2:
                    st, fld = parts[-2], parts[-1]
                    srx = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(structure|class)\s+" + re.escape(st) + r"\b(.*?)(?=^\S|\Z)", re.M | re.S)
                    for f in cands + files:
                        if f not in cache:
                            cache[f] = ps.strip_comments(git(repo, "show", f"{commit}:{f}").decode("utf-8", "replace"))
                        if st not in cache[f]: continue
                        m = srx.search(cache[f])
                        if m:
                            fm = re.search(r"(?:^|\(|\s)" + re.escape(fld) + r"\s*:\s*([^\n]*)", m.group(2))
                            if fm:
                                sig = {"kind": "field", "binders": "", "conclusion": norm(fm.group(1))[:400],
                                       "hyps": [], "line": cache[f][:m.start()].count("\n") + 1, "path": f,
                                       "field_of": st}
                                break
            row = {"lane": lane, "name": th["name"], "module": mod, "status": th["status"],
                   "axioms": th["axioms"], "repo": src["repository"], "commit": commit[:8]}
            if not sig:
                row.update({"shape": "SEM_FONTE_LOCALIZADA"}); missing.append(th["name"])
            else:
                row.update(sig)
                row["shape"] = "CAMPO_DE_ESTRUTURA_HIPOTESE" if sig.get("kind") == "field" else shape(sig, th["name"])
                txt = th["name"] + " " + sig["conclusion"]
                row["obligations"] = sorted({o for o, p, rx in OBLIG_RX if rx.search(txt)})
            rows.append(row)
        print(f"{lane}: {len(inv['theorems'])} teoremas, sem fonte={sum(1 for r in rows if r['lane']==lane and r['shape']=='SEM_FONTE_LOCALIZADA')}", flush=True)

    # descarga interna: hipóteses de condicionais provadas por algum teorema sem hipótese dos 2.440
    proved_types = defaultdict(list)
    for r in rows:
        if r.get("conclusion") and r.get("kind") != "field" and not r.get("hyps") and r["status"] == "CLEAN" and "→" not in r["conclusion"] \
                and not re.search(r"\b(∀|∃)", r.get("binders", "")):
            if not r.get("binders") or not re.search(r"\(", r["binders"]):
                proved_types[r["conclusion"]].append(r["name"])
    for r in rows:
        if r.get("shape") == "CONDICIONAL_PARA_ALVO":
            dis = {h: proved_types.get(h, [])[:2] for h in r["hyps"]}
            r["hyp_discharge"] = dis
            r["fully_discharged"] = bool(r["hyps"]) and all(dis.values())

    # props do kernel
    props = []
    for lane in sources:
        inv = json.load(open(os.path.join(master, "inventories", lane, "PROOF_INVENTORY.json")))
        for p in inv["props"]:
            props.append({"lane": lane, **p})
    summary = {
        "total": len(rows),
        "by_lane": Counter(r["lane"] for r in rows),
        "by_shape": Counter(r["shape"] for r in rows),
        "by_lane_shape": {l: Counter(r["shape"] for r in rows if r["lane"] == l) for l in sources},
        "by_obligation": Counter(o for r in rows for o in r.get("obligations", [])),
        "conditionals_fully_discharged": [r["name"] for r in rows if r.get("fully_discharged")],
        "props_by_status": Counter(p["status"] for p in props),
        "missing_source": len(missing),
    }
    json.dump({"summary": summary, "props": props, "theorems": rows}, open(outp, "w"), ensure_ascii=False, indent=1)
    print(json.dumps(summary, ensure_ascii=False, indent=1, default=dict))


if __name__ == "__main__":
    main(*sys.argv[1:4])
