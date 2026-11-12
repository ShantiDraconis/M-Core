import Mathlib

/-!
# Auditor de enunciados

`#auditar_prefixo P` examina cada teorema dos módulos cujo nome começa por `P` e imprime uma linha por teorema:

```
AUDITORIA	<nome>	<módulo>	<linha>	<classe>=<detalhe>;…
```

Classes (`hipoteses_contraditorias`, `falso`, `falso_por_contraexemplo` e `trivial` são **certificadas**: o termo que a tática produziu foi
passou no kernel como teorema auxiliar):

* `hipoteses_contraditorias=<tática>`: das hipóteses sai `False` (o enunciado é vazio);
* `conclusao_vazia`: a conclusão, depois de desdobrar definições, é `True` ou `∃ _, True`;
* `falso=<tática>`: a negação do enunciado (sem variáveis livres) foi provada;
* `falso_por_contraexemplo=<valores>`: variáveis em ℕ ou ℤ com valores pequenos em que as hipóteses valem e a
  conclusão não; a negação é provada por `decide` nesses valores;
* `trivial=<tática>`: o enunciado inteiro fecha com uma única tática padrão (informativo: compara-se com o
  enunciado informal para ver se a formalização perdeu a dificuldade);
* `axioma_extra=<nomes>`: depende de axiomas fora de `propext`, `Classical.choice`, `Quot.sound`, `sorryAx`;
* riscos de codificação (não são defeitos; contam como no artigo *Faults in Our Formal Benchmarking*):
  `divisao_por_zero_nao_excluida` (denominador em ℝ, ℚ ou ℂ cujo `≠ 0` não sai das hipóteses),
  `funcao_totalizada=<nome>` (`Real.sqrt` sem `0 ≤ x`, `Real.log` sem `0 < x` deriváveis das hipóteses),
  `divisao_inteira` e `subtracao_em_N` (truncamento em ℕ e ℤ).

Cada tentativa tem um teto de heartbeats e não altera o estado. O `plausible` (contraexemplo por amostragem)
fica fora deste passo: ele executa o enunciado e pode derrubar o processo (por exemplo, um fatorial enorme).
-/

open Lean Meta Elab Command

namespace AuditorEnunciados

def permitidos : List Name := [``propext, ``Classical.choice, ``Quot.sound, ``sorryAx]

/-- Roda `x` com teto de `n` heartbeats (na unidade de `set_option maxHeartbeats`), sem deixar rastro no estado; falha (inclusive por tempo) vira `none`. -/
def tentar (n : Nat) (x : MetaM α) : MetaM (Option α) := do
  let s ← saveState
  let r ← tryCatchRuntimeEx
    (withTheReader Core.Context (fun c => { c with maxHeartbeats := n * 1000 }) do
      withCurrHeartbeats do
        let v ← x
        pure (some v))
    (fun _ => pure none)
  s.restore
  return r

