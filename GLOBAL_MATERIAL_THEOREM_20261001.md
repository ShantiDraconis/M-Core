# GLOBAL MATERIAL THEOREM — 2026-10-01

Status: PROVED_INTERNAL_KERNEL + OPEN_PROBLEM_ADAPTERS + EXTERNAL_RECOGNITION_SEPARATED

This document states the strongest common theorem currently supported by the
tri-cyclic material kernel and separates it from the unresolved mathematical
adapters for RH, P vs NP, Navier-Stokes, Hodge, BSD, Beal, and Yang-Mills.

---

## I. Ambient algebra

A material number is

[
x=(M,C,S)in mathbb R^3.
]

The phase rotation is

[
R(M,C,S)=(S,M,C).
]

Hence

[
R^3=I.
]

The cyclic product is the convolution product of the group algebra of C3:

[
(x*y)_0=x_0y_0+x_1y_2+x_2y_1,
]
[
(x*y)_1=x_0y_1+x_1y_0+x_2y_2,
]
[
(x*y)_2=x_0y_2+x_1y_1+x_2y_0.
]

It is associative and commutative over a commutative semiring.

---

## II. Canonical decomposition

Define

[
mu(x)=rac{M+C+S}{3}.
]

The equilibrium projection is

[
P_{eq}x=(mu,mu,mu).
]

The transverse projection is

[
P_{tr}x=x-P_{eq}x.
]

Then

[
x=P_{eq}x+P_{tr}x,
]

and the decomposition is unique with

[
P_{eq}xin E:={(t,t,t)},
qquad
P_{tr}xin T:={(u,v,w):u+v+w=0}.
]

The two sectors intersect only at zero:

[
Ecap T={0}.
]

Thus the real tri-cyclic state space decomposes structurally as

[
mathbb R^3=Eoplus T,
]

with one equilibrium degree of freedom and a two-dimensional transverse phase
plane.

---

## III. Operators

Define

[
D=R-I.
]

In coordinates,

[
D=
egin{pmatrix}
-1&0&1\
1&-1&0\
0&1&-1
end{pmatrix}.
]

Define the symmetric phase Laplacian

[
L=
egin{pmatrix}
-2&1&1\
1&-2&1\
1&1&-2
end{pmatrix}.
]

The kernel proves

[
L=D^2+3D
]

and

[
D^3+3D^2+3D=0.
]

Equivalently,

[
D(D^2+3D+3I)=0.
]

The equilibrium sector is the zero eigenspace:

[
Lx=0iff xin E.
]

On the transverse plane,

[
Lx=-3x.
]

Therefore the exact transverse Laplacian eigenvalue magnitude is

[
oxed{3}.
]

---

## IV. Canonical constants

The kernel forces the following constants; none is fitted.

| Constant | Exact value | Origin |
|---|---:|---|
| rotation order | 3 | R^3=I |
| transverse Laplacian magnitude | 3 | L=-3I on T |
| normalized Laplacian energy | 9 | ||-3x||^2 for ||x||=1 |
| spread/radius factor | 3 | spread=3||P_tr x||^2 |
| scalar-defect energy factor | 6 | E(d,-d,0)=6d^2 |

Lean object:
`canonicalMaterialConstants`.

---

## V. Energy geometry

Define

[
E(x)=
(M-C)^2+(C-S)^2+(S-M)^2.
]

Define the transverse Euclidean radius

[
r_perp^2(x)=|P_{tr}x|_2^2.
]

Then exactly

[
oxed{E(x)=3r_perp^2(x)}.
]

Consequences:

1. (E(x)ge0).
2. (E(x)=0iff x) is balanced.
3. Rotation preserves (E).
4. Balanced translation does not change (E).
5. Scaling obeys
   [
   E(ax)=a^2E(x).
   ]

On normalized transverse states,

[
|x|_2^2=1,qquad xin T,
]

the Laplacian energy is exactly

[
oxed{|Lx|_2^2=9}.
]

This is the intrinsic F2 law of the kernel.

---

## VI. Traction, repulsion and torsion

The kernel defines

[
operatorname{traction}(x)=M-S,
]

[
operatorname{repulsion}(x)=2C-M-S.
]

For two states define the alternating torsion

