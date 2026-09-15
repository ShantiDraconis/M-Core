from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Hashable, Iterable, Sequence

@dataclass(frozen=True)
class S0:
    """Immutable audit state. Replacing S0 is a new experiment, never a proof step."""
    u0: object
    I_star_0: float
    nu0: float
    chi0: float
    N0: float
    T0: float

@dataclass(frozen=True)
class ZeroPath:
    name: str
    # samples(n) returns (G,H) along a path approaching the zero locus.
    samples: Callable[[int], tuple[float, float]]
    expected_limit: float | None = None

class ISignature(ABC):
    def __init__(self, s0: S0): self._s0 = s0
    @property
    def s0(self) -> S0: return self._s0
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def base(self) -> float: ...
    @abstractmethod
    def amplitude(self, A: float) -> float: ...
    @abstractmethod
    def scale(self, lam: float) -> float: ...
    @abstractmethod
    def dag_edges(self) -> Sequence[tuple[Hashable, Hashable]]: ...
    def zero_paths(self) -> Iterable[ZeroPath]: return ()
