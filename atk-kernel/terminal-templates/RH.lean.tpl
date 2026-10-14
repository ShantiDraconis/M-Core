import ATK.FinalRoot

/-!
# Portão terminal de RH — MODELO (não compilado; vira `ATK/Terminal/RH.lean`)

Falta só o PRODUTOR: uma prova, sem hipóteses, de que não existe zero fora da linha crítica.
A ligação produtor → enunciado oficial já está certificada: `ATK.ForaDaLinha.riemann_iff_vazio`.
Para instalar: troque `PROVA_DO_PRODUTOR`, salve como `ATK/Terminal/RH.lean` e rode
`python3 scripts/instalar_portao.py RH`.
-/

namespace ATK.Terminal.RH

theorem produtor : IsEmpty ATK.ForaDaLinha.ZeroFora := PROVA_DO_PRODUTOR

theorem terminal : RiemannHypothesis := ATK.ForaDaLinha.riemann_iff_vazio.mpr produtor

end ATK.Terminal.RH

#print axioms ATK.Terminal.RH.produtor
#print axioms ATK.Terminal.RH.terminal
