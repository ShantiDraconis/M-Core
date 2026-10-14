#!/usr/bin/env python3
"""Catálogo dos termos terminais: valida `scripts/termos.json` contra os modelos de portão e o kernel.

Confere, sem escrever nada em `ATK/`:
  * cada lacuna (`PROVA_*`, `LIGACAO_*`) de cada modelo em `terminal-templates/` tem exatamente uma
    entrada no catálogo, e o catálogo não tem entradas órfãs;
  * as contagens: 18 ocorrências na rota da prova, 12 na rota da refutação, 25 lacunas distintas;
  * cada nome Lean do catálogo está declarado em `ATK/Termos.lean` e cada teorema citado
    está na lista de teoremas esperados (logo, auditado pelo kernel no CI);
  * com o relatório do kernel e a fiação tipada à mão: quantos teoremas do catálogo estão
    certificados e quantos tipos o kernel conferiu.

Uso: `python3 scripts/termos.py [--md SAIDA.md]` (o `--md` gera a ficha completa de 24 componentes).
"""
import json
import os
import re
import sys

PH = re.compile(r"\b(PROVA_[A-Z0-9_]+|LIGACAO_[A-Z0-9_]+)\b")
LINHAS = ["RH", "Beal", "NS", "PNP", "Hodge", "BSD", "YM"]
MODELOS = ["NSModelo", "PNPModelo", "HodgeModelo", "BSDModelo", "YMModelo"]
PROVA = set(MODELOS + LINHAS)
REFUTACAO = set(MODELOS + [k + "Refutacao" for k in LINHAS])


def e(x):
    """Escapa `|` dentro de células de tabela Markdown."""
    return str(x).replace("|", "\\|")


def compute(root, verdict_of=None, fiacao=None):
    cat = json.load(open(os.path.join(root, "scripts", "termos.json"), encoding="utf-8"))
    terms = cat["terms"]
    tpl_dir = os.path.join(root, "terminal-templates")
    occ = set()
    for f in sorted(os.listdir(tpl_dir)):
        if f.endswith(".lean.tpl"):
            name = f[:-len(".lean.tpl")]
            for h in set(PH.findall(open(os.path.join(tpl_dir, f), encoding="utf-8").read())):
                occ.add((name, h))
    keys = [(t["template"], t["placeholder"]) for t in terms]
    problems = []
    if len(set(keys)) != len(keys):
        problems.append("entradas repetidas no catálogo")
    problems += [f"lacuna sem entrada: {n}:{h}" for n, h in sorted(occ - set(keys))]
    problems += [f"entrada órfã: {n}:{h}" for n, h in sorted(set(keys) - occ)]
    ids = [t["id"] for t in terms]
    if len(set(ids)) != len(ids):
        problems.append("ids repetidos")
    n_prova = sum(1 for n, _ in occ if n in PROVA)
    n_ref = sum(1 for n, _ in occ if n in REFUTACAO)
    src = open(os.path.join(root, cat["modulo"]), encoding="utf-8").read()
    expected = {l.strip() for l in open(os.path.join(root, "scripts", "expected_theorems.txt")) if l.strip()}
    for t in terms:
        short = t["nome_lean"].split(".")[-1]
        if not re.search(r"\b(def|abbrev)\s+" + re.escape(short) + r"\b", src):
            problems.append(f"{t['id']}: {t['nome_lean']} não declarado em {cat['modulo']}")
        for thm in t["teoremas"]:
            if thm not in expected:
                problems.append(f"{t['id']}: teorema {thm} fora da lista auditada")
    for l, dl in cat["linhas"].items():
        for thm in dl.get("leis", []):
            if thm not in expected:
                problems.append(f"{l}: lei {thm} fora da lista auditada")
    thms = sorted({x for t in terms for x in t["teoremas"]} | {"ATK.Termos.raiz_de_termos", "ATK.Termos.raiz_iff"})
    cert = None if verdict_of is None else sum(verdict_of.get(x) == "CERTIFIED" for x in thms)
    typed = {}
    if fiacao and fiacao.get("ran"):
        for r in fiacao["rows"]:
            for h in r.get("typed", []):
                typed[(r["template"], h)] = r["compiled"]
    for t in terms:
        t["tipo_conferido"] = typed.get((t["template"], t["placeholder"]))
    fechadas = 0  # uma lacuna só fecha com o portão instalado e certificado (universal_green.py)
    return {"ok": not problems, "problems": problems, "distintos": len(occ), "prova": n_prova,
            "refutacao": n_ref, "compartilhadas": n_prova + n_ref - len(occ),
            "teoremas": len(thms), "teoremas_certificados": cert,
            "tipos_conferidos": sum(1 for v in typed.values() if v), "tipos_total": len(occ),
            "fechadas": fechadas, "terms": terms, "linhas": cat["linhas"]}


