import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

values = []

lines[0] += ' '
try:
    while lines[0].find(' ') != -1:
        values.append(int(lines[0][:lines[0].find(' ')]))
        lines[0] = lines[0][lines[0].find(' ') + 1:]

except ValueError as e:
    print(e)
    exit(0)
except IndexError as e:
    print(e)
    exit(0)

mapper = dict()
for i in values:
    if i in mapper:
        mapper[i] += 1
    else:
        mapper[i] = 1
(big_count, big_value) = (0, 0)
(smol_count, smol_value) = (100, 100)
for i in mapper:
    if big_count < mapper[i] or ((big_count is mapper[i]) and (big_value < i)):
        big_count = mapper[i]
        big_value = i
    if smol_count > mapper[i] or ((smol_count is mapper[i]) and (smol_value > i)):
        smol_count = mapper[i]
        smol_value = i

print(big_value - smol_value)
