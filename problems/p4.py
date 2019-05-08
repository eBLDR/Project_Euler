"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindromic(n):
    return str(n) == str(n)[::-1]


def palindromic_product(min_, max_):
    r = []
    for i in range(min_, max_ + 1):
        for j in range(min_, max_ + 1):
            p = i * j
            if is_palindromic(p):
                r.append(p)
    return r


MIN = 100
MAX = 999
print(max(palindromic_product(MIN, MAX)))
