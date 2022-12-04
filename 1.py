import fetch_input
max_cal = [0]*3
cur_cal = 0
for line in fetch_input.get_input(1):
    line = line.strip()
    if len(line) > 0:
        cur_cal += int(line)
    else:
        if cur_cal > max_cal[0]:
            max_cal[0] = cur_cal
        elif cur_cal > max_cal[1]:
            max_cal[1] = cur_cal
        elif cur_cal > max_cal[2]:
            max_cal[2] = cur_cal
        cur_cal = 0
if cur_cal > max_cal[0]:
    max_cal[0] = cur_cal
elif cur_cal > max_cal[1]:
    max_cal[1] = cur_cal
elif cur_cal > max_cal[2]:
    max_cal[2] = cur_cal
print(max_cal, sum(max_cal))
