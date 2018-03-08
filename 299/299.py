import sys

def bubble_sort(l):
    length = len(l)
    is_sorted = False
    swaps = 0 #Count swaps

    while not is_sorted:
        is_sorted = True #Reset
        for i in range(1,length):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                is_sorted = False
                swaps += 1
        length -= 1 #Last element is guaranteed to be sorted

    return l, swaps


# The forums claim that reading line by line does not work for input because
# blank lines may exist.
def read_line(stream):
    l = ''
    while len(l) == 0 or l.isspace():
        l = stream.readline()
    return l


n = int(read_line(sys.stdin))
for _ in range(n):
    length = int(read_line(sys.stdin))
    if length > 0:
        train = list(map(int, read_line(sys.stdin).split()))
        _, swaps = bubble_sort(train)
    else: #Account for length 0 trains
        swaps = 0
    print('Optimal train swapping takes {} swaps.'.format(swaps))
