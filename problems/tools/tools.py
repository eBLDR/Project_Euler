"""
Set of tools.
"""


def find_factors(n):
    factors = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n = int(n/i)
                break
    return factors


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def is_prime(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
            if len(div) > 1:
                return False
    else:
        return True
