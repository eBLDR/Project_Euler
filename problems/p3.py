"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def find_prime_factors(n):
    factors = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
                n = int(n/i)
                break
    return factors


def max_in_seq(seq):
    return max(seq)


N = 600851475143
print(max_in_seq(find_prime_factors(N)))
