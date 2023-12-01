import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

try:
    nbr = int(lines.pop(0))
except ValueError:
    print('Error: Input must be an integer')
    exit(0)

if nbr < 8 or nbr > 30:
    print('Error: Number must be between 8 and 30')
    exit(0)

indices = ([], [], [], [], [])
for i in range(nbr):
    splitted = lines[i].split(' ')
    for split in splitted:
        letter = split[0]
        index = int(split[1])
        indices[index - 1].append(letter)
    for i in range(len(indices)):
        if len(indices[i]) < max(len(indices[0]), len(indices[1]), len(indices[2]), len(indices[3]), len(indices[4])):
            indices[i].append(None)

test_string = [0,0,0,0,0]
possibilities = ['R', 'V', 'B']
tested = {}
while test_string != [2,2,2,2,2]:
    test_string[0] += 1
    for i in range(len(test_string)):
        if test_string[i] == 3:
            test_string[i] = 0
            test_string[i + 1] += 1
    string = ''
    for i in test_string:
        string += possibilities[i]
    tested[string] = 0
    for i in range(max(len(indices[0]), len(indices[1]), len(indices[2]), len(indices[3]), len(indices[4])) - 1):
        if indices[0][i] == string[0] or indices[1][i] == string[1] or indices[2][i] == string[2] or indices[3][i] == string[3] or indices[4][i] == string[4]:
            tested[string] += 1
        else:
            break

print(tested[max(tested, key=lambda k: tested[k])])