"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def find_multiples(upper_limit, n):
    # upper_limit is not included
    r = [i for i in range(n, upper_limit, n)]
    return r


def add_values(list_1, list_2):
    r_set = set(list_1)
    r_set.update(list_2)
    return sum(r_set)


M1, M2 = 3, 5
LIMIT = 1000
result = add_values(find_multiples(LIMIT, M1), find_multiples(LIMIT, M2))
print(result)
