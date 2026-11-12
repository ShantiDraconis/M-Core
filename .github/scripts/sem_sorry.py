#!/usr/bin/env python3
"""Procura `sorry` e `admit` no código Lean, fora de comentários e de strings.

Substitui o `grep '\\bsorry\\b'` que marcava a palavra dentro de docstrings (alarme falso de 11/11/2026 em
`MCore/IBoundaryProvenance.lean`: "A no-axiom/no-sorry kernel"). O teste em `audit/testes_portao/` mostra por
que isto continua sendo só uma primeira barreira: `sorryAx` escrito direto passa por qualquer busca de texto,
e quem pega é o kernel (`#print axioms`) ou o aviso `declaration uses 'sorry'` no log de compilação.

Uso: python3 sem_sorry.py <arquivo-ou-pasta> ...   (sai com 1 se achar)
"""
import pathlib
import re
import sys


def codigo(s: str) -> str:
    """O texto sem comentários (de linha e de bloco, aninhados) e com as strings esvaziadas."""
    out, i, n, prof = [], 0, len(s), 0
    while i < n:
        if s.startswith("/-", i):
            prof, i = prof + 1, i + 2
        elif prof and s.startswith("-/", i):
            prof, i = prof - 1, i + 2
        elif prof:
            if s[i] == "\n":  # mantém as quebras de linha para a numeração bater com a fonte
                out.append("\n")
            i += 1
        elif s.startswith("--", i):
            j = s.find("\n", i)
            i = n if j < 0 else j
        elif s[i] == '"':
            j = i + 1
            while j < n and s[j] != '"':
                j += 2 if s[j] == "\\" else 1
            out.append('""')
            i = j + 1
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def main() -> int:
    achados = []
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        for f in sorted([p] if p.is_file() else p.rglob("*.lean")):
            c = codigo(f.read_text(encoding="utf-8"))
            for m in re.finditer(r"\b(sorry|admit)\b", c):
                linha = c.count("\n", 0, m.start()) + 1
                achados.append(f"{f}:{linha}: {m.group(0)}")
    print("\n".join(achados) or "sem sorry/admit no código")
    return 1 if achados else 0


if __name__ == "__main__":
    sys.exit(main())
