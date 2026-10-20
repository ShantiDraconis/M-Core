from python.m_core.signature import ISignature, ZeroPath

class NSAuditAdapter(ISignature):
    """Audit fixture, NOT a Navier-Stokes regularity theorem.
    It realizes the four structural phenomena on explicit test data.
    """
    def name(self): return "NS-audit-fixture"
    def base(self): return 0.4
    def amplitude(self,A): return A*self.base()
    def scale(self,lam):
        if lam <= 0: raise ValueError("critical scaling parameter must be positive")
        return self.base()
    def dag_edges(self):
        return [("G1","G4"),("G4","G1"),("G1","a(t)"),("Y","a(t)"),("I","Y")]
    def zero_paths(self):
        # Same quotient G/H represented by G=x, H=y, approached along x=c*y.
        def path(c): return lambda n: (c/n, 1/n)
        return [ZeroPath("K0",path(0.0),0.0), ZeroPath("RHO",path(0.5),0.5), ZeroPath("ETA",path(1.0),1.0)]
