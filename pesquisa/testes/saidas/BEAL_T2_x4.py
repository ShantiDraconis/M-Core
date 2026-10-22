import sys, os, time
sys.path.insert(0, "/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/code")
from PNP_T1_enc import *
f = FUNCS["XOR"](4)
# plant the known 12-gate circuit and check it satisfies the sb CNF (unit-propagate by adding assignment)
C, meta = encode(4, 12, f, "ATK", "sb")
# known circuit: blocks on (x0,x1)->w, (w,x2)->u, (u,x3)->out ; block(a,b)= OR(a,b), AND(a,b), NOT(AND), AND(OR,NOT)
G=[]
def block(a,b,base):
    return [("ou",a,b),("e",a,b),("nao",base+1,base+1),("e",base,base+2)]
n=4
G += block(0,1,4)       # gates 0..3 -> wires 4..7
G += block(2,7,8)       # wires 8..11
G += block(3,11,12)     # wires 12..15
print(atk_computa(G,4)==f)
assum=[]
for i,(op,a,b) in enumerate(G):
    assum.append(meta["A"][i][a]); assum.append(meta["B"][i][b])
    oA,oO,oN=meta["ops"][i]
    assum.append({"e":oA,"ou":oO,"nao":oN}[op])
for l in assum: C.add([l])
st,model,dt=solve(C,60)
print("planted:",st,dt)
