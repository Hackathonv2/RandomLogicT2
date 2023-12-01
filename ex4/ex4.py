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