/-- A tática fecha o alvo fechado `g` (sem variáveis livres), e o termo passa no kernel como teorema auxiliar
(`addDecl`, depois desfeito com o resto do estado). Níveis de universo que ficaram livres no termo valem 0. -/
def fecha (g : Expr) (tac : Syntax) (lps : List Name) (n : Nat := 50000) : MetaM Bool := do
  let r ← tentar n do
    let alvo ← mkFreshExprMVar g
    let (gs, _) ← Lean.Elab.runTactic alvo.mvarId! tac
    unless gs.isEmpty do throwError "sobrou alvo"
    let v ← instantiateMVars alvo
    if v.hasSorry || v.hasSyntheticSorry || v.hasExprMVar then throwError "incompleto"
    for m in (collectLevelMVars {} v).result do assignLevelMVar m levelZero
    let v ← instantiateMVars v
    addDecl (.thmDecl { name := `_auditor_certificado, levelParams := lps, type := g, value := v })
    pure ()
  return r.isSome

partial def conclusaoVazia (e : Expr) : MetaM Bool := do
  let e ← whnf e
  if ← isDefEq e (mkConst ``True) then return true
  if e.isAppOfArity ``Exists 2 then
    let p := e.appArg!
    if p.isLambda then
      return ← lambdaTelescope p fun _ b => conclusaoVazia b
  return false

def taticasFalse : MetaM (List (String × Syntax)) := do
  return [("contradiction", ← `(tactic| (intros; contradiction))), ("simp_all", ← `(tactic| (intros; simp_all))),
    ("omega", ← `(tactic| (intros; omega))), ("linarith", ← `(tactic| (intros; linarith))),
    ("linarith", ← `(tactic| (intros; casesm* _ ∧ _; linarith))),
    ("norm_num", ← `(tactic| (intros; norm_num at *)))]

def taticasTriviais : MetaM (List (String × Syntax)) := do
  return [("rfl", ← `(tactic| (intros; rfl))),
    ("norm_num", ← `(tactic| (intros; norm_num))), ("simp", ← `(tactic| (intros; simp))),
    ("omega", ← `(tactic| (intros; omega))), ("linarith", ← `(tactic| (intros; linarith))),
    ("positivity", ← `(tactic| (intros; positivity)))]

def taticasNegacao : MetaM (List (String × Syntax)) := do
  return [("norm_num", ← `(tactic| norm_num)), ("simp", ← `(tactic| simp))]

def hipotesesContraditorias (tipo : Expr) (lps : List Name) : MetaM (Option String) := do
  -- o alvo `∀ xs, False` é montado no telescópio, mas a tática roda fora dele, para não usar as variáveis
  -- livres do telescópio no lugar das que o `intros` introduz
  let some g ← forallTelescope tipo fun xs _ => do
      let mut temHip := false
      for x in xs do
        if ← isProp (← inferType x) then temHip := true
      if !temHip then return none
      return some (← mkForallFVars xs (mkConst ``False))
    | return none
  for (nome, tac) in ← taticasFalse do
    if ← fecha g tac lps then return some nome
  return none

def trivial (tipo : Expr) (lps : List Name) : MetaM (Option String) := do
  for (nome, tac) in ← taticasTriviais do
    if ← fecha tipo tac lps then return some nome
  return none

def falso (tipo : Expr) (lps : List Name) : MetaM (Option String) := do
  if tipo.hasLooseBVars || (← isProp tipo) == false then return none
  -- só enunciados sem variáveis livres no topo (sem ∀ de dados): a negação é uma proposição fechada
  if tipo.isForall then return none
  for (nome, tac) in ← taticasNegacao do
    if ← fecha (mkNot tipo) tac lps then return some nome
  return none

/-- Valores de teste para variáveis em ℕ e ℤ (as primeiras `k` de cada lista quando há três variáveis). -/
def valoresNat : List Nat := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def valoresInt : List Int := [0, 1, -1, 2, -2, 3, -3, 4, 5, 6, -4, 7, 10]

def numeral (t : Expr) (k : Nat) : MetaM (TSyntax `term) := do
  if t.isConstOf ``Nat then
    return ⟨Syntax.mkNumLit (toString (valoresNat[k]!))⟩
  let v := valoresInt[k]!
  if v < 0 then
    let n : TSyntax `num := Syntax.mkNumLit (toString v.natAbs)
    `(-$n)
  else return ⟨Syntax.mkNumLit (toString v)⟩

/-- Contraexemplo certificado: o enunciado tem só variáveis explícitas em ℕ ou ℤ (até três) seguidas de hipóteses;
procura valores pequenos em que as hipóteses valem e a conclusão não, e prova `¬ enunciado` com `decide` no termo
`absurd (h a b …) (by decide)`, conferido no kernel. -/
def testemunha (tipo : Expr) (lps : List Name) : MetaM (Option String) := do
  let tipos? ← forallTelescope tipo fun xs _ => do
    let mut dados : Array Expr := #[]
    let mut emHipoteses := false
    for x in xs do
      let t ← inferType x
      if ← isProp t then
        emHipoteses := true
      else
        if emHipoteses then return none
        if !(t.isConstOf ``Nat || t.isConstOf ``Int) then return none
        if (← x.fvarId!.getBinderInfo) != .default then return none
        dados := dados.push t
    if dados.isEmpty || dados.size > 3 then return none
    return some dados
  let some tipos := tipos? | return none
  let n := if tipos.size == 3 then 6 else valoresNat.length
  let mut combos : List (List Nat) := [[]]
  for _ in tipos do
    combos := combos.flatMap fun c => (List.range n).map fun k => c ++ [k]
  for c in combos do
    let args ← (tipos.toList.zip c).mapM fun (t, k) => numeral t k
    let tac ← `(tactic| (intro h; exact absurd (h $(args.toArray)*) (by decide)))
    if ← fecha (mkNot tipo) tac lps 4000 then
      let vals := (tipos.toList.zip c).map fun (t, k) =>
        if t.isConstOf ``Nat then toString (valoresNat[k]!) else toString (valoresInt[k]!)
      return some (String.intercalate "," vals)
  return none

/-- Todos os subtermos de `e` (sem entrar em tipos de binders implícitos de instância). -/
partial def subtermos (e : Expr) (acc : Array Expr := #[]) : Array Expr :=
  let acc := acc.push e
  match e with
  | .app f a => subtermos a (subtermos f acc)
  | .lam _ t b _ | .forallE _ t b _ => subtermos b (subtermos t acc)
  | .letE _ t v b _ => subtermos b (subtermos v (subtermos t acc))
  | .mdata _ b => subtermos b acc
  | .proj _ _ b => subtermos b acc
  | _ => acc

def taticasCondicao : MetaM (List Syntax) := do
  return [← `(tactic| (intros; positivity)), ← `(tactic| (intros; casesm* _ ∧ _; positivity)),
    ← `(tactic| (intros; norm_num)),
    ← `(tactic| (intros; first | linarith | (intro h; linarith))), ← `(tactic| (intros; simp_all))]

