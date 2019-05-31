"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from problems.tools.tools import is_prime


def find_prime_by_index(i):
    primes = []
    # last_digit = ['1', '3', '7', '9']
    n = 2
    while len(primes) < i:
        # Filter for performance, only numbers ending with these values can be prime
        # if len(str(n)) > 1 and str(n)[-1] in last_digit:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes[-1]


INDEX = 10001
print(find_prime_by_index(INDEX))
