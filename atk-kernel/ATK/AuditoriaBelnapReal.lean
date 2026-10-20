import ATK.StatusHonesto

/-!
# ATK — Auditoria Belnap real sobre as 8 pontes, 8 obrigações e as ligações

Este arquivo aplica `ATK.StatusHonesto.Evidencia`/`ValorBelnap` aos itens reais listados em
`scripts/obligations.json` (pontes B1–B8, obrigações O1–O8, ligações L1/L2) **um por um** —
nunca como um único valor agregado para "`OPEN_MATH`" ou "`CLOSED_MATH`" inteiros. Essas duas
camadas são conjunções de itens heterogêneos (`ATK.ClosedMath.OpenObligations`, `Bridges`):
combinar evidência de itens não relacionados sob uma regra "qualquer favor / qualquer contra"
produziria um artefato da agregação, não um veredito que signifique algo sobre a conjunção
inteira. Por isso este arquivo audita cada item separadamente, e nenhuma prova aqui atribui um
`ValorBelnap` a `OPEN_MATH` ou `CLOSED_MATH` como um todo.

Regras seguidas (ver a ressalva em `ATK.StatusHonesto`):
* `temAFavor := true` só quando `scripts/obligations.json` marca o item como
  `PROVADA_NO_KERNEL`/`CLOSED`, citando o `proof_theorem` real.
* `temContra := true` só quando existe, no próprio kernel, uma prova específica que mina a
  reivindicação — nunca a mera ausência de uma prova.
-/

namespace ATK.AuditoriaBelnapReal

open ATK.StatusHonesto

/-! ## Pontes (B1–B8) -/

/-- B1 — ponte de Riemann (Nyman–Beurling–Báez-Duarte): `PROVADA_NO_KERNEL`. -/
def b1 : Evidencia :=
  { camada := "BRIDGE", claim := "B1 (Riemann, Nyman–Beurling–Báez-Duarte)",
    temAFavor := true, temContra := false, fonte := "scripts/obligations.json, B1",
    prova := some "ATK.ObligationsClosed.B1" }

/-- B4 — ponte de P vs NP (Cook–Levin) sobre o modelo genuíno `ATK.ModeloPNP.modeloPNP`:
`PROVADA_NO_KERNEL`. -/
def b4 : Evidencia :=
  { camada := "BRIDGE", claim := "B4 (P vs NP, Cook–Levin)",
    temAFavor := true, temContra := false, fonte := "scripts/obligations.json, B4",
    prova := some "ATK.ObligationsClosed.B4" }

/-- B2 — ponte de Beal (FLT): `PARCIAL_NO_MODELO_DO_LANE`, não certificada como obrigação
fechada. -/
def b2 : Evidencia :=
  { camada := "BRIDGE", claim := "B2 (Beal, FLT)", temAFavor := false, temContra := false,
    fonte := "scripts/obligations.json, B2 (PARCIAL_NO_MODELO_DO_LANE)" }

/-- B3, B5, B6, B7, B8 — publicadas na literatura, não formalizadas no kernel. -/
def b3 : Evidencia :=
  { camada := "BRIDGE", claim := "B3 (Navier–Stokes, Leray)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, B3" }

def b5 : Evidencia :=
  { camada := "BRIDGE", claim := "B5 (Hodge, Lefschetz)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, B5" }

def b6 : Evidencia :=
  { camada := "BRIDGE", claim := "B6 (BSD, Gross–Zagier–Kolyvagin)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, B6" }

def b7 : Evidencia :=
  { camada := "BRIDGE", claim := "B7 (Yang–Mills, Osterwalder–Schrader)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, B7" }

def b8 : Evidencia :=
  { camada := "BRIDGE", claim := "B8 (Beal, Darmon–Merel)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, B8" }

/-! ## Obrigações abertas (O1–O8) -/

/-- Nenhuma das 8 obrigações abertas tem prova nem refutação no kernel. Faltar a prova não é
evidência contra (ver `ATK.StatusHonesto`): é `nenhum`, nunca `ambos`. -/
def o1 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O1 (Riemann, UniformLogBound)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, O1 (OPEN_MATH)" }

def o2 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O2 (Beal, GCDLowerBoundSmallExponents)",
    temAFavor := false, temContra := false, fonte := "scripts/obligations.json, O2 (OPEN_MATH)" }

