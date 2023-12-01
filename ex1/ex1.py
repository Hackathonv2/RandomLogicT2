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
        print(f"divided {n} by 3")
        n = n / 3
    elif n % 2 == 0:
        print(f"divided {n} by 2")
        n = n / 2
    else:
        print(f"subtracted {n} by 1")
        n = n - 1

exit(n)