#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'master-terminal' / 'wrapper_equivalence_registry.json'

EXPECTED = {'RIEMANN','P_VS_NP','BEAL','HODGE','YANG_MILLS','BSD','NAVIER_STOKES'}

def fail(msg: str) -> None:
    raise SystemExit('WRAPPER_EQUIVALENCE_RED: ' + msg)

def main() -> int:
    data = json.loads(REGISTRY.read_text())
    lanes = data.get('lanes', [])
    if len(lanes) != 7:
        fail(f'expected 7 lanes, found {len(lanes)}')
    slots = [x.get('slot') for x in lanes]
    if set(slots) != EXPECTED or len(slots) != len(set(slots)):
        fail(f'slot mismatch: {slots}')
    for lane in lanes:
        slot = lane['slot']
        credit = lane.get('terminal_credit', 0)
        state = lane.get('inhabitant_state')
        if state != 'PRODUCED' and credit != 0:
            fail(f'{slot} has terminal credit without a produced inhabitant')
        if credit not in (0, 1):
            fail(f'{slot} terminal_credit must be 0 or 1')
        if state == 'PRODUCED':
            evidence = lane.get('producer_evidence')
            if not isinstance(evidence, dict):
                fail(f'{slot} PRODUCED requires producer_evidence')
            required = ('theorem','sha','run_id','axiom_audit')
            missing = [k for k in required if not evidence.get(k)]
            if missing:
                fail(f'{slot} producer_evidence missing: {missing}')
            if evidence.get('axiom_audit') != 'CLEAN':
                fail(f'{slot} produced inhabitant requires CLEAN axiom audit')
            if credit != 1:
                fail(f'{slot} produced inhabitant must carry terminal_credit=1')
    print('WRAPPER_EQUIVALENCE_GREEN')
    print('SLOTS=7')
    print('TERMINAL_CREDIT=' + str(sum(x.get('terminal_credit',0) for x in lanes)) + '/7')
    print('POLICY=NO_WRAPPER_PROMOTION')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
