"""
Starting in the top left corner of a 2x2 grid, and only being able
to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
from itertools import product


def generate_truth_table(d):
    match = 0
    gen = product([i for i in range(d)], repeat=d)
    for i in gen:
        if sum(i) == d - 1:
            match += 1
    return match


GRID = 20
TABLE_SIZE = GRID + 1
# print(generate_truth_table(TABLE_SIZE))


# It takes to long to compute, using maths based on a result set we get
# the derivative progression:
# 3 + 1/3 + 1/6 + 1/10 + 1/15 + ... = 3 + SUM(1/n!); start on n=2
def factorial(n):
    return sum([i for i in range(1, n + 1)])


result = 6  # Starting value for case when table size is 2
slope = 3
for num in range(2, GRID):
    slope += 1.0 / factorial(num)
    result *= slope


print(result)
