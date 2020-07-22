"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from problems.tools.tools import proper_divisors


def sum_of_proper_divisors(number):
    return sum(proper_divisors(number))


def is_pair_amicable(n, m):
    return sum_of_proper_divisors(n) == m and sum_of_proper_divisors(m) == n


def find_all_amicable(limit):
    amicable = set()
    for i in range(1, limit):
        possible_friend = sum_of_proper_divisors(i)
        if possible_friend == i:
            continue
        if possible_friend < limit and is_pair_amicable(i, possible_friend):
            amicable.update({i, possible_friend})
    return amicable


LIMIT = 10000
print(sum(find_all_amicable(LIMIT)))
