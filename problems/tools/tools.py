"""
Set of tools.
"""


def product_of_seq(seq):
    r = 1
    for n in seq:
        r *= n
    return r


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def sum_digits(n):
    r = 0
    for i in str(n):
        r += int(i)
    return r


def proper_divisors(n):
    r = []
    for i in range(1, n):
        if n % i == 0:
            r.append(i)

    return r


def find_prime_factors(n):
    r = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                r.append(i)
                n = int(n / i)
                break
    return r


def find_divisors(n):
    r = []
    for i in range(1, n + 1):
        if n % i == 0:
            r.append(i)
    return r


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