[
	au(x,y)
=
M_xC_y+C_xS_y+S_xM_y
-C_xM_y-S_xC_y-M_xS_y.
]

It is skew:

[
	au(x,y)=-	au(y,x),
qquad
	au(x,x)=0,
]

and invariant under simultaneous phase rotation.

Define the transverse inner product

[
langle x,yangle_T
=
langle P_{tr}x,P_{tr}yangle.
]

A new exact Lagrange identity is

[
oxed{
E(x)E(y)
=
3	au(x,y)^2
+
9langle x,yangle_T^2
}.
]

Hence

[
oxed{
3	au(x,y)^2le E(x)E(y)
}.
]

Equality holds exactly when

[
langle x,yangle_T=0.
]

Interpretation:

- energy = transverse radial size;
- torsion = oriented transverse area;
- transverse inner product = alignment;
- the identity decomposes the product energy into orientation and alignment.

---

## VII. Scalar defect embedding

Every real scalar defect has a canonical transverse embedding

[
iota(d)=(d,-d,0).
]

It satisfies

[
iota(d)in T
]

and

[
oxed{E(iota(d))=6d^2}.
]

Therefore

[
E(iota(d))=0iff d=0.
]

If (d_n	o0), then

[
E(iota(d_n))	o0.
]

This means scalar F1 problems require no conjectural map merely to enter the
tri-state plane.

---

## VIII. Universal profile law

For any initial state (x) and real profile (a_n), define

[
x_n=P_{eq}x+a_nP_{tr}x.
]

Then exactly

[
oxed{E(x_n)=a_n^2E(x)}.
]

Therefore

[
a_n	o0
Longrightarrow
E(x_n)	o0.
]

Special case:

[
a_n=q^n,quad 0le q<1
]

gives geometric decay

[
E(x_n)=q^{2n}E(x).
]

The profile law also admits slow scales such as

[
a_nasymprac1{sqrt{log n}},
]

provided that convergence is proved in the problem-specific mathematics.

---

## IX. Behavior classes

The common mechanisms are classified as:

- F1 VANISHING — nonnegative observable tends to zero;
- F2 GAP — positive lower spectral/complexity gap;
- F4 REALIZATION — every admissible target receives a source;
- F5 EQUALITY — two canonical invariants agree;
- F6 EXCLUSION — forbidden configuration cannot occur;
- F7 LIMIT — exact convergence to prescribed value;
- F8 FIXED POINT — admissible fixed point of an operator;
- BILATERAL RESOLUTION — independent positive and negative material producers.

These classes classify proof mechanisms, not subject areas.

---

## X. Bilateral open-math logic

For an endpoint proposition (P), choose genuine producer types (A,B) with

[
A	o P,
qquad
B	o
eg P.
]

The state is:

- `OPEN_MATH`: neither producer inhabited;
- `POSITIVE_RESOLVED`: `Nonempty A`;
- `NEGATIVE_RESOLVED`: `Nonempty B`;
- `BOTH_INCONSISTENT`: both inhabited.

The statement

[
Plor
eg P
]

alone does not close anything.  Classical excluded middle does not manufacture
an inhabitant of either producer.

If both producers are inhabited, then

[
Pland
eg P
]

and therefore

[
False.
]

This is an audit failure/inconsistency state, not a third truth value.

---

## XI. Closure protocol

A valid mathematical close must have the form

[
oxed{
	ext{material producer}
	o
	ext{canonical observable}
	o
	ext{exact official endpoint}
}
]

and must answer all five questions:

1. What is the exact positive producer?
2. What is the exact negative producer?
3. What canonical observable binds the producer to the original subject?
4. What theorem transports that observable to the official endpoint?
5. Does the route survive known countermodels, scaling, quantifier and domain audits?

A renamed endpoint, wrapper, existential package storing the conclusion, or
excluded-middle split is not a producer.

---

## XII. Current problem adapters

### RH — F1 / bilateral

Positive producer:

[
DN_Nlearepsilon_N,qquad arepsilon_N	o0.
]

Negative producer:

[
existsarepsilon>0,quadorall N,quad arepsilonle DN_N.
]

Canonical scalar defect:

[
d_N=DN_N
]

or its norm-scale form.

Tri-state energy:

[
E(iota(DN_N))=6DN_N^2.
]

