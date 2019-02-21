"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


def sum_digits(n):
    r = 0
    for i in str(n):
        r += int(i)
    return r


NUMBER = 2 ** 1000
print(sum_digits(NUMBER))
