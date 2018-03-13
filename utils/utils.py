import math

def sieveOfEratosthenes(n):
    """
    Given a number n, returns a list of all primes up to n.
    """
    values = [x for x in range(2, n+1)]
    primes = []

    #Any encountered value not marked False is a prime
    for i,v in enumerate(values):
        if v is not False:
            primes.append(v)

            #Assign False to every v-th value starting at the next multiple of v
            values[i+v::v] = [False] * (((n-1) - (i+1)) // v)

    return primes

if __name__ == '__main__':
    print(sieveOfEratosthenes(35000))
