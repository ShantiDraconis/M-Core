#!/usr/bin/env python3
"""Plano do verde universal, etapas T1–T9, CALCULADO a partir das evidências do auditor.

Separa as duas metas:
  * VERDE DA BIBLIOTECA — T1–T6 e T9: tudo compila, cada teorema tem só axiomas padrão, as fontes
    estão congeladas e o portão é fail-closed;
  * VERDE UNIVERSAL DAS CONJECTURAS — T7 (enunciados reais ligados) e T8 (produtores terminais).
Nenhum estado é escrito à mão: cada etapa tem um critério verificável (ver `CRITERIOS`).
"""
import json
import os
import sys

CRITERIOS = {
    "T1": "Certificar a biblioteca e o SHA das fontes: todos os teoremas esperados com axiomas padrão.",
    "T2": "Congelar: audits/provenance.json tem o mesmo sources_sha256 das fontes atuais.",
    "T3": "Projeto Lake independente: atk-kernel/ com lakefile e lean-toolchain próprios; o núcleo lean/MCore não é tocado.",
    "T4": "Compatibilidade Lean 4.19.0 (raiz MCore) ↔ 4.34.1 (atk-kernel): resolvida por isolamento — a certificação não exige versão comum.",
    "T5": "lake build: todo arquivo auditado compila (file_status sem FAIL).",
    "T6": "#print axioms (fecho transitivo por construção) ⊆ {propext, Classical.choice, Quot.sound} e nenhuma fonte com sorry/admit/axiom.",
    "T7": "Vincular os enunciados reais: RH e Beal usam os enunciados oficiais; NS, P≠NP, Hodge, BSD e YM exigem as ligações L1–L5.",
    "T8": "Produtores terminais incondicionais: os 7 portões de scripts/terminal_gates.json certificados.",
    "T9": "Certificar só o que é verde: o portão é fail-closed (ensaio completo) e nenhum terminal foi promovido sem prova.",
}


def _toolchain(path):
    return open(path).read().strip() if os.path.exists(path) else None


