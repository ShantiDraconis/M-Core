# Control: Picard numbers of Fermat surfaces rho(X_m^2) = 1 + #{a in (Z/m-0)^4 : sum<t a_i> = 2m for all units t}
import itertools, math, sys
def rho(m):
    U=[t for t in range(1,m) if math.gcd(t,m)==1]
    c=0
    for a in itertools.product(range(1,m),repeat=3):
        a4=(-sum(a))%m
        if a4==0: continue
        v=a+(a4,)
        if all(sum((t*x)%m for x in v)==2*m for t in U): c+=1
    return c+1
for m in range(3,int(sys.argv[1])+1):
    r=rho(m); f=3*(m-1)*(m-2)+1
    print(m, r, "coprime6-formula" if math.gcd(m,6)==1 else "", f if math.gcd(m,6)==1 else "", "OK" if (math.gcd(m,6)!=1 or r==f) else "FAIL")
