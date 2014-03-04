from lib import factorize

def isPalindrome(n):
    test = str(n)
    return test == test[::-1]

def chunker(lst):
    return (lst[pos-2:pos] for pos in xrange(len(lst), 0, -2))

def solve():
    for x in range(998001, 0, -1):
        if isPalindrome(x):
            factors = factorize(x)
            for pair in chunker(factors):
                if len(str(pair[0])) == 3 and len(str(pair[1])) == 3:
                    return x

if __name__ == '__main__':
    pair = solve()
    print pair

