(* ATK–Closed Math: núcleo algébrico/geométrico em Coq (Rocq), verificado por coqc + coqchk.

   Espelha (em versão real/componente) os teoremas de ATK/ClosedMathCEZ.lean,
   ATK/ClosedMathCompleto.lean, ATK/ClosedMathToro.lean e ATK/RHTerminal.lean.
   Complexos são pares de reais; as identidades são provadas componente a componente.
   Único axioma: [classic] (lógica clássica), usado apenas na classificação exaustiva.
   Nada aqui afirma a Hipótese de Riemann. *)

Require Import Reals Lra Psatz Classical.
Open Scope R_scope.

(* ------------------------------------------------------------------ complexos *)
Record C := mkC { re : R; im : R }.
Definition Cadd (a b : C) := mkC (re a + re b) (im a + im b).
Definition Csub (a b : C) := mkC (re a - re b) (im a - im b).
Definition Cmul (a b : C) := mkC (re a * re b - im a * im b) (re a * im b + im a * re b).
Definition Cconj (a : C) := mkC (re a) (- im a).
Definition Cr (x : R) := mkC x 0.
Definition Ci := mkC 0 1.
Definition C0 := mkC 0 0.
Definition C1 := mkC 1 0.
Definition nsq (a : C) := re a * re a + im a * im a.

Lemma C_ext : forall a b : C, re a = re b -> im a = im b -> a = b.
Proof. intros [a1 a2] [b1 b2]; simpl; intros H1 H2; subst; reflexivity. Qed.

(* ------------------------------------------------------------------ 1. semântica *)
Definition Critico (F : C -> C) (s : C) := F s = C0 /\ re s = 1/2.
Definition Externo (F : C -> C) (s : C) := F s = C0 /\ re s <> 1/2.
Definition NaoZeroC (F : C -> C) (s : C) := F s <> C0 /\ re s = 1/2.
Definition NaoZeroE (F : C -> C) (s : C) := F s <> C0 /\ re s <> 1/2.

Theorem classificacao : forall F s,
  Critico F s \/ Externo F s \/ NaoZeroC F s \/ NaoZeroE F s.
Proof.
  intros F s; unfold Critico, Externo, NaoZeroC, NaoZeroE.
  destruct (classic (F s = C0)) as [Hz|Hz]; destruct (classic (re s = 1/2)) as [Hl|Hl]; tauto.
Qed.

Theorem exclusivos : forall F s,
  ~ (Critico F s /\ Externo F s) /\ ~ (Critico F s /\ NaoZeroC F s) /\
  ~ (Critico F s /\ NaoZeroE F s) /\ ~ (Externo F s /\ NaoZeroC F s) /\
  ~ (Externo F s /\ NaoZeroE F s) /\ ~ (NaoZeroC F s /\ NaoZeroE F s).
Proof. intros F s; unfold Critico, Externo, NaoZeroC, NaoZeroE; tauto. Qed.

(* ------------------------------------------------------------------ 2. verificador *)
Inductive Veredito := zero | naoZero | indeterminado.

Theorem checar_correto : forall x m r : R,
  Rabs (x - m) <= r -> r < Rabs m -> x <> 0.
Proof.
  intros x m r H1 H2 Hx; subst x.
  rewrite Rminus_0_l, Rabs_Ropp in H1; lra.
Qed.

Theorem zero_sempre_indeterminado : forall r : R, 0 <= r -> ~ (r < Rabs 0).
Proof. intros r Hr H; rewrite Rabs_R0 in H; lra. Qed.

(* ------------------------------------------------------------------ 3. operadores *)
Definition opJ := Cconj.
Definition opR (s : C) := Csub C1 (Cconj s).
Definition opS (s : C) := Csub C1 s.
Definition opT (s : C) := Cmul Ci (Cconj s).
Definition Dd (s : C) := re s - 1/2.

