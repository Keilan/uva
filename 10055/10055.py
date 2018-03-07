import sys

for line in sys.stdin:
    first, second = map(int, line.split()[:2])

    if first > second:
        print(first-second)
    else:
        print(second-first)
