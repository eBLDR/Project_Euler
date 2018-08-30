"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from tools.tools import find_prime_factors



def max_in_seq(seq):
    return max(seq)


N = 600851475143
print(max_in_seq(find_prime_factors(N)))
