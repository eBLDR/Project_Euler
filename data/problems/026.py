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


def calculate_recurring_cycle(number_string: str) -> str:
    decimal_digits = number_string.split(".")[1] if "." in number_string else ""

    if not decimal_digits:
        return ""

    for number_of_repeated_digits in range(1, len(decimal_digits)):
        possible_repeated_digits = decimal_digits[:number_of_repeated_digits]

        for init_index in range(number_of_repeated_digits, len(decimal_digits), number_of_repeated_digits):
            if not possible_repeated_digits == decimal_digits[init_index: init_index + number_of_repeated_digits]:
                break
        else:
            return possible_repeated_digits

    return ""


def find_max_recurring_cycle(max_denominator):
    max_recurring = 1
    max_recurring_denominator = None

    for denominator in range(2, max_denominator):
        length_recurring_cycle = len(calculate_recurring_cycle(str(1 / denominator)))

        if length_recurring_cycle > max_recurring:
            max_recurring = length_recurring_cycle
            max_recurring_denominator = denominator

    return max_recurring_denominator


MAX_D = 10
print(find_max_recurring_cycle(MAX_D))
