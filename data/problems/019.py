"""
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime


def count_sundays_on_first(start_date, end_date):
    sundays_on_first = 0
    date = start_date

    while date <= end_date:
        if date.day == 1 and date.weekday() == 6:
            sundays_on_first += 1
        date += datetime.timedelta(days=1)

    return sundays_on_first


start = datetime.datetime(1901, 1, 1)
end = datetime.datetime(2000, 12, 31)
print(count_sundays_on_first(start, end))
