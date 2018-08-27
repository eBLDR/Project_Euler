"""
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


def fibonacci_series(upper_limit):
    """ n = n-1 + n-2"""
    seq = [1, 2]
    i = 0
    while True:
        n = seq[i] + seq[i + 1] if seq[i] + seq[i + 1] <= upper_limit else None
        if n:
            seq.append(n)
            i += 1
        else:
            break
    return seq


def sum_even_seq(seq):
    r = []
    for i in seq:
        if i % 2 == 0:
            r.append(i)
    return sum(r)


LIMIT = 4000000
print(sum_even_seq(fibonacci_series(LIMIT)))
