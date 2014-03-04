from number3 import isPrime, largestPrime, factorize

def testTwoIsPrime():
    assert isPrime(2)

def testThreeIsPrime():
    assert isPrime(3)

def testTwentyIsNotPrime():
    assert not isPrime(20)

def testLargestPrimeOf13195Is29():
    assert largestPrime(13195) == 29

def testfactor():
    print factorize(9009)

def testSolution():
    answer = largestPrime(600851475143)
    print "the answer is " + str(answer)
