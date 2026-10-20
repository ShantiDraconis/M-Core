# I3 Tristable — OPEN_MATH Lane

Status: OPEN_MATH

Scope: only the I3 tristable claim. This lane does not change the state of any Millennium-problem endpoint or the global FINAL_ROOT.

## Mathematical target

Let omega be a primitive cube root of unity in C. Formalize and kernel-check:

1. omega^3 = 1.
2. omega != 1.
3. The three states 1, omega, omega^2 are pairwise distinct.
4. 1 + omega + omega^2 = 0.
5. Multiplication by omega induces the exact three-cycle
   Manifesto -> Travessia -> Semente -> Manifesto.

Semantic labels:
- Manifesto = 1
- Travessia = omega
- Semente = omega^2

## Required certificates

I3-DEFINITION -> I3-DISTINCT-3 -> I3-CYCLE -> I3-PERIOD-3 -> I3-EQUILIBRIUM -> I3-FINAL-THEOREM -> I3-AXIOM-AUDIT -> I3-FROZEN -> I3-CERTIFIED

## Fail-closed rule

SOURCE -> BUILD_PENDING -> GREEN -> FROZEN -> CERTIFIED.

Do not mark GREEN with sorry, admit, a newly introduced axiom that states the target, fabricated CI evidence, semantic weakening, or circular reasoning.

The OPEN_MATH state closes only for I3 after the exact I3 final theorem is kernel-checked and its audit passes. Global math_state, FINAL_ROOT, and FINAL_PROOF remain unchanged.

## Initial state

I3-DEFINITION: SOURCE
I3-DISTINCT-3: BUILD_PENDING
I3-CYCLE: BUILD_PENDING
I3-PERIOD-3: BUILD_PENDING
I3-EQUILIBRIUM: BUILD_PENDING
I3-FINAL-THEOREM: BUILD_PENDING
I3-AXIOM-AUDIT: BUILD_PENDING
I3->GLOBAL-OPEN_MATH: UNPROVED
