"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
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
print(generate_truth_table(TABLE_SIZE))
