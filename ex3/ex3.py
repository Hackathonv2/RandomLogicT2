import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nbr_relations, nbr = lines[0].split(' ')
try:
    nbr = int(nbr)
    nbr_relations = int(nbr_relations)
except ValueError:
    print('Error: Input must be an integer')
    exit(0)

if not (nbr_relations >= 1 and nbr_relations < nbr and nbr < 11000):
    print('Error: args no gut')
    exit(0)

relations = {}
for i in range(1, nbr_relations + 1):
    control, controlled = lines[i].split(' ')
    if control not in relations:
        relations[control] = []
    relations[control].append(controlled)

prev_rel = relations
for control in prev_rel.keys():
    for controlled in prev_rel[control]:
        if controlled in prev_rel:
            for child in prev_rel[controlled]:
                relations[control].append(child)



top_control = max(relations, key=lambda k: len(relations[k]))
print(top_control)
