import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

try:
    str1 = str(lines[0])
    str2 = str(lines[1])
except ValueError:
    print('Error: Input must be an integer')
    exit(0)
except IndexError:
    print('input too short')
    exit(0)

def get_common(str1, str2):
    common = ""
    for char in str1:
        if char in str2:
            common += char
    return common

common1 = get_common(str1, str2)
common2 = get_common(str2, str1)
if (common1 == common2):
    print("TEMPETE")
    print(common1)
else:
    print("NORMAL")
    