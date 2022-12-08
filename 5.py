import fetch_input
result = 0
lines = list(fetch_input.get_input(5))
stack_count = 0
for line in lines:
    if len(line) > 0 and all(c in '123456789' for c in  set(line) - {' '}):
        stack_count = max(int(i) for i in line.split() if len(i) > 0)
stacks = [[] for i in range((stack_count))]
print(len(stacks))
print(len(lines[0])+1)
def group_string(string, line_size=4):
    while len(string) >= line_size:
        yield string[:line_size].strip()
        string = string[line_size:]
    if len(string) > 0:
        yield string
moves = 0
for line in lines:
    if len(line.strip()) == 0: continue
    if '[' in line:
        per_stack = group_string(line)
        for stack, inp in zip(stacks, per_stack):
            if len(inp.strip()) > 1:
                stack.append(inp[1])
    if line.split()[0] == 'move':
        moves += 1
        args = line.strip().split()
        qty = int(args[1])
        from_ = int(args[3])-1
        to_ = int(args[5])-1
        print(line, stacks[from_][:qty])
        stacks[to_] = stacks[from_][:qty][::-1] + stacks[to_]
        stacks[from_] = stacks[from_][qty:]
        for i, s in enumerate(stacks):
            print(i, s)
        print('')
print(''.join(s[0] for s in stacks))