Lemma J_J : forall s, opJ (opJ s) = s.
Proof. intros [a b]; apply C_ext; simpl; ring. Qed.
Lemma R_R : forall s, opR (opR s) = s.
Proof. intros [a b]; apply C_ext; unfold opR, Csub, Cconj, C1; simpl; ring. Qed.
Lemma S_S : forall s, opS (opS s) = s.
Proof. intros [a b]; apply C_ext; unfold opS, Csub, C1; simpl; ring. Qed.
Lemma T_T : forall s, opT (opT s) = s.
Proof. intros [a b]; apply C_ext; unfold opT, Cmul, Cconj, Ci; simpl; ring. Qed.
Lemma R_J : forall s, opR (opJ s) = opS s.
Proof. intros [a b]; apply C_ext; unfold opR, opJ, opS, Csub, Cconj, C1; simpl; ring. Qed.
Lemma J_R : forall s, opJ (opR s) = opS s.
Proof. intros [a b]; apply C_ext; unfold opR, opJ, opS, Csub, Cconj, C1; simpl; ring. Qed.
Lemma R_S : forall s, opR (opS s) = opJ s.
Proof. intros [a b]; apply C_ext; unfold opR, opJ, opS, Csub, Cconj, C1; simpl; ring. Qed.
Lemma D_R : forall s, Dd (opR s) = - Dd s.
Proof. intros [a b]; unfold Dd, opR, Csub, Cconj, C1; simpl; ring. Qed.
Lemma TRT : forall w, opT (opR (opT w)) = Cadd (Cconj w) Ci.
Proof. intros [a b]; apply C_ext; unfold opT, opR, Cmul, Csub, Cconj, Cadd, Ci, C1; simpl; ring. Qed.
Lemma TRT_fixo : forall w, opT (opR (opT w)) = w <-> im w = 1/2.
Proof.
  intros [a b]; rewrite TRT; unfold Cadd, Cconj, Ci; simpl; split.
  - intro H; injection H; intros; lra.
  - intro H; apply C_ext; simpl; lra.
Qed.
Lemma T_isometria : forall s w, nsq (Csub (opT s) (opT w)) = nsq (Csub s w).
Proof. intros [a b] [c d]; unfold nsq, opT, Csub, Cmul, Cconj, Ci; simpl; ring. Qed.

(* par simétrico s± = 1/2 ± d + t i *)
Definition sp (d t : R) := mkC (1/2 + d) t.
Definition sm (d t : R) := mkC (1/2 - d) t.
Lemma T4_centro : forall d t, re (Cadd (sp d t) (sm d t)) / 2 = 1/2 /\ im (Cadd (sp d t) (sm d t)) / 2 = t.
Proof. intros; unfold Cadd, sp, sm; simpl; split; field. Qed.
Lemma T5_separacao : forall d t, nsq (Csub (sp d t) (sm d t)) = (2 * d) ^ 2.
Proof. intros; unfold nsq, Csub, sp, sm; simpl; ring. Qed.
Lemma T6_coincidencia : forall d t, sp d t = sm d t <-> d = 0.
Proof.
  intros d t; unfold sp, sm; split.
  - intro H; injection H; intros; lra.
  - intro H; subst d; apply C_ext; simpl; ring.
Qed.

(* ------------------------------------------------------------------ 4. modelo G *)
Definition sq (z : C) := Cmul z z.
Definition G (d g : R) (s : C) : C :=
  Cmul (Cadd (sq (Csub (Csub s (Cr (1/2))) (Cr d))) (Cr (g * g)))
       (Cadd (sq (Cadd (Csub s (Cr (1/2))) (Cr d))) (Cr (g * g))).

Definition xm (s : C) := Csub s (Cr (1/2)).
Ltac cring := apply C_ext; unfold G, xm, sq, Cmul, Cadd, Csub, Cconj, Cr, Ci, C0, C1, opS, opJ; simpl; ring.

Theorem P1 : forall d g,
  G d g (mkC (1/2 + d) g) = C0 /\ G d g (mkC (1/2 + d) (- g)) = C0 /\
  G d g (mkC (1/2 - d) g) = C0 /\ G d g (mkC (1/2 - d) (- g)) = C0.
Proof. intros d g; repeat split; cring. Qed.

Theorem G_R : forall d g s, G d g (opS s) = G d g s.
Proof. intros d g [a b]; cring. Qed.

Theorem G_conj : forall d g s, G d g (opJ s) = Cconj (G d g s).
Proof. intros d g [a b]; cring. Qed.

