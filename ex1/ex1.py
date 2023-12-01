import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int, help='Enter a number from 1 to 1000')
args = parser.parse_args()

if args.number < 1 or args.number > 1000:
    print('Error: Number must be between 1 and 1000')
    exit(1)

n = args.number
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