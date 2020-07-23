"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from data.tools.tools import is_prime


def primes_below_limit(l):
    primes = []
    n = 2
    while n < l:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes


def add_seq(seq):
    return sum(seq)


LIMIT = 2000000
print(add_seq(primes_below_limit(LIMIT)))
