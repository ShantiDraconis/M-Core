#!/usr/bin/env python3
"""Varredura estática da prova da OpenAI (Navier–Stokes): construções que poderiam burlar o kernel ou o enunciado.

Uso: python3 varredura.py <raiz do repositório openai/NavierStokesAndEuler>
"""
import json
import os
import re
import sys

PADROES = [r"\bsorry\b", r"\badmit\b", r"^\s*(private |protected )?axiom\b", r"native_decide", r"decide \+native",
           r"implemented_by", r"@\[extern", r"\bunsafe\b", r"^\s*opaque\b", r"skipKernelTC", r"\bdebug\.", r"addDecl",
           r"Lean\.Elab", r"\bEnvironment\b", r"#exit", r"^\s*elab\b", r"^\s*macro\b", r"^\s*syntax\b", r"run_cmd",
           r"run_elab", r"^\s*initialize\b", r"ofReduceBool", r"trustCompiler", r"Lean\.Kernel", r"#eval",
           r"set_option maxHeartbeats 0", r"^\s*set_option\b"]


def sem_comentarios(s):
    s = re.sub(r"/-.*?-/", "", s, flags=re.S)
    return re.sub(r"--[^\n]*", "", s)


def main(raiz):
    res = {"arquivos": 0, "linhas": 0, "ocorrencias": {}, "imports_externos": set()}
    for sub in ("NavierStokes", "Euler"):
        for dp, _, fs in os.walk(os.path.join(raiz, sub)):
            for f in fs:
                if not f.endswith(".lean"):
                    continue
                p = os.path.join(dp, f)
                txt = open(p, encoding="utf-8").read()
                res["arquivos"] += 1
                res["linhas"] += txt.count("\n")
                limpo = sem_comentarios(txt)
                for pat in PADROES:
                    for m in re.finditer(pat, limpo, re.M):
                        res["ocorrencias"].setdefault(pat, []).append(os.path.relpath(p, raiz))
                for imp in re.findall(r"^import\s+(\S+)", txt, re.M):
                    if not imp.startswith(("NavierStokes", "Euler", "Mathlib")):
                        res["imports_externos"].add(imp)
    res["imports_externos"] = sorted(res["imports_externos"])
    res["ocorrencias"] = {k: len(v) for k, v in res["ocorrencias"].items()}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    r = main(sys.argv[1] if len(sys.argv) > 1 else ".")
    sys.exit(1 if r["ocorrencias"] else 0)
