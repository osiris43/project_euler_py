import math

def factorize(n):
    factors = []

    for x in range(2, int(math.sqrt(n))+1):
        if n%x == 0:
            factors.append(x)
            factors.append(n/x)

    return factors