def o3 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O3 (Navier–Stokes, EnstrophyAPrioriBound)",
    temAFavor := false, temContra := false, fonte := "scripts/obligations.json, O3 (OPEN_MATH)" }

def o4 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O4 (P vs NP, SATNotInP)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, O4 (OPEN_MATH)" }

def o5 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O5 (Hodge, MiddleCodimension)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, O5 (OPEN_MATH)" }

def o6 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O6 (BSD, cota superior do posto)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, O6 (OPEN_MATH)" }

def o7 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O7 (BSD, segunda obrigação)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, O7 (OPEN_MATH)" }

def o8 : Evidencia :=
  { camada := "OPEN_MATH", claim := "O8 (Yang–Mills, mass gap)", temAFavor := false,
    temContra := false, fonte := "scripts/obligations.json, O8 (OPEN_MATH)" }

/-! ## O caso real de `ambos`: o esquema paramétrico sem a ligação fixada -/

/-- `L1` (ligação de Navier–Stokes) está `CLOSED` no modelo genuíno — isso continua só a favor.
Mas o **mesmo esquema** `ClayStatementA M`, antes de fixar esse modelo genuíno, também é
satisfeito trivialmente por um modelo de brinquedo vazio (`ns_toy_model_vacuous`), e
`ns_depende_do_modelo` prova que o esquema é verdadeiro num modelo e falso noutro. Isso é
evidência real e específica contra tratar o esquema paramétrico, por si só, como significativo
— um caso legítimo de `ambos`, distinto de `L1` em si. -/
def esquemaNS_sem_ligacao : Evidencia :=
  { camada := "LIGAÇÃO", claim := "esquema NS paramétrico antes de fixar L1",
    temAFavor := true, temContra := true,
    fonte := "ATK.ClosedMath.ns_toy_model_vacuous + ATK.FinalRoot.ns_depende_do_modelo" }

/-- O mesmo para `L2` / P vs NP: `pnp_toy_model_vacuous` + `pnp_depende_do_modelo`. -/
def esquemaPNP_sem_ligacao : Evidencia :=
  { camada := "LIGAÇÃO", claim := "esquema P vs NP paramétrico antes de fixar L2",
    temAFavor := true, temContra := true,
    fonte := "ATK.ClosedMath.pnp_toy_model_vacuous + ATK.FinalRoot.pnp_depende_do_modelo" }

/-! ## Teoremas -/

theorem b1_verdadeiro : b1.valor = .verdadeiro := rfl
theorem b4_verdadeiro : b4.valor = .verdadeiro := rfl

theorem pontesNaoProvadas_nenhum :
    b2.valor = .nenhum ∧ b3.valor = .nenhum ∧ b5.valor = .nenhum ∧ b6.valor = .nenhum ∧
      b7.valor = .nenhum ∧ b8.valor = .nenhum :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem obrigacoesAbertas_nenhum :
    o1.valor = .nenhum ∧ o2.valor = .nenhum ∧ o3.valor = .nenhum ∧ o4.valor = .nenhum ∧
      o5.valor = .nenhum ∧ o6.valor = .nenhum ∧ o7.valor = .nenhum ∧ o8.valor = .nenhum :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem esquemaSemLigacao_ambos :
    esquemaNS_sem_ligacao.valor = .ambos ∧ esquemaPNP_sem_ligacao.valor = .ambos :=
  ⟨rfl, rfl⟩

/-!
Nesta auditoria item a item, `ambos` ocorre exatamente duas vezes, e só para a reivindicação
"o esquema paramétrico sem ligação fixada é significativo por si só" — nunca para `OPEN_MATH`
ou `CLOSED_MATH` como um todo, que permanecem conjunções majoritariamente `nenhum` (6 das 8
obrigações e 6 das 8 pontes) mais duas pontes `verdadeiro` (B1, B4). Atribuir `ambos` a
`OPEN_MATH`/`CLOSED_MATH` inteiros por decreto, sem esta auditoria item a item, não é algo que
este arquivo prove ou licencie.
-/

end ATK.AuditoriaBelnapReal

#print axioms ATK.AuditoriaBelnapReal.b1_verdadeiro
#print axioms ATK.AuditoriaBelnapReal.b4_verdadeiro
#print axioms ATK.AuditoriaBelnapReal.pontesNaoProvadas_nenhum
#print axioms ATK.AuditoriaBelnapReal.obrigacoesAbertas_nenhum
#print axioms ATK.AuditoriaBelnapReal.esquemaSemLigacao_ambos
