# Tri-Cyclic Material Principle — research proposal

Status: PROVED_KERNEL + CONJECTURAL_PROBLEM_ADAPTERS

## 1. Proven kernel theorem

Let x be a real tri-state with unique decomposition

x = balancedProjection(x) + fluctuation(x),

where the first term is balanced and the second has zero total.

For 0 <= q < 1 define

x_n = balancedProjection(x) + q^n fluctuation(x).

Then the formal kernel proves

phaseEnergy(x_n) = q^(2n) phaseEnergy(x),

hence

phaseEnergy(x_n) -> 0.

The same tri-cyclic kernel has an intrinsic transverse Laplacian gap:
on zero-sum states Lx = -3x, and on normalized transverse states the
Laplacian energy is exactly 9.

This gives two simultaneous, rigorously separated mechanisms:
- F1 vanishing by transverse contraction;
- F2 positive spectral gap on the transverse complement.

Lean:
- MCore.MaterialMath.TransverseContraction
- phaseEnergy_geometricTransverseTrajectory
- phaseEnergy_geometricTransverseTrajectory_tendsto_zero
- geometricTransverseVanishingLaw
- triCyclic_F1_F2_kernel

## 2. Scientific proposal

The conjectural principle is not that every open problem is "the same".
It is that each terminal obstruction may admit a faithful problem-specific
observable whose balanced/transverse decomposition exposes one of the already
formalized material laws.

A valid adapter must satisfy all of:
1. canonical binding to the official mathematical object;
2. no target proposition stored as an input field;
3. exact transport from the material law to the official terminal target;
4. preservation of quantifiers, scaling, domain, and normalization;
5. failure on known countermodels/degenerate models.

Only after these are proved may the common kernel be used.

## 3. Seven lane hypotheses

### RH / F1
Construct an observable T_N in TriNumber R from the concrete NB coefficient
error such that

phaseEnergy(T_N) = c * DN(N)

for one explicit c>0, and prove a true transverse contraction or other
VanishingLaw for T_N.

Then the existing
VanishingUpperBound / DNLimit / finite-span chain closes RH.

Open identification:
NB error -> tri-state transverse energy.

### P versus NP / F2
For every canonical polynomial-time deterministic SAT candidate M construct a
tri-state T(M) and canonical SAT instance x(M) such that

positive transverse gap(T(M))
  -> not M.CorrectAt SAT x(M).

The tri-state gap must not encode the failure witness as an input field.

Open identification:
machine semantics -> admissible tri-state gap -> canonical SAT failure.

### Navier-Stokes / F7 or negative resolution
Positive route:
derive tri-state phases from genuine velocity/vorticity observables and prove
transverse contraction gives the strict signed-gain budget.

Negative route:
the 2026 external formal breakdown proof is a separate official resolution
orientation and does not require this adapter.

### Hodge / F4
Associate to each rational Hodge class a material target and prove that a
RealizationLaw source decodes to a genuine algebraic cycle whose cycle class
is the original class.

Open identification:
material realization source -> algebraic cycle.

### BSD / F5
Map one genuine elliptic curve to same-carrier material invariants and prove
that the EqualityLaw is exactly:
- analytic order = Mordell-Weil rank;
- refined leading coefficient identity;
while Sha finiteness remains genuinely represented.

Open identification:
curve arithmetic/analytic invariants -> faithful material equality.

### Beal / F6
Associate each admissible Beal datum to a tri-state for which
coprimality implies membership in a forbidden material configuration.
Then prove the ExclusionLaw from the arithmetic equation.

Open identification:
a^x+b^y=c^z with x,y,z>2 -> exclusion of gcd=1.

### Yang-Mills / F2
Map regulated 4D physical states into the transverse material plane and prove
phase energy controls the same Hamiltonian spectral quantity through regulator
removal and infinite-volume limits.

Open identification:
tri-state phase gap -> physical continuum mass gap.

## 4. Refutation firewall

The proposal is falsified as a universal closing mechanism if, for any lane:
- no faithful canonical observable can be constructed;
- the material invariant loses required quantifiers or scaling;
- the adapter is inhabited by a known countermodel;
- the supposed adapter requires the target theorem itself;
- the transported law is weaker than the official endpoint.

## 5. Strongest current claim

PROVED:
A nontrivial three-phase algebra has:
- unique equilibrium + transverse decomposition;
- exact quadratic phase geometry;
- order-three rotation;
- exact transverse spectral eigenvalue 3;
- normalized spectral energy gap 9;
- exact geometric transverse contraction law;
- F1 vanishing under 0<=q<1;
- F2 positive gap independently.

CONJECTURAL:
that the exact mathematical terminal observables of RH, P!=NP, Hodge, BSD,
Beal, Yang-Mills, and the positive NS route admit faithful adapters into this
kernel.

Therefore this is a unified research mechanism, not a claim that the open
problems are already solved.