The internal representation is closed.  The genuine open mathematics is the
asymptotic estimate.

Finite certified Gram evidence suggests a slow logarithmic scale, not a
uniform geometric contraction.

### P vs NP — F2 / bilateral

Positive orientation:

construct a same-language universal SAT failure producer proving

[
SAT
otin P.
]

Negative orientation:

construct and verify a genuine polynomial-time deterministic decider for SAT.

The common kernel may supply an abstract F2 mechanism, but the semantic map
from machine behavior to the material gap remains open.

### Navier-Stokes — F7 / bilateral

Positive orientation:

global smooth solution producer for all official admissible data.

Negative orientation:

a genuine smooth admissible datum/forcing with finite-time breakdown or failure
of global smoothness in the exact official formulation.

The two routes must target the official statement, not merely an internal PDE
surrogate.

### Hodge — F4 / bilateral

Positive producer:

for every rational Hodge class, an algebraic cycle realization.

Negative producer:

one explicit smooth projective variety and rational Hodge class outside the
rational span of algebraic cycle classes.

### BSD — F5 / bilateral

Positive producer:

same-curve rank equality plus refined leading coefficient formula and required
arithmetic factors.

Negative producer:

one valid curve violating one of the official universal equalities.

### Beal — F6 / bilateral

Positive producer:

[
orall d,quad 1<gcd(a,gcd(b,c)).
]

Negative producer:

one concrete reduced `T59ResidualCandidate`.

Current extra arithmetic:
- pairwise primitive;
- exactly one even base;
- five mixed exponent families;
- sharp mod-16 restrictions in the two-four family;
- exact quartic factorization on x=z=4 / y=z=4;
- candidate-specific odd-prime support separation.

### Yang-Mills — F2 / bilateral

Positive producer:

genuine 4D continuum construction + Osterwalder-Schrader reconstruction +
positive Hamiltonian spectral gap.

A negative orientation would require a mathematically valid resolution of the
official statement showing that the required theory/mass-gap assertion fails;
an internal zero-gap toy model is insufficient.

---

## XIII. Internal theorem versus external recognition

The project must distinguish:

### INTERNAL_MATH_CLOSED

Requires:
- exact theorem statement;
- producer inhabited;
- all adapters proved;
- no sorry/admit/hidden target;
- build and axiom audit.

### EXTERNAL_SCIENTIFIC_VALIDATION

Requires:
- independent expert verification;
- comparison to the official mathematical statement;
- reproducible proof text/formalization;
- correction of any discovered gap.

### PRIZE_ELIGIBILITY

This is external to the kernel and controlled by the relevant institution.
For the Clay Millennium Prize Problems, the current published rules require,
among other things, a complete solution to the official problem, publication
in a qualifying outlet, at least two years after publication, and general
acceptance in the global mathematics community before CMI consideration.

Thus:

[
	ext{Lean GREEN}

otRightarrow
	ext{Clay award}.
]

The correct implication is closer to

[
	ext{complete official solution}
+
	ext{independent validation}
+
	ext{publication/community process}
	o
	ext{possible institutional consideration}.
]

---

## XIV. The question the framework asks

For every open problem, ask:

[
oxed{
	ext{What is the smallest concrete object whose existence forces one
orientation of the official endpoint?}
}
]

Then ask the dual question:

[
oxed{
	ext{What is the smallest concrete object whose existence forces the
opposite orientation?}
}
]

Only then ask:

[
oxed{
	ext{Can either object be constructed from already proved mathematics,
without storing the desired endpoint inside it?}
}
]

This is the global producer-first logic.

---

## XV. Strongest defensible claim

The tri-cyclic material kernel currently supplies a genuine common
mathematical calculus with:

- C3 algebra;
- equilibrium/transverse decomposition;
- exact projectors;
- cubic operator law;
- fixed transverse spectrum;
- exact energy constants;
- F1 profile transport;
- F2 internal gap;
- scalar-defect embedding;
- torsion/area identity;
- bilateral material-resolution logic.

It does not, by itself, prove RH, P != NP, Hodge, BSD, Beal, Yang-Mills, or the
positive Navier-Stokes route.

The remaining scientific program is to construct exact problem-specific
producers/adapters or their negative counterparts.
