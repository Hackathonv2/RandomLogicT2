import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

try:
    for i in range(len(lines)):
        lines[i] = int(lines[i])
except ValueError:
    print('Error: Input must be an integer')
    exit(0)

already_got = lines.pop(0)
somme = sum(lines)
need_to_get = somme / 2
got = already_got
got_so_far = 0

lines.sort(reverse=True)

# print(f"sum: {somme}, need to get: {need_to_get}, got: {got}")
while got < need_to_get:
    need_to_get_this_round = need_to_get - got
    closest_number = min(lines, key=lambda x: abs(x - need_to_get_this_round))
    if closest_number < need_to_get_this_round:
        idx = lines.index(closest_number)
        if idx > 0:
            closest_number = lines[idx - 1]
    got += closest_number
    got_so_far += closest_number
    lines.remove(closest_number)

print(got_so_far, end='')
