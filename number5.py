import math, sys

def prime_factorization(n):
  def is_prime(n):
    return not [x for x in xrange(2, int(math.sqrt(n))) if n%x==0]

  primes = []
  candidates = xrange(2, n+1)
  candidate = 2

  while not primes and candidate in candidates:
    if n%candidate == 0 and is_prime(candidate):
      primes = primes + [candidate] + prime_factorization(n/candidate)
    candidate += 1

  return primes

  def least_common_multiple(numbers):
    factors = {}
    
    # Get the prime factors for each number in the list
    for number in numbers:
      factors[number] = [prime_factorization(number)]

    # For each number and list of factors
    for k,v in factors.iteritems():
      factorsCount = {}

      for x in v[0]:
        if x in factorsCount:
          factorsCount[x]++
        else:
          factorsCount[x] = 1

        v[1] = factorsCount

    

if __name__ == '__main__':
  print prime_factorization(25)
