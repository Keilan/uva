import sys

for line in sys.stdin:
    participants, budget, hotels, weeks = map(int, line.split())

    min_cost = 500000 + 1 #higher than the max budget to start

    while hotels:
        price = int(sys.stdin.readline())
        data = list(map(int, sys.stdin.readline().split()))

        #If there is enough room and the price is cheaper, update cost
        if max(data) >= participants:
            cost = price*participants

            if cost < min_cost:
                min_cost = cost

        hotels -= 1

    if min_cost <= budget:
        print(min_cost)
    else:
        print('stay home')
