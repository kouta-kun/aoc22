import fetch_input
import os
import re
lines = list(fetch_input.get_input(7))
def group_string(string, line_len):
    while len(string) > 0:
        yield string[:line_len]
        string = string[line_len:]

i = 0
curdir = None
dirs = {}
subdirs = {}
for line in lines:
    if len(line.strip()) == 0: continue
    if line[0] == '$':
        c, cmd, *args = line.split()
        if cmd == 'cd':
            path ,= args
            if path[0] == '/':
                curdir = path
            else:
                curdir = os.path.normpath(os.path.join(curdir, path))
            if curdir not in dirs:
                dirs[curdir] = 0
                subdirs[curdir] = []
    else:
        sz, fname = line.split()
        if sz != 'dir':
            dirs[curdir] += int(sz)
        else:
            subdirs[curdir].append(os.path.normpath(os.path.join(curdir, fname)))

dirsizes = {}
def dirsize(dirname):
    dsize = dirs[dirname]
    for i in subdirs[dirname]:
        if i in dirs:
            dsize += dirsize(i)
    return dsize
totsize = 0
# part 1
for d in dirs:
    dsize = dirsize(d)
    if dsize <= 100000:
        totsize += dsize
print(totsize)
# part 2
totsize = dirsize('/')
unused = 70000000 - totsize
ms = None
for d in dirs:
    ds = dirsize(d)
    if unused + ds >= 30000000:
        if ms is None or ms > ds:
            ms = ds
print(ms)
