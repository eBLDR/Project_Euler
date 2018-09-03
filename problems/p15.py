"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from itertools import product


def generate_truth_table(d):
    return [i for i in product([i for i in range(TABLE_SIZE)], repeat=TABLE_SIZE)]


def find_matches(n, array):
    match = 0
    for r in array:
        if sum(r) == n - 1:
            match += 1
    return match


TABLE_SIZE = 20
print(find_matches(TABLE_SIZE, generate_truth_table(TABLE_SIZE)))
