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

(* fechamento robusto para igualdades reais: tenta ring/lra/nra/field, com e sem simplificação *)
Ltac fecha := first [ ring | lra | nra | field | (simpl; ring) | (simpl; lra) | (cbn; ring)
                    | (cbn; lra) | (simpl; field) | (simpl; nra) ].

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
Proof. intros [a b]; unfold Dd, opR, Csub, Cconj, C1; fecha. Qed.
Lemma TRT : forall w, opT (opR (opT w)) = Cadd (Cconj w) Ci.
Proof. intros [a b]; apply C_ext; unfold opT, opR, Cmul, Csub, Cconj, Cadd, Ci, C1; simpl; ring. Qed.
Lemma TRT_fixo : forall w, opT (opR (opT w)) = w <-> im w = 1/2.
Proof.
  intros [a b]; rewrite TRT; unfold Cadd, Cconj, Ci; simpl; split.
  - intro H; injection H; intros; lra.
  - intro H; apply C_ext; simpl; lra.
Qed.
Lemma T_isometria : forall s w, nsq (Csub (opT s) (opT w)) = nsq (Csub s w).
Proof. intros [a b] [c d]; unfold nsq, opT, Csub, Cmul, Cconj, Ci; fecha. Qed.

(* par simétrico s± = 1/2 ± d + t i *)
Definition sp (d t : R) := mkC (1/2 + d) t.
Definition sm (d t : R) := mkC (1/2 - d) t.
Lemma T4_centro : forall d t, re (Cadd (sp d t) (sm d t)) / 2 = 1/2 /\ im (Cadd (sp d t) (sm d t)) / 2 = t.
Proof. intros; unfold Cadd, sp, sm; split; fecha. Qed.
Lemma T5_separacao : forall d t, nsq (Csub (sp d t) (sm d t)) = (2 * d) ^ 2.
Proof. intros; unfold nsq, Csub, sp, sm; fecha. Qed.
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
Ltac cring := apply C_ext; unfold G, xm, sq, Cmul, Cadd, Csub, Cconj, Cr, Ci, C0, C1, opS, opJ; fecha.

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
    assert (Hre : re (G d g (Cr 2)) = ((3/2 - d) * (3/2 - d) + g * g) * ((3/2 + d) * (3/2 + d) + g * g))
      by (unfold G, sq, Cmul, Cadd, Csub, Cr; fecha).
    rewrite H in Hre; simpl in Hre.
    assert (H0 : 0 < g * g) by (apply Rsqr_pos_lt; exact Hg).
    assert (Hp : 0 < ((3/2 - d) * (3/2 - d) + g * g) * ((3/2 + d) * (3/2 + d) + g * g)).
    { apply Rmult_lt_0_compat; apply Rplus_le_lt_0_compat; try exact H0; apply Rle_0_sqr. }
    lra.
  - simpl; lra.
Qed.

Theorem P5_NC : forall d g, g <> 0 -> NaoZeroC (G d g) (Cr (1/2)).
Proof.
  intros d g Hg; split.
  - intro H.
    assert (Hre : re (G d g (Cr (1/2))) = (d * d + g * g) * (d * d + g * g))
      by (unfold G, sq, Cmul, Cadd, Csub, Cr; fecha).
    rewrite H in Hre; simpl in Hre.
    assert (H0 : 0 < g * g) by (apply Rsqr_pos_lt; exact Hg).
    assert (Hp : 0 < (d * d + g * g) * (d * d + g * g)).
    { apply Rmult_lt_0_compat; apply Rplus_le_lt_0_compat; try exact H0; apply Rle_0_sqr. }
    lra.
  - simpl; reflexivity.
Qed.

(* "ambos": o ramo ½ + λ + i g é zero de G_λ para todo λ; crítico em λ = 0, externo em λ = 1/4 *)
Theorem P4_ambos : forall g,
  (forall l, G l g (mkC (1/2 + l) g) = C0) /\ re (mkC (1/2 + 0) g) = 1/2 /\ re (mkC (1/2 + 1/4) g) = 3/4.
Proof. intro g; split; [intro l; exact (proj1 (P1 l g)) | simpl; split; fecha]. Qed.

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
Proof. intros a b; apply Rgt_not_eq; pose proof (Rle_0_sqr a); pose proof (Rle_0_sqr b); unfold Rsqr in *; lra. Qed.

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
  assert (H : 0 < / (r * (R0 - r))) by (apply Rinv_0_lt_compat; apply Rmult_lt_0_compat; lra).
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
  - exact (transporte_zero F G0 phi u s H).
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