(* expansão quártica: G = x^4 + 2(g²−d²)x² + (g²+d²)², x = s − 1/2 *)
Theorem G_quartica : forall d g s,
  G d g s = Cadd (Cadd (sq (sq (xm s))) (Cmul (Cr (2 * (g * g - d * d))) (sq (xm s)))) (Cr ((g * g + d * d) ^ 2)).
Proof. intros d g [a b]; cring. Qed.

Theorem P2_critico : forall g, Critico (G 0 g) (mkC (1/2) g).
Proof.
  intro g; split.
  - replace (mkC (1/2) g) with (mkC (1/2 + 0) g) by (apply C_ext; simpl; ring).
    exact (proj1 (P1 0 g)).
  - simpl; reflexivity.
Qed.

Theorem P3_externo : forall d g, d <> 0 -> Externo (G d g) (mkC (1/2 + d) g).
Proof. intros d g Hd; split; [exact (proj1 (P1 d g)) | simpl; intro H; apply Hd; lra]. Qed.

Theorem P5_NE : forall d g, g <> 0 -> NaoZeroE (G d g) (Cr 2).
Proof.
  intros d g Hg; split.
  - intro H.
    assert (Hre : re (G d g (Cr 2)) = ((3/2 - d) ^ 2 + g * g) * ((3/2 + d) ^ 2 + g * g))
      by (unfold G, sq, Cmul, Cadd, Csub, Cr; simpl; field).
    rewrite H in Hre; simpl in Hre.
    assert (Hp : 0 < ((3/2 - d) ^ 2 + g * g) * ((3/2 + d) ^ 2 + g * g)).
    { apply Rmult_lt_0_compat; assert (0 < g * g) by (apply Rsqr_pos_lt; exact Hg); nra. }
    lra.
  - simpl; lra.
Qed.

Theorem P5_NC : forall d g, g <> 0 -> NaoZeroC (G d g) (Cr (1/2)).
Proof.
  intros d g Hg; split.
  - intro H.
    assert (Hre : re (G d g (Cr (1/2))) = (d * d + g * g) ^ 2)
      by (unfold G, sq, Cmul, Cadd, Csub, Cr; simpl; field).
    rewrite H in Hre; simpl in Hre.
    assert (0 < g * g) by (apply Rsqr_pos_lt; exact Hg).
    nra.
  - simpl; reflexivity.
Qed.

(* "ambos": o ramo ½ + λ + i g é zero de G_λ para todo λ; crítico em λ = 0, externo em λ = 1/4 *)
Theorem P4_ambos : forall g,
  (forall l, G l g (mkC (1/2 + l) g) = C0) /\ re (mkC (1/2 + 0) g) = 1/2 /\ re (mkC (1/2 + 1/4) g) = 3/4.
Proof. intro g; split; [intro l; exact (proj1 (P1 l g)) | simpl; split; field]. Qed.

(* as simetrias de ζ são compatíveis com as duas respostas *)
Theorem simetria_compativel_com_ambos :
  (forall s, G 0 1 (opS s) = G 0 1 s) /\ (forall s, G 1 1 (opS s) = G 1 1 s) /\
  Critico (G 0 1) (mkC (1/2) 1) /\ Externo (G 1 1) (mkC (1/2 + 1) 1).
Proof.
  split; [intro; apply G_R|]. split; [intro; apply G_R|].
  split; [apply P2_critico | apply P3_externo; apply R1_neq_R0].
Qed.

(* ------------------------------------------------------------------ 5. geometrias *)
Lemma den_ne : forall a b, 1 + a * a + b * b <> 0.
Proof. intros a b; apply Rgt_not_eq; nra. Qed.

Theorem P_esfera : forall a b,
  (2 * a / (1 + a * a + b * b)) ^ 2 + (2 * b / (1 + a * a + b * b)) ^ 2 +
  ((a * a + b * b - 1) / (1 + a * a + b * b)) ^ 2 = 1.
Proof. intros a b; field; apply den_ne. Qed.

Theorem Cil_par : forall d,
  cos (2 * PI * (1/2 + d)) = - cos (2 * PI * d) /\ sin (2 * PI * (1/2 + d)) = - sin (2 * PI * d) /\
  cos (2 * PI * (1/2 - d)) = - cos (2 * PI * d) /\ sin (2 * PI * (1/2 - d)) = sin (2 * PI * d).
