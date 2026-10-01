theory ATK_Seven_Lanes
  imports ATK_Closure
begin

type_synonym
  ('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle =
  "'rh * 'pnp * 'ym * 'ns * 'bsd * 'hodge * 'beal"

definition rh_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'rh" where
  "rh_of B = fst B"

definition pnp_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'pnp" where
  "pnp_of B = fst (snd B)"

definition ym_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'ym" where
  "ym_of B = fst (snd (snd B))"

definition ns_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'ns" where
  "ns_of B = fst (snd (snd (snd B)))"

definition bsd_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'bsd" where
  "bsd_of B = fst (snd (snd (snd (snd B))))"

definition hodge_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'hodge" where
  "hodge_of B = fst (snd (snd (snd (snd (snd B)))))"

definition beal_of ::
  "('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle => 'beal" where
  "beal_of B = snd (snd (snd (snd (snd (snd B)))))"

definition build_seven ::
  "'rh => 'pnp => 'ym => 'ns => 'bsd => 'hodge => 'beal =>
   ('rh,'pnp,'ym,'ns,'bsd,'hodge,'beal) seven_bundle" where
  "build_seven rh pnp ym ns bsd hodge beal =
    (rh,pnp,ym,ns,bsd,hodge,beal)"

theorem build_seven_projects_rh:
  "rh_of (build_seven rh pnp ym ns bsd hodge beal) = rh"
  by (simp add: rh_of_def build_seven_def)

theorem build_seven_projects_pnp:
  "pnp_of (build_seven rh pnp ym ns bsd hodge beal) = pnp"
  by (simp add: pnp_of_def build_seven_def)

theorem build_seven_projects_ym:
  "ym_of (build_seven rh pnp ym ns bsd hodge beal) = ym"
  by (simp add: ym_of_def build_seven_def)

theorem build_seven_projects_ns:
  "ns_of (build_seven rh pnp ym ns bsd hodge beal) = ns"
  by (simp add: ns_of_def build_seven_def)

theorem build_seven_projects_bsd:
  "bsd_of (build_seven rh pnp ym ns bsd hodge beal) = bsd"
  by (simp add: bsd_of_def build_seven_def)

theorem build_seven_projects_hodge:
  "hodge_of (build_seven rh pnp ym ns bsd hodge beal) = hodge"
  by (simp add: hodge_of_def build_seven_def)

theorem build_seven_projects_beal:
  "beal_of (build_seven rh pnp ym ns bsd hodge beal) = beal"
  by (simp add: beal_of_def build_seven_def)

text "
The seven_bundle is only a product of seven already supplied inhabitants.
It cannot manufacture any lane.  This is the Isabelle/HOL counterpart of
Lean SevenInhabitantBundle and Coq SevenInhabitants.
"

end
