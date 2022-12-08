import fetch_input
lines = list(fetch_input.get_input(6))
line = lines[0]
for i in range(4, len(line)):
    if len(set(line[i-4:i])) == 4:
        print(i)
        break
