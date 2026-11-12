import Lean

/-!
# Verificador de referência para o teste do portão

`#auditar` examina cada teorema declarado no arquivo corrente e imprime uma linha
`AUDITORIA <nome>: <veredito>`. O veredito junta três testes, todos no kernel ou no elaborador,
nenhum sobre o texto da fonte:

* **axiomas**: `collectAxioms` fora de `propext`, `Classical.choice`, `Quot.sound` (pega `sorryAx`,
  axiomas próprios em qualquer forma de declaração e `Lean.ofReduceBool` do `native_decide`);
* **vazio**: a conclusão, depois de abrir os `∀` e desdobrar definições (`whnf`), é `True` ou `∃ _, True`;
* **hipóteses contraditórias**: das hipóteses do enunciado sai `False` por
  `contradiction`, `simp_all`, `omega` ou `decide`.

O terceiro teste é heurístico: só acha contradições que essas táticas achem.
-/

open Lean Meta Elab Command

namespace Auditoria

def permitidos : List Name := [``propext, ``Classical.choice, ``Quot.sound]

/-- A conclusão desdobra para `True` ou `∃ _, True`. -/
partial def conclusaoVazia (e : Expr) : MetaM Bool := do
  let e ← whnf e
  if ← isDefEq e (mkConst ``True) then return true
  if e.isAppOfArity ``Exists 2 then
    let p := e.appArg!
    if p.isLambda then
      return ← lambdaTelescope p fun _ b => conclusaoVazia b
  return false

/-- Das hipóteses sai `False` por uma tática padrão. -/
def hipotesesContraditorias (tipo : Expr) : MetaM Bool := do
  forallTelescope tipo fun xs _ => do
    let mut temHipotese := false
    for x in xs do
      if ← isProp (← inferType x) then temHipotese := true
    if !temHipotese then return false
    let alvo ← mkFreshExprMVar (mkConst ``False)
    let tac ← `(tactic| first | contradiction | simp_all | omega | decide)
    try
      let (gs, _) ← Lean.Elab.runTactic alvo.mvarId! tac
      return gs.isEmpty
    catch _ => return false

def auditar (n : Name) (tipo : Expr) : MetaM String := do
  let axs ← collectAxioms n
  let extras := axs.toList.filter (fun a => !permitidos.contains a)
  let mut achados : List String := []
  unless extras.isEmpty do achados := achados ++ [s!"axiomas {extras}"]
  if ← forallTelescope tipo fun _ c => conclusaoVazia c then achados := achados ++ ["vazio"]
  if ← hipotesesContraditorias tipo then achados := achados ++ ["hipoteses contraditorias"]
  return if achados.isEmpty then "OK" else String.intercalate ", " achados

elab "#auditar" : command => do
  let env ← getEnv
  let nomes := env.constants.map₂.foldl (init := #[]) fun acc n c =>
    match c with
    | .thmInfo _ => if n.isInternal then acc else acc.push n
    | _ => acc
  for n in nomes.qsort (·.toString < ·.toString) do
    let some c := env.find? n | continue
    let v ← liftTermElabM <| auditar n c.type
    logInfo m!"AUDITORIA {n}: {v}"

end Auditoria
