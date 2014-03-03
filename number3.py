import math

def largestPrime(n):
    factors = factorize(n)
    # list comprehension?
    factors.sort()
    factors.reverse()

    for factor in factors:
        if isPrime(factor):
            return factor

    return -1

def isPrime(n):
    if len(factorize(n))== 0:
        return True
    else:
        return False

def factorize(n):
    factors = []

    for x in range(2, int(math.sqrt(n))+1):
        if n%x == 0:
            factors.append(x)
            factors.append(n/x)

    return factors

if __name__ == '__main__':
    print largestPrime(600851475143)