/-- Condições laterais (`b ≠ 0`, `0 ≤ x`, `0 < x`) montadas no telescópio do enunciado; um risco só conta se a
condição **não** sair das hipóteses por uma das táticas acima (provas conferidas no kernel). -/
def riscos (tipo : Expr) (lps : List Name) : MetaM (List String) := do
  let cands : Array (String × Option Expr) ← forallTelescope tipo fun xs concl => do
    let hips ← xs.filterMapM fun x => do
      let t ← inferType x
      if ← isProp t then return some t else return none
    let mut out : Array (String × Option Expr) := #[]
    for e in #[concl] ++ hips do
      for sub in subtermos e do
        if sub.isAppOfArity ``HDiv.hDiv 6 then
          let α := sub.getArg! 0
          let b := sub.getArg! 5
          if α.isConstOf ``Nat || α.isConstOf ``Int then
            out := out.push ("divisao_inteira", none)
          else if (α.isConstOf ``Real || α.isConstOf ``Rat || α.isConstOf ``Complex) &&
              !b.isAppOfArity ``OfNat.ofNat 3 then
            if b.hasLooseBVars then
              out := out.push ("divisao_por_zero_nao_excluida", none)
            else
              let c ← mkAppM ``Ne #[b, ← mkNumeral α 0]
              out := out.push ("divisao_por_zero_nao_excluida", some (← mkForallFVars xs c))
        else if sub.isAppOfArity ``HSub.hSub 6 && (sub.getArg! 0).isConstOf ``Nat then
          out := out.push ("subtracao_em_N", none)
        else if let .const n _ := sub.getAppFn then
          if sub.getAppNumArgs == 1 && (n == ``Real.sqrt || n == ``Real.log) then
            let x := sub.getArg! 0
            let nome := s!"funcao_totalizada={n}"
            if x.hasLooseBVars then
              out := out.push (nome, none)
            else
              let zero ← mkNumeral (mkConst ``Real) 0
              let c ← if n == ``Real.sqrt then mkAppM ``LE.le #[zero, x] else mkAppM ``LT.lt #[zero, x]
              out := out.push (nome, some (← mkForallFVars xs c))
    return out
  let mut res : List String := []
  for (nome, cond?) in cands do
    if res.contains nome then continue
    match cond? with
    | none => res := res ++ [nome]
    | some g =>
      let mut ok := false
      for tac in ← taticasCondicao do
        if ← fecha g tac lps 20000 then
          ok := true
          break
      unless ok do res := res ++ [nome]
  return res

def auditar (n : Name) (tipo : Expr) (lps : List Name) : MetaM String := do
  let mut achados : List String := []
  let axs ← collectAxioms n
  let extras := axs.toList.filter (fun a => !permitidos.contains a)
  unless extras.isEmpty do achados := achados ++ [s!"axioma_extra={extras}"]
  if let some t ← hipotesesContraditorias tipo lps then achados := achados ++ [s!"hipoteses_contraditorias={t}"]
  if ← forallTelescope tipo fun _ c => conclusaoVazia c then achados := achados ++ ["conclusao_vazia"]
  if let some t ← falso tipo lps then achados := achados ++ [s!"falso={t}"]
  else if let some v ← testemunha tipo lps then achados := achados ++ [s!"falso_por_contraexemplo={v}"]
  if let some t ← trivial tipo lps then achados := achados ++ [s!"trivial={t}"]
  achados := achados ++ (← riscos tipo lps)
  return String.intercalate ";" achados

elab "#auditar_prefixo " p:ident : command => do
  let env ← getEnv
  let pref := p.getId
  let mut alvos : Array (Name × Name) := #[]
  for (n, c) in env.constants.map₁.toList do
    if let .thmInfo _ := c then
      if n.isInternal then continue
      let some idx := env.getModuleIdxFor? n | continue
      let m := env.header.moduleNames[idx.toNat]!
      if pref.isPrefixOf m then alvos := alvos.push (n, m)
  for (n, m) in alvos.qsort (fun a b => a.1.toString < b.1.toString) do
    let some c := env.find? n | continue
    let linha : Nat := match ← findDeclarationRanges? n with
      | some r => r.range.pos.line
      | none => 0
    let v ← liftTermElabM <| auditar n c.type c.levelParams
    logInfo m!"AUDITORIA\t{n}\t{m}\t{linha}\t{v}"

end AuditorEnunciados
