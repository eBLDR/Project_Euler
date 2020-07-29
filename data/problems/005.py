"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""


def find_minimum(range_):
    possible_number = 1

    while True:
        if all(
            [
                possible_number % n == 0 for n in range_
            ]
        ):
            return possible_number

        possible_number += 1

        # Method 2 - probably more efficient
        # match = True

        # for divisor in range_:
        #     if possible_number % divisor != 0:
        #         match = False
        #         possible_number += 1
        #         break
        #
        # if match:
        #     return possible_number


RANGE = range(1, 21)
print(find_minimum(RANGE))
