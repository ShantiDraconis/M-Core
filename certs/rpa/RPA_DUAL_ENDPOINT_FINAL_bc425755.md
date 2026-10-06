# RPA DUAL ENDPOINT FINAL CERTIFICATE

STATUS: PENDING_KERNEL
HEAD: bc425755af2b8beec50668defc397eb09c98377a
RUN: 37515066916

## Certified target

The final RPA state contains two distinct endpoint positions simultaneously:

OPEN_ENDPOINT
CLOSED_ENDPOINT

with:

OPEN_ENDPOINT != CLOSED_ENDPOINT            [position/state distinction]
OPEN_ENDPOINT <-> CLOSED_ENDPOINT            [logical identity preservation]

and:

DUAL_ENDPOINT_STATE :=
  OPEN_ENDPOINT
  AND CLOSED_ENDPOINT
  AND (OPEN_ENDPOINT <-> CLOSED_ENDPOINT)

## Canonical chain

OPEN_ENDPOINT + CLOSED_ENDPOINT
= DUAL_ENDPOINT_STATE
= OPEN_MATH + CLOSED_MATH
= OPEN_BRIDGE + CLOSED_BRIDGE
= MATH
= FINAL_ROOT
= GLOBAL_EXTERNAL_CERTIFICATE

## Kernel theorems

- openEndpointSide_ne_closedEndpointSide
- dualEndpointState_iff_transition
- dualEndpointState_iff_both_and_identity
- open_and_closed_coexist
- dual_state_projects_open
- dual_state_projects_closed
- dual_endpoint_full_chain
- dual_endpoint_eq_global_external
- global_certificate_contains_both_endpoints

## Fail-closed rule

GLOBAL_EXTERNAL_CERTIFICATE implies both OPEN_ENDPOINT and CLOSED_ENDPOINT.

Therefore:
- no OPEN-only certificate is valid;
- no CLOSED-only certificate is valid;
- no wrapper can bypass either endpoint;
- the final certificate is a certificate of coexistence and transition.

## Promotion rule

Promote PENDING_KERNEL -> GREEN -> FROZEN -> CERTIFIED only if run 37515066916
completes SUCCESS at HEAD bc425755af2b8beec50668defc397eb09c98377a.

No mathematical endpoint inhabitant may be fabricated by aliases, wrappers,
renaming, or structural equivalence.
