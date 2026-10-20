from python.m_core.dag import (
    has_cycle_G1_G4,
    reachable_plus,
    downstream_of_G1_only,
)


def test_reachable_plus_empty_is_not_reflexive():
    assert reachable_plus([], "x", "x") is False


def test_reachable_plus_nonempty_cycle_returns_to_source():
    edges = [("G1", "G4"), ("G4", "G1")]
    assert reachable_plus(edges, "G1", "G1") is True
    assert has_cycle_G1_G4(edges) is True


def test_reachable_plus_transitive_nonempty_path():
    edges = [("a", "b"), ("b", "c")]
    assert reachable_plus(edges, "a", "c") is True
    assert reachable_plus(edges, "c", "a") is False


def test_downstream_gate_rejects_targetY_readback():
    edges = [("Y", "mid"), ("mid", "a(t)")]
    assert reachable_plus(edges, "Y", "a(t)") is True
    assert downstream_of_G1_only(edges) is False


def test_downstream_gate_rejects_I_readback():
    edges = [("I", "mid"), ("mid", "a(t)")]
    assert reachable_plus(edges, "I", "a(t)") is True
    assert downstream_of_G1_only(edges) is False


def test_clean_fixture_has_no_forbidden_reachability():
    edges = [("G1", "a(t)"), ("a(t)", "G4")]
    assert has_cycle_G1_G4(edges) is False
    assert reachable_plus(edges, "Y", "a(t)") is False
    assert reachable_plus(edges, "I", "a(t)") is False
    assert downstream_of_G1_only(edges) is True