Proof.
  intro d.
  replace (2 * PI * (1/2 + d)) with (2 * PI * d + PI) by field.
  replace (2 * PI * (1/2 - d)) with (PI - 2 * PI * d) by field.
  rewrite cos_plus, sin_plus, cos_minus, sin_minus, cos_PI, sin_PI.
  repeat split; ring.
Qed.

Theorem Cil_dist_par : forall d,
  (cos (2 * PI * (1/2 + d)) - cos (2 * PI * (1/2 - d))) ^ 2 +
  (sin (2 * PI * (1/2 + d)) - sin (2 * PI * (1/2 - d))) ^ 2 = (2 * sin (2 * PI * d)) ^ 2.
Proof. intro d; destruct (Cil_par d) as [H1 [H2 [H3 H4]]]; rewrite H1, H2, H3, H4; ring. Qed.

Theorem K_cone : forall delta th,
  (Rabs delta * cos th) ^ 2 + (Rabs delta * sin th) ^ 2 = delta ^ 2.
Proof.
  intros delta th.
  assert (H := sin2_cos2 th); unfold Rsqr in H.
  replace ((Rabs delta * cos th) ^ 2 + (Rabs delta * sin th) ^ 2)
    with (Rabs delta ^ 2 * (sin th * sin th + cos th * cos th)) by ring.
  rewrite H, pow2_abs; ring.
Qed.

Theorem K_vertice : forall th, Rabs 0 * cos th = 0 /\ Rabs 0 * sin th = 0.
Proof. intro th; rewrite Rabs_R0; split; ring. Qed.

Theorem Kt_injetiva : forall T d1 t1 d2 t2,
  (Rabs d1 * cos (2 * PI * t1 / T), Rabs d1 * sin (2 * PI * t1 / T), d1, t1) =
  (Rabs d2 * cos (2 * PI * t2 / T), Rabs d2 * sin (2 * PI * t2 / T), d2, t2) -> d1 = d2 /\ t1 = t2.
Proof. intros T d1 t1 d2 t2 H; injection H; intros; split; assumption. Qed.

(* toro: R age como z ↦ −z; linha crítica no equador interno; curvatura *)
Theorem tor_R : forall sigma,
  cos (2 * PI * (1 - sigma)) = cos (2 * PI * sigma) /\ sin (2 * PI * (1 - sigma)) = - sin (2 * PI * sigma).
Proof.
  intro sigma.
  replace (2 * PI * (1 - sigma)) with (2 * PI - 2 * PI * sigma) by ring.
  rewrite cos_minus, sin_minus, cos_2PI, sin_2PI; split; ring.
Qed.

Theorem tor_linha : forall R0 r, R0 + r * cos (2 * PI * (1/2)) = R0 - r /\ r * sin (2 * PI * (1/2)) = 0.
Proof.
  intros R0 r; replace (2 * PI * (1/2)) with PI by field.
  rewrite cos_PI, sin_PI; split; ring.
Qed.

Theorem tor_dist_par : forall r d,
  (r * sin (2 * PI * (1/2 + d)) - r * sin (2 * PI * (1/2 - d))) ^ 2 = (2 * r * sin (2 * PI * d)) ^ 2.
Proof. intros r d; destruct (Cil_par d) as [H1 [H2 [H3 H4]]]; rewrite H2, H4; ring. Qed.

Definition Kg (R0 r th : R) := cos th / (r * (R0 + r * cos th)).

Theorem curvatura_linha : forall R0 r, 0 < r -> r < R0 ->
  Kg R0 r PI = -1 / (r * (R0 - r)) /\ Kg R0 r PI < 0 /\ Kg R0 r 0 = 1 / (r * (R0 + r)).
Proof.
  intros R0 r Hr HR; unfold Kg; rewrite cos_PI, cos_0.
  replace (R0 + r * -1) with (R0 - r) by ring.
  replace (R0 + r * 1) with (R0 + r) by ring.
  split; [reflexivity | split; [| reflexivity]].
  assert (H : 0 < / (r * (R0 - r))) by (apply Rinv_0_lt_compat; nra).
  unfold Rdiv; lra.
Qed.

(* ------------------------------------------------------------------ 6. taxonomia *)
Theorem P_posneg : forall a b z : R, (z * z - a * a) * (z * z + b * b) = (z - a) * (z + a) * (z * z + b * b).
Proof. intros; ring. Qed.