(* ------------------------------------------------------------------ Jensen / Turán / Toeplitz *)
(* Espelha ATK/JensenTuran.lean na parte algébrica. *)

Definition disc3 (a b c d : R) :=
  b^2*c^2 - 4*a*c^3 - 4*b^3*d - 27*a^2*d^2 + 18*a*b*c*d.

Theorem disc3_raizes : forall A r1 r2 r3,
  disc3 A (-A*(r1+r2+r3)) (A*(r1*r2+r1*r3+r2*r3)) (-A*r1*r2*r3) =
  A^4*((r1-r2)*(r1-r3)*(r2-r3))^2.
Proof. intros; unfold disc3; ring. Qed.

Theorem disc3_jensen : forall g0 g1 g2 g3,
  disc3 g3 (3*g2) (3*g1) g0 = 27*(4*(g1^2-g0*g2)*(g2^2-g1*g3) - (g1*g2-g0*g3)^2).
Proof. intros; unfold disc3; ring. Qed.

Theorem turan3 : forall g0 g1 g2 g3 r1 r2 r3,
  3*g2 = -g3*(r1+r2+r3) -> 3*g1 = g3*(r1*r2+r1*r3+r2*r3) -> g0 = -g3*r1*r2*r3 ->
  (g1*g2-g0*g3)^2 <= 4*(g1^2-g0*g2)*(g2^2-g1*g3).
Proof.
  intros g0 g1 g2 g3 r1 r2 r3 HB HC HD.
  assert (E : disc3 g3 (3*g2) (3*g1) g0 = g3^4*((r1-r2)*(r1-r3)*(r2-r3))^2).
  { rewrite HB, HC, HD. apply disc3_raizes. }
  rewrite disc3_jensen in E.
  assert (P : 0 <= g3^4*((r1-r2)*(r1-r3)*(r2-r3))^2).
  { apply Rmult_le_pos.
    - replace (g3^4) with ((g3^2)^2) by ring. apply pow2_ge_0.
    - apply pow2_ge_0. }
  lra.
Qed.

(* Jensen de grau 2: g2 z^2 + 2 g1 z + g0 com z = x + i y; partes real e imaginária. *)
Theorem jensen_grau2 : forall g0 g1 g2 x y, g2 <> 0 ->
  g2*(x^2 - y^2) + 2*g1*x + g0 = 0 -> y*(2*(g2*x + g1)) = 0 ->
  g0*g2 <= g1^2 -> y = 0.
