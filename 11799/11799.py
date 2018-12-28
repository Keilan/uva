import sys

n = int(sys.stdin.readline())

for idx in range(n):
    speeds = [int(i) for i in sys.stdin.readline().split()]
    print('Case {}: {}'.format(idx+1, max(speeds)))
