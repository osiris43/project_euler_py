import sys

ListOfPrimes=[2,3,5,7,11,13,17,19]
maxprimeinlist=ListOfPrimes[-1]
 
# Put Primes in a dictionary
DictPrime={}
DictPrime.fromkeys(ListOfPrimes,True)

def intsqrt(n):
  """ Return the integer square root of a long number """
  def intsqrt_core(digitpair,remainder,results):
    # function intsqrt_core returns (results,remainder)
    if digitpair<100:
      currvalue=remainder*100 + digitpair
      for d in range(9,-1,-1):
        x=(2*10*results + d)*d
        if x <= currvalue:
          remainder= currvalue - x
          results=results*10 + d
          return(results,remainder)
    else:
      (results,remainder)=intsqrt_core(digitpair//100,remainder,results)
      (results,remainder)=intsqrt_core(digitpair%100,remainder,results)
      return(results,remainder)
  (results,remainder)=intsqrt_core(n,0,0)
  return results

def isPrime(n):
  """ Return True if n is a prime """
  if DictPrime.has_key(n):
    return True
  high=intsqrt(n)
  for x in ListOfPrimes:
    if x <= high and n%x == 0:
      return False
    if x >= high:
      return True
  x=maxprimeinlist + 2
  while x<=high:
    if n%x == 0:
      return False
    x += 2
  return True

def factorize(n):
  """ Factorize a integer number """
  primes = []
  candidate = 2
  while not primes and candidate <= n:
    if n%candidate == 0 and isPrime(candidate):
      primes = primes + [candidate] + factorize(n/candidate)
    candidate += 1
  return primes

def condense(L):
  """ Condense result in list to prime^nth_power format """
  prime,count,list=0,0,[]
  for x in L:
    if x == prime:
      count += 1
    else:
      if prime != 0:
        list = list + [str(prime) + '^' + str(count)]
      prime,count=x,1
  list = list + [str(prime) + '^' + str(count)]
  return list

if __name__ == '__main__':
  print condense(factorize(long(600851475143)))