Theorem truncamento_033 : 33 / 100 - 1 / 3 = - 1 / 300.
Proof. field. Qed.

Theorem zero_sobre_zero_convencao : forall x : R, x <> 1 -> (x * x - 1) / (x - 1) = x + 1.
Proof. intros x Hx; field; lra. Qed.

(* ------------------------------------------------------------------ 7. pontes e terminal *)
Definition TransporteZero (F G0 phi u : R -> R) := forall s, G0 (phi s) = u s * F s.

Theorem transporte_zero : forall F G0 phi u s, TransporteZero F G0 phi u -> F s = 0 -> G0 (phi s) = 0.
Proof. intros F G0 phi u s H Hz; unfold TransporteZero in H; rewrite H, Hz; ring. Qed.

Theorem transporte_zero_iff : forall F G0 phi u s,
  TransporteZero F G0 phi u -> u s <> 0 -> (F s = 0 <-> G0 (phi s) = 0).
Proof.
  intros F G0 phi u s H Hu; split.
  - apply transporte_zero; assumption.
  - intro Hz; unfold TransporteZero in H; rewrite H in Hz; destruct (Rmult_integral _ _ Hz) as [H1|H1]; [contradiction | exact H1].
Qed.

(* T28: |F − P| ≤ E < L ≤ |P| em K ⇒ F ≠ 0 em K *)
Theorem criterio_aproximacao : forall (F P : R -> R) (K : R -> Prop) (E L : R),
  (forall s, K s -> Rabs (F s - P s) <= E) -> (forall s, K s -> L <= Rabs (P s)) -> E < L ->
  forall s, K s -> F s <> 0.
Proof.
  intros F P K E L HE HL HEL s Hs Hz.
  specialize (HE s Hs); specialize (HL s Hs).
  rewrite Hz, Rminus_0_l, Rabs_Ropp in HE; lra.
Qed.

(* cobertura: se cada K_n (cobrindo S) não tem zeros, S não tem zeros *)
Theorem cobertura_exclui : forall (F : R -> R) (S : R -> Prop) (K : nat -> R -> Prop),
  (forall s, S s -> exists n, K n s) -> (forall n s, K n s -> F s <> 0) -> forall s, S s -> F s <> 0.
Proof. intros F S K Hcov HK s Hs; destruct (Hcov s Hs) as [n Hn]; exact (HK n s Hn). Qed.

(* ------------------------------------------------------------------ 8. tempos verbais *)
Inductive Tempo := perfeito | negado | condicional | futuro | presente.

Definition Exige (t : Tempo) (p h : Prop) : Prop :=
  match t with
  | perfeito => p
  | negado => ~ p
  | condicional => h -> p
  | futuro => True
  | presente => True
  end.

Record Afirmacao := { enunciado : Prop; tempo : Tempo; hipotese : Prop; testemunha : Exige tempo enunciado hipotese }.

Theorem perfeito_verdadeiro : forall a, tempo a = perfeito -> enunciado a.
Proof. intros [p t h w] Ht; simpl in *; subst t; exact w. Qed.

Theorem negado_falso : forall a, tempo a = negado -> ~ enunciado a.
Proof. intros [p t h w] Ht; simpl in *; subst t; exact w. Qed.

Theorem futuro_vazio : forall P : Prop, exists a b : Afirmacao,
  enunciado a = P /\ enunciado b = (~ P) /\ tempo a = futuro /\ tempo b = futuro.
Proof.
  intro P.
  exists (Build_Afirmacao P futuro True I), (Build_Afirmacao (~ P) futuro True I).
  repeat split.
Qed.

Definition a_classificacao : Afirmacao :=
  Build_Afirmacao (forall F s, Critico F s \/ Externo F s \/ NaoZeroC F s \/ NaoZeroE F s)
    perfeito True classificacao.

(* ------------------------------------------------------------------ auditoria *)
Print Assumptions classificacao.
Print Assumptions P1.
Print Assumptions G_quartica.
Print Assumptions P5_NE.
Print Assumptions curvatura_linha.
Print Assumptions criterio_aproximacao.
Print Assumptions perfeito_verdadeiro.
