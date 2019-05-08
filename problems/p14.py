"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def odd_expr(n):
    return n * 3 + 1


def even_expr(n):
    return int(n / 2)


def collatz_terms(n):
    terms = [n]
    while n != 1:
        n = even_expr(n) if n % 2 == 0 else odd_expr(n)
        terms.append(n)
    return terms


def find_longest_chain(limit):
    chains = []
    for i in range(1, limit):
        chains.append(len(collatz_terms(i)))
    return chains.index(max(chains)) + 1


LIMIT = 1000000
print(find_longest_chain(LIMIT))
