import sys
import math

for line in sys.stdin:

    n = int(line) - 1 #Formula below is assuming we start at zero

    #Find the row - note that each row has one more element than the last, so we can use the
    # fact that the sum of the first n numbers is n(n-1)/2 and the quadratic equation
    r = math.floor((1 + math.sqrt(1+8*n))/2)

    #Distance from the start of the row to the desired number
    remaining = n - (r*(r-1))/2

    #Handle numerator and denominator separately based on whether row is even or odd
    if r % 2 == 0:
        num = 1 + remaining
        den = r - remaining
    else:
        num = r - remaining
        den = 1 + remaining

    print('TERM {} IS {}/{}'.format(n+1, int(num), int(den)))
