"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def calculate_recurring_cycle(number):
    recurring = 1

    for n in str(number):
        pass

    return recurring


def find_max_recurring_cycle(max_denominator):
    max_recurring = 1
    max_recurring_denominator = None

    for denominator in range(2, max_denominator):
        unit_fraction = calculate_recurring_cycle(1 / denominator)
        recurring_cycle = calculate_recurring_cycle(unit_fraction)

        if calculate_recurring_cycle(unit_fraction) > max_recurring:
            max_recurring = recurring_cycle
            max_recurring_denominator = denominator

    return max_recurring_denominator


MAX_D = 1000
print(find_max_recurring_cycle(MAX_D))
