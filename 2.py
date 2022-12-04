import fetch_input
REL = {
    ('P','R'): 1,
    ('R','S'): 1,
    ('S','P'): 1
}

VAL = {
    'R': 1,
    'P': 2,
    'S': 3
}

REL = {k:v for k,v in (list(REL.items()) + [(k[::-1], 0) for k,v in REL.items()])}

MY_MAP = {'X':'R','Y':'P','Z':'S'}
OT_MAP = {'A':'R','B':'P','C':'S'}
PT_SEL = 0
PT_WIN = 0

for line in fetch_input.get_input(2):
    line = line.strip()
    if len(line) == 0: continue
    ot,my = line.split()

    my = MY_MAP[my]
    ot = OT_MAP[ot]

    PT_SEL += VAL[my]
    if my == ot:
        PT_WIN += 1
    else:
        PT_WIN += REL[(my,ot)]*2

PT = PT_SEL + (PT_WIN * 3)
print(PT)
