"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""


def is_divisible(dvnd, dvsr):
    return True if dvnd % dvsr == 0 else False


def find_minimum(rng):
    r = None
    dvdn = 1
    while not r:
        match = True
        for dvsr in rng:
            if not is_divisible(dvdn, dvsr):
                match = False
                dvdn += 1
                break
        if match:
            r = dvdn
    return r


RANGE = range(1, 21)
print(find_minimum(RANGE))
