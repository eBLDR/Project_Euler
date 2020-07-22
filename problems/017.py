"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
import string


def count_letters(l):
    r = 0
    for word in l:
        for char in word.lower():
            if char in string.ascii_lowercase:
                r += 1
    return r


def generate_word_list():
    word_list = []
    units = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
             '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    ten_to_19 = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
                 '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
                 '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    tenths = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
              '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
    and_ = 'and'
    hundred = 'hundred'
    thousand = 'thousand'

    for i in range(1, 1001):
        if i < 10:
            word_list.append(units[str(i)])

        elif 10 <= i < 100:
            tenth, unit = str(i)[0], str(i)[1]

            if tenth == '1':
                word_list.append(ten_to_19[tenth + unit])
            else:
                word_list.append(tenths[tenth])

                if unit != '0':
                    word_list.append(units[unit])

        elif 100 <= i < 1000:
            hundredth, tenth, unit = str(i)[0], str(i)[1], str(i)[2]

            word_list.append(units[hundredth])
            word_list.append(hundred)

            if i % 100 != 0:
                word_list.append(and_)

            if tenth == '0':
                if unit != '0':
                    word_list.append(units[unit])
            elif tenth == '1':
                word_list.append(ten_to_19[tenth + unit])
            else:
                word_list.append(tenths[tenth])

                if unit != '0':
                    word_list.append(units[unit])

        elif i == 1000:
            word_list.append(units['1'])
            word_list.append(thousand)

    return word_list


print(count_letters(generate_word_list()))
