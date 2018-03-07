import sys

for line in sys.stdin:
    v, t = map(int, line.split())

    # Derive this formula as follows
    # 1. a = (v - v_initial)/t
    # 2. Plug a into d = v_initial*t + (1/2)at**2
    # 3. Simplify to get d = 2vt
    print(2*v*t)
