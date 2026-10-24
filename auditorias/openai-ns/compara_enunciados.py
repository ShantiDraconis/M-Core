#!/usr/bin/env python3
"""Compara, sem comentários, três textos: o enunciado da Formal Conjectures (DeepMind, commit 8bf45ed), o desafio do
repositório da OpenAI (ComparatorChallenges/NavierStokes.lean) e as definições usadas pela solução
(NavierStokes/ComparatorDefinitions.lean). Imprime as diferenças linha a linha.

Uso: python3 compara_enunciados.py <formal-conjectures/.../NavierStokes.lean> <desafio> <definicoes>
"""
import difflib
import re
import sys


def linhas(p):
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"/-.*?-/", "", s, flags=re.S)
    s = re.sub(r"--[^\n]*", "", s)
    return [l.rstrip() for l in s.split("\n") if l.strip()]


def diff(a, b, na, nb):
    d = list(difflib.unified_diff(linhas(a), linhas(b), na, nb, lineterm="", n=0))
    print(f"### {na} → {nb}: {len(d)} linhas de diff")
    print("\n".join(d))
    return d


if __name__ == "__main__":
    up, des, defs = sys.argv[1:4]
    diff(up, des, "formal-conjectures", "desafio-openai")
    d2 = diff(des, defs, "desafio-openai", "definicoes-da-solucao")
    # a única diferença admitida entre desafio e definições é a remoção dos dois teoremas com `sorry`
    extra = [l for l in d2 if l.startswith("+") and not l.startswith("+++")]
    sys.exit(1 if extra else 0)