def compute(root, report):
    st = report.get("status", {})
    certified, total = report.get("certified", 0), report.get("total", 0)
    flags = report.get("source_flags") or {}
    rows = report.get("theorems") or []
    ug = report.get("universal_green") or {}
    fia = report.get("fiacao") or {}
    ens = report.get("ensaio") or {}
    src = report.get("sources_sha256")

    fs = {}
    p = os.path.join(root, "reports", "file_status.txt")
    if os.path.exists(p):
        for line in open(p):
            parts = line.split()
            if len(parts) >= 2:
                fs[parts[0]] = parts[1]
    prov_p = os.path.join(root, "audits", "provenance.json")
    prov = json.load(open(prov_p)) if os.path.exists(prov_p) else {}

    tc_atk = _toolchain(os.path.join(root, "lean-toolchain"))
    tc_root = _toolchain(os.path.join(root, "..", "lean-toolchain"))
    has_lake = any(os.path.exists(os.path.join(root, f)) for f in ("lakefile.toml", "lakefile.lean"))

    steps = {}

    def put(k, state, detail):
        steps[k] = {"criterio": CRITERIOS[k], "estado": state, "detalhe": detail}

    put("T1", "GREEN" if total and certified == total else "OPEN",
        f"{certified}/{total} teoremas certificados; sources_sha256 {src}")
    if not prov:
        put("T2", "OPEN", "audits/provenance.json ausente — rode scripts/congelar.py")
    elif prov.get("sources_sha256") == src:
        put("T2", "GREEN", f"congelado em {src} ({prov.get('n_files')} arquivos)")
    else:
        put("T2", "DESATUALIZADO", f"congelado em {prov.get('sources_sha256')}, fontes atuais {src} — rode scripts/congelar.py")
    put("T3", "GREEN" if has_lake and tc_atk else "OPEN",
        f"atk-kernel: lakefile próprio = {has_lake}, toolchain {tc_atk}")
    put("T4", "GREEN" if tc_atk else "OPEN",
        f"atk-kernel {tc_atk}; raiz {tc_root or 'não presente neste checkout'} — isolados, sem ponte necessária")
    fails = [f for f, s in fs.items() if s != "OK"]
    put("T5", "GREEN" if fs and not fails else ("OPEN" if not fs else "RED"),
        f"{len(fs) - len(fails)}/{len(fs)} arquivos compilam" + (f"; falham: {', '.join(fails[:5])}" if fails else ""))
    bad_ax = [r["theorem"] for r in rows if r.get("verdict") != "CERTIFIED"]
    put("T6", "GREEN" if rows and not bad_ax and not flags else ("OPEN" if not rows else "RED"),
        f"{len(rows) - len(bad_ax)}/{len(rows)} teoremas com axiomas padrão; fontes sinalizadas: {len(flags)}")
    links = ug.get("LINKINGS_OPEN", "?")
    put("T7", "PARCIAL" if ug else "OPEN",
        f"2/7 linhas com enunciado oficial (RH, Beal); ligações abertas {links}")
    put("T8", "GREEN" if ug.get("UNIVERSAL_GREEN") else "OPEN",
        f"linhas verdes {ug.get('LINES_GREEN', '?')}; termos que faltam {fia.get('n_missing', '?')}")
    consistent = bool(ug) and ug.get("UNIVERSAL_GREEN") == (ug.get("LINES_GREEN") == "7/7")
    gate_ok = bool(ens.get("ok")) and consistent
    put("T9", "GREEN" if gate_ok else "OPEN",
        f"ensaio do portão {ens.get('passed', 'não executado')}; UNIVERSAL_GREEN {str(ug.get('UNIVERSAL_GREEN')).lower()} "
        f"com FINAL_ROOT {ug.get('FINAL_ROOT') or 'null'}")

    lib = all(steps[k]["estado"] == "GREEN" for k in ("T1", "T2", "T3", "T4", "T5", "T6", "T9"))
    conj = steps["T7"]["estado"] == "GREEN" and steps["T8"]["estado"] == "GREEN"
    counts = {}
    for v in steps.values():
        counts[v["estado"]] = counts.get(v["estado"], 0) + 1
    return {"etapas": steps, "VERDE_BIBLIOTECA": lib, "VERDE_UNIVERSAL_CONJECTURAS": conj,
            "UNIVERSAL_GREEN": bool(ug.get("UNIVERSAL_GREEN")), "FINAL_ROOT": ug.get("FINAL_ROOT"),
            "contagem": counts, "sources_sha256": src}


def markdown(res):
    c = res["contagem"]
    md = [f"### Plano do verde universal (T1–T9) — biblioteca `{'VERDE' if res['VERDE_BIBLIOTECA'] else 'ABERTA'}` · "
          f"conjecturas `{'VERDE' if res['VERDE_UNIVERSAL_CONJECTURAS'] else 'ABERTAS'}`",
          "",
          " · ".join(f"{k} {v}" for k, v in sorted(c.items())),
          "",
          "| Etapa | Critério | Estado | Evidência |", "|---|---|---|---|"]
    icon = {"GREEN": "✅", "PARCIAL": "🟡", "DESATUALIZADO": "🟠", "OPEN": "⬜", "RED": "❌"}
    for k, v in res["etapas"].items():
        md.append(f"| {k} | {v['criterio']} | {icon.get(v['estado'], '')} {v['estado']} | {v['detalhe']} |")
    md += ["", "Verde da biblioteca = T1–T6 e T9. Verde universal das conjecturas = T7 e T8, que dependem de "
           "matemática nova e de fundações ainda ausentes da Mathlib."]
    return md


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rp = os.path.join(root, "reports", "report.json")
    report = json.load(open(rp)) if os.path.exists(rp) else {}
    res = compute(root, report)
    print("\n".join(markdown(res)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
