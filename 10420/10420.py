import sys

n = int(sys.stdin.readline())

countries = {}

for _ in range(n):
    country = sys.stdin.readline().split()[0]

    #Add to the current value (or 0 if not present)
    countries[country] = countries.get(country, 0) + 1

#Order keys alphabetically
keys = sorted(countries.keys())

for k in keys:
    print('{} {}'.format(k,countries[k]))
