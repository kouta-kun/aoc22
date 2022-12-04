import fetch_input
count = 0
for line in fetch_input.get_input(4):
    if len(line.strip()) == 0: continue
    a1, a2 = line.split(',')
    aa, ab = a1.split('-')
    ba, bb = a2.split('-')
    arange = set(range(int(aa), int(ab)+1))
    brange = set(range(int(ba), int(bb)+1))
    if arange & brange != set():
        count += 1
print(count)
