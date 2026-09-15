import dataclasses
import pytest
from python.m_core.signature import S0
from python.m_core.axioms import audit_A1,audit_A2,audit_A3,audit_A4
from adapters.ns_adapter import NSAuditAdapter

@pytest.fixture
def I(): return NSAuditAdapter(S0("u0",0.6,0.01,1.0,1.0,0.0))

@pytest.mark.parametrize("delta",[0.1,0.01,0.001])
def test_A1_delta(I,delta): assert audit_A1(I,[delta])["pass"]
def test_A1_unbounded_witness_family(I):
    vals=[I.amplitude(A) for A in (1,10,100,1000)]
    assert all(a<b for a,b in zip(vals,vals[1:])) and vals[-1]>100

def test_A2_direct_cycle(I): assert audit_A2(I)["cycle"]
def test_A2_downstream_violation(I): assert not audit_A2(I)["downstream_ok"]

def test_A3_K0(I): assert audit_A3(I)["limits"][0] == pytest.approx(0.0)
def test_A3_RHO(I): assert audit_A3(I)["limits"][1] == pytest.approx(0.5)
def test_A3_path_dependence(I): assert audit_A3(I)["pass"] and audit_A3(I)["path_dependent"]

def test_A4_lambda_small(I): assert I.scale(1e-3) == pytest.approx(I.base())
def test_A4_lambda_large(I): assert I.scale(1e3) == pytest.approx(I.base())
def test_A4_calibration_not_theorem(I):
    r=audit_A4(I); assert r["pass"] and r["tau_rigid"] is None and r["eps0_rigid"] is None

def test_S0_frozen(I):
    with pytest.raises(dataclasses.FrozenInstanceError): I.s0.I_star_0=0.7
