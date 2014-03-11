import lib
from collections import defaultdict

def prime_factorization(n):
    primes = []
    candidates = xrange(2, n+1)
    candidate = 2

    while not primes and candidate in candidates:
        if n%candidate == 0 and lib.is_prime(candidate):
            primes = primes + [candidate] + prime_factorization(n/candidate)
        candidate += 1

    return primes

def least_common_multiple(numbers):
    factorsDict = {}

    counter = {}
    # Get the prime factors for each number in the list
    for number in numbers:
        factorsDict[number] = [prime_factorization(number)]

    # For each number and list of factors
    for factors in factorsDict.values():
        factorsCount = defaultdict(int)


        for x in factors[0]:
            factorsCount[x] += 1

        for a,b in factorsCount.iteritems():
            if counter.has_key(a):
                if counter[a] < b:
                    counter[a] = b
            else:
                counter[a] = b

    result = 1
    for prime, primeCount in counter.iteritems():
        result = result * (prime ** primeCount)
    print result

if __name__ == '__main__':
    print least_common_multiple(range(1,21))
