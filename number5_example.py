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




if __name__ == '__main__':
  print prime_factorization(25)
