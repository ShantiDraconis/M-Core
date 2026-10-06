# M-Core RPA Confirmation Certificate v1

Status: **BUILD_PENDING**

Kernel target: `MCore.FinalFail.RPAConfirmation`

Canonical five-view chain:

```
OPEN_MATH + CLOSED_MATH
= OPEN_BRIDGE + CLOSED_BRIDGE
= MATH
= FINAL_ROOT
= GLOBAL_EXTERNAL_CERTIFICATE
```

The five names are formal views of one `RPAConfirmation OpenMath ClosedMath`.

A completed confirmation requires:

- an `OpenMath` witness,
- a `ClosedMath` witness,
- an identity-preserving bridge `OpenMath ↔ ClosedMath`.

This certificate validates the RPA transition architecture. It does **not**
promote any Millennium-problem lane unless that lane's exact material terminal
witness is independently kernel-verified.
