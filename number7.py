from lib import is_prime

def solve(n):
    counter = 0
    startingPrime = 1
    while counter < n:
        startingPrime += 1
        if is_prime(startingPrime):
            counter += 1

    print startingPrime

if __name__ == '__main__':
    solve(10001)

