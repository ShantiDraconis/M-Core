# M-Core RPA Confirmation Certificate v1

Status: **BUILD_PENDING**

Kernel target: `MCore.FinalFail.RPAConfirmation`

Canonical chain:

```
OPEN_ENDPOINT + CLOSED_ENDPOINT
= DUAL_ENDPOINT_STATE
= OPEN_MATH + CLOSED_MATH
= OPEN_BRIDGE + CLOSED_BRIDGE
= MATH
= FINAL_ROOT
= GLOBAL_EXTERNAL_CERTIFICATE
```

The two endpoint positions are distinct:

```
EndpointRole.openEndpoint ≠ EndpointRole.closedEndpoint
```

while their logical identity is preserved through:

```
OpenMath ↔ ClosedMath
```

A valid `RPAConfirmation OpenMath ClosedMath` contains both endpoint
witnesses simultaneously, the proof that the endpoint roles are distinct,
and the identity-preserving bridge.

The later names are formal views of that same dual-endpoint state.

This certificate validates the RPA transition architecture. It does **not**
promote a mathematical lane to materially CLOSED unless that lane's exact
terminal endpoint witness is independently kernel-verified.
