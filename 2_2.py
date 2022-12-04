import fetch_input
REL = {
    ('R','P'): 2,
    ('S','R'): 2,
    ('P','S'): 2
}

VAL = {
    'R': 1,
    'P': 2,
    'S': 3
}

REL = {k:v for k,v in (list(REL.items()) + [(k[::-1], 0) for k,v in REL.items()] + [((s,s), 1) for s in VAL.keys()])}

W_MAP = {s: [k[1] for k,v in REL.items() if k[0] == s and v == 2][0] for s in VAL.keys()}
D_MAP = {s: [k[1] for k,v in REL.items() if k[0] == s and v == 1][0] for s in VAL.keys()}
L_MAP = {s: [k[1] for k,v in REL.items() if k[0] == s and v == 0][0] for s in VAL.keys()}

MY_MAP = {'X':(L_MAP, 0),'Y':(D_MAP,1),'Z':(W_MAP,2)}
OT_MAP = {'A':'R','B':'P','C':'S'}
PT_SEL = 0
PT_WIN = 0

for line in fetch_input.get_input(2):
    line = line.strip()
    if len(line) == 0: continue
    ot,my_t = line.split()
    ot  = OT_MAP[ot]


    my, my_pts = MY_MAP[my_t]

    my_sel = my[ot]

    PT_SEL += VAL[my_sel]
    PT_WIN += my_pts

PT = PT_SEL + (PT_WIN * 3)
print(PT)
