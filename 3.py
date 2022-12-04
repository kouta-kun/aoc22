import fetch_input
priority = {i: ord(i)-ord('a')+1 for i in (chr(i) for i in range(ord('a'), ord('z')+1))}
for i in set(priority):
    priority[i.upper()] = priority[i] + 26
print(priority)

pri_sum = 0
for line in fetch_input.get_input(3):
    line = line.strip()
    if len(line) == 0: continue
    line_a, line_b = line[len(line)//2:], line[:len(line)//2]
    shared_type = set(line_a) & set(line_b)
    if len(shared_type) > 1:
        print('error:',line_a, line_b, shared_type)
    pri_sum += priority[list(shared_type)[0]]
print(pri_sum)