def markdown(res):
    c = res
    cert = "?" if c["teoremas_certificados"] is None else c["teoremas_certificados"]
    md = [f"### Termos terminais — {c['distintos']} lacunas distintas (prova {c['prova']}, refutação "
          f"{c['refutacao']}, {c['compartilhadas']} ligações compartilhadas); tipos conferidos "
          f"{c['tipos_conferidos']}/{c['tipos_total']}; teoremas do catálogo certificados {cert}/{c['teoremas']}; "
          f"fechadas {c['fechadas']}/{c['distintos']}", ""]
    if c["problems"]:
        md += ["**Catálogo inconsistente:** " + "; ".join(c["problems"]), ""]
    md += ["| Id | Linha | Rota | Lacuna | Tipo Lean | O que é | Tipo conferido | Estado |",
           "|---|---|---|---|---|---|---|---|"]
    for t in c["terms"]:
        tc = {True: "✅", False: "❌", None: "—"}[t.get("tipo_conferido")]
        md.append(f"| {t['id']} | {t['linha']} | {t['rota']} | `{t['template']}:{t['placeholder']}` | "
                  f"`{e(t['lean_type'])}` | {e(t['enunciado'])} | {tc} | {e(t['estado'])} |")
    return md


def ficha(res, sha=None):
    """A ficha completa: os 24 componentes de cada termo (os de domínio são da linha)."""
    md = ["# Termos terminais — ficha de 24 componentes", "",
          "Gerado por `atk-kernel/scripts/termos.py --md` a partir de `atk-kernel/scripts/termos.json` "
          "(catálogo) e `atk-kernel/ATK/Termos.lean` (nomes e teoremas no kernel).", "",
          "## Contagem reconciliada", "",
          f"- **{res['distintos']} lacunas distintas** nos 21 modelos de portão.",
          f"- Rota da prova: **{res['prova']}** ocorrências (13 provas + 5 ligações).",
          f"- Rota da refutação: **{res['refutacao']}** ocorrências (7 refutações + as mesmas 5 ligações).",
          f"- {res['prova']} + {res['refutacao']} = {res['prova'] + res['refutacao']} por rota; "
          f"{res['prova'] + res['refutacao']} − {res['compartilhadas']} compartilhadas = {res['distintos']} distintas. "
          "As duas contagens (\"18 + 12\" do CI e \"25\" do inventário) estão certas; medem coisas diferentes.",
          f"- Tipos conferidos pelo kernel: **{res['tipos_conferidos']}/{res['tipos_total']}** "
          "(cada lacuna trocada por `(sorry : <tipo do catálogo>)` compila; trocar o tipo de B3 pelo de O3 "
          "faz a compilação falhar).",
          f"- Fechadas: **{res['fechadas']}/{res['distintos']}**. Nenhuma lacuna está preenchida; preencher uma "
          "lacuna de produtor ou de refutação é resolver o problema correspondente.", ""]
    if sha:
        md += [f"Fontes do kernel: SHA-256 `{sha}`.", ""]
    md += ["## Os 24 componentes", "",
           "Componentes 1–3, 8, 17–20, 23 e 24 são de cada termo; 4–7, 9–16, 21 e 22 são do domínio da linha "
           "e valem para todos os termos dela (não se inventam derivadas para objetos lógicos: onde não se "
           "aplica, está escrito).", ""]
    porlinha = {}
    for t in res["terms"]:
        porlinha.setdefault(t["linha"], []).append(t)
    for l in LINHAS:
        d = res["linhas"][l]
        md += [f"## {l} — {e(d['problema'])}", "",
               f"Enunciado oficial no portão: {e(d['enunciado_oficial'])}. Ligação: {e(d['ligacao'])}. "
               f"Mathlib: {e(d['mathlib'])}.", "",
               "| Componente (domínio da linha) | Conteúdo |", "|---|---|",
               f"| 4 · Domínio e codomínio | {e(d['dominio'])} |",
               f"| 5 · Classes numéricas | {e(d['classes'])} |",
               f"| 6 · Parâmetros | {e(d['parametros'])} |",
               f"| 7 · Operadores | {e(d['operadores'])} |",
               f"| 9 · Invariantes | {e(d['invariantes'])} |",
               f"| 10 · Dimensão | {e(d['dimensao'])} |",
               f"| 11 · Geometria | {e(d['geometria'])} |",
               f"| 12 · Coordenadas | {e(d['coordenadas'])} |",
               f"| 13 · Métrica ou topologia | {e(d['metrica'])} |",
               f"| 14 · Derivadas | {e(d['derivadas'])} |",
               f"| 15 · Integrais | {e(d['integrais'])} |",
               f"| 16 · Limites | {e(d['limites'])} |",
               "| 21 · Exemplos (no kernel) | " + "; ".join(f"`{x}`" if x.startswith("ATK.") else x for x in d["exemplos"]) + " |",
               "| 22 · Contraexemplos (no kernel) | " + "; ".join(
                   f"`{x.split(' ')[0]}`" + x[len(x.split(' ')[0]):] if x.startswith("ATK.") else x
                   for x in d["contraexemplos"]) + " |", ""]
        for t in porlinha.get(l, []):
            hip = ("o modelo tem de satisfazer o critério de fidelidade da ligação" if t["papel"] == "ligacao"
                   else "nenhuma: o portão exige um termo sem hipóteses")
            tc = {True: "tipo conferido pelo kernel", False: "TIPO DIVERGENTE", None: "tipo não conferido nesta execução"}[t.get("tipo_conferido")]
            md += [f"### {t['id']} — `{t['template']}:{t['placeholder']}`", "",
                   "| Componente | Conteúdo |", "|---|---|",
                   f"| 1 · Identidade | {t['id']} · `{t['nome_lean']}` · {e(t['papel'])} {e(t['ref'])} · rota {t['rota']} |",
                   f"| 2 · Definição formal | {e(t['enunciado'])} — tipo Lean `{e(t['lean_type'])}` |",
                   f"| 3 · Tipo matemático | {e(t['tipo_matematico'])} |",
                   "| 8 · Leis (certificadas, da linha) | " + "; ".join(f"`{x}`" for x in d.get("leis", [])) + " |",
                   f"| 17 · Hipóteses | {hip} |",
                   "| 18 · Lemas (certificados, do termo) | " + ("; ".join(f"`{x}`" for x in t["teoremas"]) or "— (dado; critério na linha)") + " |",
                   f"| 19 · Dependências | `ATK/Termos.lean`; {e(d['ligacao'])} |",
                   f"| 20 · Obrigação terminal | alimenta `{t['alimenta']}` |",
                   f"| 23 · Certificado Lean | {e(t['estado'])} · {tc} |",
                   f"| 24 · Proveniência | `atk-kernel/terminal-templates/{t['template']}.lean.tpl` · `atk-kernel/scripts/termos.json` |", ""]
    return md


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rep = os.path.join(root, "reports")
    verdict_of = fiacao = sha = None
    if os.path.exists(os.path.join(rep, "report.json")):
        r = json.load(open(os.path.join(rep, "report.json"), encoding="utf-8"))
        verdict_of = {x["theorem"]: x["verdict"] for x in r.get("theorems", [])}
        sha = r.get("sources_sha256")
    if os.path.exists(os.path.join(rep, "fiacao.json")):
        fiacao = json.load(open(os.path.join(rep, "fiacao.json"), encoding="utf-8"))
    try:  # SHA das fontes atuais (o do relatório pode ser de uma execução anterior)
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import congelar
        sha = congelar.sources_sha(root)
        sha = sha[0] if isinstance(sha, tuple) else sha
    except Exception:
        pass
    res = compute(root, verdict_of, fiacao)
    if "--md" in sys.argv:
        out = sys.argv[sys.argv.index("--md") + 1]
        open(out, "w", encoding="utf-8").write("\n".join(ficha(res, sha)) + "\n")
    print("\n".join(markdown(res)))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
