import sys

n = int(sys.stdin.readline())

for _ in range(n):
    first, second = map(int, sys.stdin.readline().split())

    if first > second:
        print('>')
    elif first < second:
        print('<')
    else:
        print('=')