Proof.
  intros g0 g1 g2 x y H2 Hre Him Hd.
  destruct (Req_dec y 0) as [Hy|Hy]; [exact Hy|].
  assert (Hx : g2*x + g1 = 0).
  { destruct (Rmult_integral _ _ Him) as [H|H]; [contradiction | lra]. }
  assert (K : (g2*g2)*(y*y) = g0*g2 - g1^2).
  { assert (Hx' : g2*x = -g1) by lra.
    replace ((g2*g2)*(y*y)) with
      ((g2*x)*(g2*x) + 2*g1*(g2*x) + g0*g2 - g2*(g2*(x^2 - y^2) + 2*g1*x + g0)) by ring.
    rewrite Hre, Hx'. ring. }
  assert (P1 : 0 < g2*g2) by (apply Rsqr_pos_lt; exact H2).
  assert (P2 : 0 < y*y) by (apply Rsqr_pos_lt; exact Hy).
  assert (P : 0 < (g2*g2)*(y*y)) by (apply Rmult_lt_0_compat; assumption).
  exfalso. lra.
Qed.

(* Normalização de Jensen: gamma_n = n! a_n; f = k!. *)
Theorem turan_normalizacao_id : forall k f a0 a1 a2,
  ((k+1)*f*a1)^2 - (f*a0)*((k+2)*(k+1)*f*a2) = ((k+1)*f^2)*((k+1)*a1^2 - (k+2)*a0*a2).
Proof. intros; ring. Qed.

(* Menor de Toeplitz D_{3,1} = det [[g1,g0,0],[g2,g1,g0],[g3,g2,g1]]. *)
Definition D31 (g0 g1 g2 g3 : R) := g1^3 - 2*g0*g1*g2 + g0^2*g3.

Theorem D31_cofator : forall g0 g1 g2 g3,
  g1*(g1*g1 - g0*g2) - g0*(g2*g1 - g0*g3) + 0*(g2*g2 - g1*g3) = D31 g0 g1 g2 g3.
Proof. intros; unfold D31; ring. Qed.

(* (1+X)^3: a = (1,3,3,1) tem D31 = 10; gamma = n! a = (1,3,6,6) tem D31 = -3. *)
Theorem tp_a_nao_passa_gamma : D31 1 3 3 1 = 10 /\ D31 1 3 6 6 = -3.
Proof. unfold D31; split; ring. Qed.

(* Momentos: gamma_n = C q^n n! M_n/(2n)!, A = 2n+1, B = 2n+3  ==>  Turan <-> A M0 M2 <= B M1^2. *)
Theorem turan_momentos_id : forall c q A B M0 M1 M2, 0 < A -> 0 < B ->
  (c*(q/(2*A))*M1)^2 - (c*M0)*(c*(q^2/(4*A*B))*M2) =
  (c^2*q^2/(4*A^2*B)) * (B*M1^2 - A*(M0*M2)).
Proof.
  intros c q A B M0 M1 M2 HA HB.
  field; repeat split; apply Rgt_not_eq; assumption.
Qed.

(* Log-convexidade (Cauchy–Schwarz) não implica Turán: M = (1, 1, 4) (medida 3/4 d0 + 1/4 d2). *)
Theorem cs_nao_implica_turan : 1^2 <= 1*4 /\ ~ (1*(1*4) <= 3*1^2).
Proof. split; lra. Qed.

(* ------------------------------------------------------------------ pendentes formalizados (rodada 6) *)
(* K6: v^T L v = soma dos quadrados das diferencas, L = 6I - J (ATK.GeometriaExtra.forma_L6). *)
Theorem forma_L6 : forall a b c d e f : R,
  a*(6*a-(a+b+c+d+e+f)) + b*(6*b-(a+b+c+d+e+f)) + c*(6*c-(a+b+c+d+e+f)) +
  d*(6*d-(a+b+c+d+e+f)) + e*(6*e-(a+b+c+d+e+f)) + f*(6*f-(a+b+c+d+e+f)) =
  (a-b)^2+(a-c)^2+(a-d)^2+(a-e)^2+(a-f)^2+(b-c)^2+(b-d)^2+(b-e)^2+(b-f)^2+
  (c-d)^2+(c-e)^2+(c-f)^2+(d-e)^2+(d-f)^2+(e-f)^2.
Proof. intros; ring. Qed.

(* gamma = (1,2,4): J_{3,0} = 1 + 6X + 12X^2 nao tem raiz real (jensen_gamma_detecta). *)
Theorem jensen_gamma_detecta : forall x : R, 1 + 6*x + 12*x^2 <> 0.
Proof.
  intros x H.
  assert (E : 1 + 6*x + 12*x^2 = 3/4*(4*x+1)^2 + 1/4) by field.
  assert (P : 0 <= (4*x+1)^2) by apply pow2_ge_0.
  lra.
Qed.

(* a = (1,2,2): discriminante de 1 + 2N X + N(N-1) X^2 e 4N (jensen_a_hiperbolico). *)
Theorem jensen_a_disc : forall N : R, (2*N)^2 - 4*(N*(N-1))*1 = 4*N.
Proof. intros; ring. Qed.

(* Rotacao preserva d^2 + t^2 (rotacao). *)
Theorem rotacao : forall d t c s : R, c^2 + s^2 = 1 ->
  (d*c - t*s)^2 + (d*s + t*c)^2 = d^2 + t^2.
Proof.
  intros d t c s H.
  replace ((d*c - t*s)^2 + (d*s + t*c)^2) with ((d^2 + t^2)*(c^2 + s^2)) by ring.
  rewrite H; ring.
Qed.

(* Barreira: a = b + t (normSq_eq_add). *)
Theorem barreira_a_b_t : forall be ga : R,
  be^2 + ga^2 = ((1-be)^2 + ga^2) + (2*be - 1).
Proof. intros; ring. Qed.

(* Ajuste de dois pontos: intercepto negativo (ajuste_negativo), dados os limites de log 2 e log 5 - log 4. *)
Theorem ajuste_intercepto : forall l2 l5 : R,
  6931471803/10000000000 < l2 -> l2 < 6931471808/10000000000 ->
  2231435/10000000 < l5 - 2*l2 -> l5 - 2*l2 < 2231436/10000000 ->
  50691202/10000000000 * (6*l2 + 3*l5) < 82337162772/10000000000000 * (8*l2) /\
  50691202/10000000000 * (6*l2 + 3*l5) - 82337162772/10000000000000 * (8*l2) <
    - 290/10000000 * ((6*l2 + 3*l5) - 8*l2).
Proof. intros; split; lra. Qed.

(* Integral por pedacos: o coeficiente (p/i + q/j) do texto daria valor negativo (contraexemplo_pedaco). *)
Theorem contraexemplo_pedaco : forall L : R,
  4054651081081/10000000000000 < L -> L < 4054651081082/10000000000000 ->
  0 < 1/2 - 2*L + 1/3 /\ 1/2 - (2/1 + 1/2)*L + 1/3 < 0.
Proof. intros; split; lra. Qed.

(* ---------------------------------------------- erros corrigidos (rodada 7, ATK/Erros*.lean) *)

(* E3: caso base da formula do texto para b_k (ErrosGram.bTexto_neg): 1 - gamma - (H_3 - log 4) < 0. *)
Theorem b_texto_base : forall g l2 s : R,
  5772156/10000000 < g -> l2 < 6931471808/10000000000 -> 11/6 - 2*l2 <= s ->
  1 - g - s < 0.
Proof. intros; lra. Qed.

(* E4: G12 > 0,7722084 > 0,7722083 (ErrosGram.G12_cotas). *)
Theorem G12_tabela : forall g l2 lp : R,
  g < 5772163/10000000 -> 6931471803/10000000000 < l2 -> 11447295/10000000 < lp ->
  7722084/10000000 < 3/4*(l2 + lp - g) - 1/4*l2.
Proof. intros; lra. Qed.

(* E12: D_N log N < C0 = 2 + gamma - log 4pi para N = 256, 8000 (ErrosGram.produtos_abaixo_C0). *)
Theorem produtos_C0 : forall g l2 lp d : R,
  5772156/10000000 < g -> l2 < 6931471808/10000000000 -> 6931471803/10000000000 < l2 ->
  lp < 11447300/10000000 -> d < 2231436/10000000 -> 2231435/10000000 < d ->
  82337162772/10000000000000 * (8*l2) < 2 + g - (2*l2 + lp) /\
  50691202/10000000000 * (6*l2 + 3*(2*l2 + d)) < 2 + g - (2*l2 + lp).
Proof. intros; split; lra. Qed.

(* E10: com u = 1/T > 1/4 (T < 4) a regiao 1/2 + u <= s <= 1 - u e vazia (ErrosAnaliticos.R_vazio). *)
Theorem regiao_vazia : forall u s : R, 1/4 < u -> ~ (1/2 + u <= s /\ s <= 1 - u).
Proof. intros u s H [H1 H2]; lra. Qed.

(* E13: 0,831907 < 1/zeta(3) < 0,8319075 (ErrosConstantes.inv_zeta_tres_cotas), na forma multiplicativa. *)
Theorem inv_zeta3 : forall z : R,
  12020568851/10000000000 < z -> z < 12020569219/10000000000 ->
  831907/1000000 * z < 1 /\ 1 < 8319075/10000000 * z.
Proof. intros; split; lra. Qed.

(* ---------------------------------------- fechamento (rodada 8, ATK/XiPhi, ATK/ToeplitzTN) *)

(* Xi = 2 int Phi cos: a constante 1/2 + 2 sum h'(0) e zero (XiPhi.constante_zero). *)
Theorem constante_theta : forall P T S : R,
  4*T = P + 1/2 -> S = P/2 - 2*T -> 1/2 + 2*S = 0.
Proof. intros; lra. Qed.

(* 1 + x + x^2: D_3 = -1 < 0 pela recorrencia tridiagonal (ToeplitzTN.um_x_x2). *)
Theorem tri_um_x_x2 : forall d0 d1 d2 d3 : R,
  d0 = 1 -> d1 = 1 -> d2 = d1 - d0 -> d3 = d2 - d1 -> d3 < 0.
Proof. intros; lra. Qed.

(* ---------------------------------------- reciproca de ASW (rodada 9, ATK/ASWReciproca) *)

(* 1/(1 - x + x^2): b_3 = -1 < 0, menor 1x1 de colunas iniciais negativo (ASWRec.cc_de_tn, contrapositiva). *)
Theorem inv_um_x_x2 : forall b0 b1 b2 b3 : R,
  b0 = 1 -> b1 - b0 = 0 -> b2 - b1 + b0 = 0 -> b3 - b2 + b1 = 0 -> b3 < 0.
Proof. intros; lra. Qed.

(* ---------------------------------------- Edrei para funcoes inteiras (rodada 10, ATK/EdreiInteira) *)

(* Descida: cada passo baixa b1 de L_j >= 1/(a0|w|); com a0 = 1, |w| = 2 e b1 = 1, tres passos dao b1 < 0. *)
Theorem descida_tres : forall b0 b1 b2 b3 L0 L1 L2 : R,
  b0 = 1 -> L0 >= 1/2 -> L1 >= 1/2 -> L2 >= 1/2 ->
  b1 = b0 - L0 -> b2 = b1 - L1 -> b3 = b2 - L2 -> b3 < 0.
Proof. intros; lra. Qed.

(* ---------------------------------------- Hadamard de genero 0 (rodada 11, ATK/HadamardGenero0) *)

(* prodCoef com a0 = 1, alpha = (1/2, 1/3): coeficientes 1 + (5/6)z + (1/6)z^2, crescentes com o numero de fatores
   (ATK.Edrei.prodCoef_mono) e <= a0 (soma alpha)^n (ATK.Edrei.prodCoef_le). *)
Theorem prodcoef_dois : forall p10 p11 p12 p20 p21 p22 : R,
  p10 = 1 -> p11 = 1/2 * 1 -> p12 = 0 ->
  p20 = p10 -> p21 = p11 + 1/3 * p10 -> p22 = p12 + 1/3 * p11 ->
  p11 <= p21 /\ p12 <= p22 /\ p22 <= 25/36 /\ 0 < p22.
Proof. intros; repeat split; lra. Qed.

(* ---------------------------------------- Laguerre (rodada 12, ATK/LaguerrePolya) *)

(* Grau 2: se p = x^2 - s x + P tem raizes reais, q = p + c p' tambem (discriminante 4c^2 + disc p). *)
Theorem laguerre_quadratica : forall s P c : R,
  s*s - 4*P >= 0 -> (2*c - s)*(2*c - s) - 4*(P - c*s) >= 0.
Proof.
  intros s P c H.
  assert (E : (2*c - s)*(2*c - s) - 4*(P - c*s) = 4*(c*c) + (s*s - 4*P)) by ring.
  rewrite E. pose proof (Rle_0_sqr c) as Hc. unfold Rsqr in Hc. lra.
Qed.

(* ---------------------------------------- Jensen/Turan (rodada 13, ATK/JensenPolya) *)

(* Se g0 + 2 g1 x + g2 x^2 = 0 com g2 > 0, entao g0 g2 <= g1^2: (g2 x + g1)^2 = g1^2 - g0 g2. *)
Theorem turan_raiz : forall g0 g1 g2 x : R,
  g2 > 0 -> g2*x*x + 2*g1*x + g0 = 0 -> g0*g2 <= g1*g1.
Proof.
  intros g0 g1 g2 x Hg H.
  assert (E : (g2*x + g1)*(g2*x + g1) = g1*g1 - g0*g2).
  { replace (g1*g1 - g0*g2) with (g1*g1 + g2*(g2*x*x + 2*g1*x) - g2*(g2*x*x + 2*g1*x + g0)) by ring.
    rewrite H. ring. }
  pose proof (Rle_0_sqr (g2*x + g1)) as Hs. unfold Rsqr in Hs. lra.
Qed.

(* ------------------------------------------------------------------ auditoria *)
Print Assumptions classificacao.
Print Assumptions P1.
Print Assumptions G_quartica.
Print Assumptions P5_NE.
Print Assumptions curvatura_linha.
Print Assumptions criterio_aproximacao.
Print Assumptions perfeito_verdadeiro.
Print Assumptions turan3.
Print Assumptions jensen_grau2.
Print Assumptions turan_momentos_id.
Print Assumptions tp_a_nao_passa_gamma.
Print Assumptions forma_L6.
Print Assumptions jensen_gamma_detecta.
Print Assumptions rotacao.
Print Assumptions ajuste_intercepto.
Print Assumptions contraexemplo_pedaco.
Print Assumptions b_texto_base.
Print Assumptions G12_tabela.
Print Assumptions produtos_C0.
Print Assumptions regiao_vazia.
Print Assumptions inv_zeta3.
Print Assumptions constante_theta.
Print Assumptions tri_um_x_x2.
Print Assumptions inv_um_x_x2.
Print Assumptions descida_tres.
Print Assumptions prodcoef_dois.
Print Assumptions laguerre_quadratica.
Print Assumptions turan_raiz.
