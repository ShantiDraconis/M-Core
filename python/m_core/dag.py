from collections import defaultdict
from typing import Hashable, Iterable

Edge = tuple[Hashable, Hashable]

def adjacency(edges: Iterable[Edge]):
    out = defaultdict(list)
    for a, b in edges: out[a].append(b)
    return out

def reachable(edges: Iterable[Edge], src: Hashable, dst: Hashable) -> bool:
    adj = adjacency(edges); stack=[src]; seen=set()
    while stack:
        x=stack.pop()
        if x == dst: return True
        if x in seen: continue
        seen.add(x); stack.extend(adj.get(x, ()))
    return False

def has_cycle_through(edges: Iterable[Edge], node: Hashable) -> bool:
    edges=list(edges); adj=adjacency(edges)
    return any(reachable(edges, nxt, node) for nxt in adj.get(node, ()))

def has_cycle_G1_G4(edges: Iterable[Edge]) -> bool:
    edges=list(edges)
    return reachable(edges, "G1", "G4") and reachable(edges, "G4", "G1")

def downstream_of_G1_only(edges: Iterable[Edge], forbidden_readers=("Y", "I")) -> bool:
    """Conservative gate: G1 must not lie on a cycle and downstream coefficient a(t)
    must not depend on target/conclusion nodes Y or I."""
    edges=list(edges)
    if has_cycle_through(edges, "G1"): return False
    return not any(reachable(edges, x, "a(t)") for x in forbidden_readers)
