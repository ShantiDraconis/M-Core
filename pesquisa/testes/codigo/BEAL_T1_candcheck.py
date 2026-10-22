# BEAL T1: conferencia independente da contagem de candidatas (sem o motor de padroes):
# para cada celula descoberta em S4, testa diretamente se a equacao de Beal com expoentes (x,y,z) se encaixa
# em alguma equacao assinada da permutacao de (p,q,r), aplicando as regras de sinal por enumeracao explicita.
import sys, itertools
W = sys.argv[1]
LO, HI = 3, 200; N = HI - LO + 1
L = open(f"{W}/beal_level_cons.bin", "rb").read()

def fits(xyz, sig):
    # equacao: +A^p +B^q -C^r = 0 (para cada ordenacao de sig); termos de Beal +a^x +b^y -c^z (ou todos trocados)
    for (p, q, r) in set(itertools.permutations(sig)):
        slots = ((1, p), (1, q), (-1, r))
        for flip in (1, -1):
            signs = (flip, flip, -flip)
            for perm in itertools.permutations(range(3)):
                good = True
                for i in range(3):
                    s, e = slots[perm[i]]
                    if xyz[i] % e != 0 or (signs[i] != s and e % 2 == 0):
                        good = False; break
                if good:
                    return True
    return False

for sig in [(2, 3, 13), (2, 5, 7), (3, 5, 11)]:
    c = 0
    i = 0
    for x in range(LO, HI + 1):
        for y in range(LO, HI + 1):
            for z in range(LO, HI + 1):
                if L[i] > 4 and fits((x, y, z), sig):
                    c += 1
                i += 1
    print(sig, "descobertos em S4 que cobriria:", c)
print("(3,4,7) coberto em S4?", L[((3 - LO) * N + (4 - LO)) * N + (7 - LO)] <= 4,
      "| (3,4,11)?", L[((3 - LO) * N + (4 - LO)) * N + (11 - LO)] <= 4,
      "| (3,5,7)?", L[((3 - LO) * N + (5 - LO)) * N + (7 - LO)] <= 4)
