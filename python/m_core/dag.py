from collections import defaultdict
from typing import Hashable, Iterable

Edge = tuple[Hashable, Hashable]


def adjacency(edges: Iterable[Edge]):
    out = defaultdict(list)
    for a, b in edges:
        out[a].append(b)
    return out


def reachable(edges: Iterable[Edge], src: Hashable, dst: Hashable) -> bool:
    """Reflexive-transitive reachability, matching Lean Reachable."""
    adj = adjacency(edges)
    stack = [src]
    seen = set()
    while stack:
        x = stack.pop()
        if x == dst:
            return True
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adj.get(x, ()))
    return False


def reachable_plus(edges: Iterable[Edge], src: Hashable, dst: Hashable) -> bool:
    """Nonempty transitive reachability, matching Lean ReachablePlus.

    At least one edge must be traversed. In particular, src == dst is true
    only when there is an actual nonempty directed cycle back to src.
    """
    edges = list(edges)
    adj = adjacency(edges)
    stack = list(adj.get(src, ()))
    seen = set()
    while stack:
        x = stack.pop()
        if x == dst:
            return True
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adj.get(x, ()))
    return False


def has_cycle_through(edges: Iterable[Edge], node: Hashable) -> bool:
    edges = list(edges)
    return reachable_plus(edges, node, node)


def has_cycle_G1_G4(edges: Iterable[Edge]) -> bool:
    """Lean parity: g1 ->+ g4 and g4 ->+ g1."""
    edges = list(edges)
    return reachable_plus(edges, "G1", "G4") and reachable_plus(edges, "G4", "G1")


def downstream_of_G1_only(edges: Iterable[Edge], forbidden_readers=("Y", "I")) -> bool:
    """Lean parity for the downstream gate.

    Reject G1/G4 feedback and any nonempty readback Y ->+ a(t) or I ->+ a(t).
    """
    edges = list(edges)
    if has_cycle_G1_G4(edges):
        return False
    return not any(reachable_plus(edges, x, "a(t)") for x in forbidden_readers)
