"""Tabela certificada dos coeficientes de Keiper–Li λₙ (companheiro numérico da rodada 108).

Entrada: a saída `-out` do programa `keiper_li` da FLINT/Arb (exemplo público de F. Johansson), que calcula a série
de log ξ em s = 1 sem usar nenhum zero de ζ e devolve z_n = λₙ/n como bolas [centro ± raio] em base 2:
uma linha "n man exp rman rexp" com centro = man·2^exp e raio = rman·2^rexp.

    ./keiper_li 10000 -prec 10600 -threads 2 -out li10000.txt      (95 s, 450 MB)
    python3 li_tabela.py li10000.txt ../dados/lambda_ate_10000.tsv

Saída: n, λₙ (25 algarismos), cota inferior certificada de λₙ (arredondada para baixo), raio relativo.
Só biblioteca padrão.
"""
import sys
from fractions import Fraction
from math import floor


def ler(caminho):
    for linha in open(caminho):
        p = linha.split()
        if len(p) != 5:
            continue
        n, man, ex, rman, rex = (int(x) for x in p)
        c = Fraction(man) * Fraction(2) ** ex
        r = Fraction(rman) * Fraction(2) ** rex
        yield n, n * c, n * r


def dec(x, casas=25):
    """x arredondado para baixo com `casas` algarismos depois da vírgula."""
    q = floor(x * 10 ** casas)
    s = str(abs(q)).rjust(casas + 1, "0")
    return ("-" if q < 0 else "") + s[:-casas] + "." + s[-casas:]


def main(entrada, saida):
    with open(saida, "w") as f:
        f.write("n\tlambda_n\tcota_inferior\traio_relativo\n")
        for n, lam, rad in ler(entrada):
            if n == 0:
                continue
            f.write(f"{n}\t{dec(lam)}\t{dec(lam - rad)}\t{float(rad / lam):.3e}\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
