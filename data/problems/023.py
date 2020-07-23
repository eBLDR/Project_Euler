"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
from data.tools.tools import proper_divisors


def is_abundant(n):
    return sum(proper_divisors(n)) > n


def all_abundant_integers(limit):
    abundant = []
    for i in range(1, limit + 1):
        if is_abundant(i):
            abundant.append(i)
    return abundant


def two_abundant_sum_integers(limit):
    abundant_int = all_abundant_integers(limit)
    all_integers = set([n for n in range(1, limit)])
    for a_1 in abundant_int:
        for a_2 in abundant_int:
            if a_1 + a_2 in all_integers:
                all_integers.remove(a_1 + a_2)
    return all_integers


LIMIT = 28123
print(sum(two_abundant_sum_integers(LIMIT)))
