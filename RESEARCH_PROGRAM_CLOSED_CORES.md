# Closed Cores — Research Program

Status: SOURCE_CATALOG_ONLY / NO_MATHEMATICAL_PROMOTION  
Repository role: cross-repository conceptual framework  
Branch: audit/closed-chain-v2.1

This document is a research agenda. It does not claim that the proposed
framework proves any Millennium problem, P versus NP, RH, or an independence
result.

## 1. Boolean core

Let

D := (NP ⊆ P).

Because P ⊆ NP is classical, D is equivalent to P = NP. Its negation is
equivalent to NP ⊄ P and hence P ≠ NP.

Under classical excluded middle:

D ∨ ¬D

and D ∧ ¬D is impossible.

This is structural wiring, not a solution of P versus NP.

## 2. The 0,1,2 encoding

For two Boolean coordinates R,I ∈ {0,1}, define

N(R,I) := R² + I².

Then N(R,I) ∈ {0,1,2}.

The value 2 occurs exactly at (R,I)=(1,1). If the chosen semantics requires
R and I to be mutually exclusive, N=2 can be designated as a contradiction
detector.

Important distinction:

- "N=2 is inconsistent" is not a theorem of Gaussian integers.
- It is a semantic invariant of a particular encoding with an exclusivity
  axiom.

For z=a+bi ∈ Z[i], the Gaussian norm is a²+b². The integer 3 is not a Gaussian
norm because a²+b²=3 has no integer solution. This arithmetic fact is separate
from the Boolean 0,1,2 encoding.

## 3. Prime-indexed extensions

Research directions:

1. Boolean vectors d=(d_p)_p with d_p∈{0,1}.
2. Multiplicative certificate codes
   C(d)=∏ p^(d_p)
   for finite-support vectors.
3. Weighted variants C_w(d)=∏ p^(w_p d_p).
4. Quadratic-form encodings using Gaussian, Eisenstein, or cyclotomic integer
   rings.

These constructions are encodings. They do not create complexity lower bounds
by themselves.

### Eisenstein direction

The Eisenstein norm

N(a+bω)=a²-ab+b²

represents arithmetic classes different from the Gaussian norm. Whether a
single cyclotomic ring such as Z[ζ_12] gives the desired invariant structure
for a specified prime list is a research question and must be proved; it is
not assumed here.

## 4. Cross-problem axes

A generic closed-core state may be represented by a Boolean vector

X=(x_1,...,x_k) ∈ {0,1}^k,

where coordinates refer to independently stated mathematical propositions.

The framework may track:
- truth state,
- proof status,
- refutation status,
- external-classical provenance,
- open-bridge obligations.

No numerical norm is allowed to promote an open proposition to a theorem.

## 5. Riemann axis

Let R denote the proposition RH.

The pair (D,R) lies in {0,1}² at the semantic level if both propositions are
assigned truth values in a meta-model. The norm R²+D² again lies in {0,1,2}.

This does not imply any logical relation between RH and P versus NP.

The bridge

RH ⇒ P ≠ NP

is OPEN / UNPROVED in this framework.

## 6. Proposed monograph

Working title:

Closed Cores: A Number-Theoretic Framework for Complexity Dichotomies

Proposed chapters:

1. Boolean closure and 0,1,2 encodings
2. Gaussian and Eisenstein norm signatures
3. Prime-indexed and Gödel-style certificate codes
4. Multi-axis theorem-status matrices
5. Riemann and complexity as independent axes
6. Formal verification in Lean
7. Real open bridges: polySAT or superpolynomial lower bounds
8. Speculative extensions: quantum, p-adic, HoTT/topos, L-functions
9. Audit methodology and no-promotion firewall

## 7. Formalization policy

Allowed:
- definitions,
- finite arithmetic identities,
- Boolean exclusivity lemmas,
- norm calculations,
- encoding injectivity theorems,
- exact theorem-status metadata.

Forbidden:
- treating an encoding as a complexity theorem,
- treating a norm value as proof of inconsistency without the stated semantic
  exclusivity invariant,
- claiming RH ⇒ P ≠ NP without a genuine bridge,
- claiming novelty without literature audit,
- using project axioms to close an open bridge.

## Frontier

The framework becomes oriented only when one obtains genuinely new mathematics,
for example:

- P=NP route: an explicit polynomial-time SAT algorithm with correctness and
  complexity proof;
- P≠NP route: an unconditional lower bound separating an NP language from P
  and surviving known barrier analyses;
- cross-domain route: a rigorously proved theorem connecting an arithmetic
  criterion to a complexity separation.

Until then this repository records structure, not a solution.
