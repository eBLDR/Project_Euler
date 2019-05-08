"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
from problems.tools.tools import find_divisors


def generator_triangle():
    n = 1
    sum_ = 1
    while True:
        yield sum_
        n += 1
        sum_ += n
        
    # return sum([i for i in range(1, n + 1)])


def find_number_of_factors(n_factors):
    n = 1
    gen = generator_triangle()
    while True:
        r = next(gen)
        if len(find_divisors(r)) > n_factors:
            return r
        n += 1


FACTORS = 500
print(find_number_of_factors(FACTORS))
