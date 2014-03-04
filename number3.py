from lib import factorize

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

if __name__ == '__main__':
    print largestPrime(600851475143)
