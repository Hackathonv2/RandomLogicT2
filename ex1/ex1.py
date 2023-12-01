import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

try:
    nbr = int(lines[0])
except ValueError:
    print('Error: Input must be an integer')
    exit(0)

if nbr < 1 or nbr > 1000:
    print('Error: Number must be between 1 and 1000')
    exit(0)

n = nbr
for i in range (4):
    if n % 3 == 0:
        n = n // 3
    elif n % 2 == 0:
        n = n // 2
    else:
        n = n - 1

print(n)
