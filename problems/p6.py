"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def square(n):
    return n**2


def sum_of_squares(rng):
    return sum([square(n) for n in rng])


def square_of_sum(rng):
    return square(sum([n for n in rng]))


def difference(n1, n2):
    return n1 - n2


RANGE = range(1, 101)
print(difference(square_of_sum(RANGE), sum_of_squares(RANGE)))
