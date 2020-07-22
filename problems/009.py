"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def satisfy_condition(n):
    scope = range(1, 500)
    for a in scope:
        for b in scope:
            if b <= a:
                continue
            for c in scope:
                if c <= b or c <= a:
                    continue
                if a + b + c == n:
                    if is_pythagorean_triplet(a, b, c):
                        return a * b * c


VALUE = 1000
print(satisfy_condition(VALUE))
