"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
            if len(div) > 1:
                return False
    else:
        return True


def primes_below_limit(l):
    primes = []
    n = 2
    while n < l:
        if is_prime(n):
            primes.append(n)
        n += 1
        if n % 1000 == 0:
            print(n)
    return primes


def add_seq(seq):
    return sum(seq)


LIMIT = 2000000
print(add_seq(primes_below_limit(LIMIT)))
