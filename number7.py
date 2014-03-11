from lib import is_prime1
import datetime

def solve(n):
    counter = 0
    startingPrime = 1
    while counter < n:
        startingPrime += 1
        if is_prime1(startingPrime):
            counter += 1

    print startingPrime

if __name__ == '__main__':
    a = datetime.datetime.now()
    solve(10001)
    print datetime.datetime.now() - a
