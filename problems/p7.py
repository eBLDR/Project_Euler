"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


def is_prime(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    return True if len(div) == 1 else False


def find_prime_by_index(i):
    primes = []
    n = 0
    while len(primes) < i:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes[-1]


INDEX = 10001
print(find_prime_by_index(INDEX))