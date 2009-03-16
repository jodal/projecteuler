"""
You are given the following information, but you may prefer to do some research
for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a
      century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

From http://projecteuler.net/index.php?section=problems&id=19
"""

import datetime as dt

def problem019(start, stop):
    """Cheating by using Python's excellent datetime module"""

    num_sundays_on_the_first = 0
    while start.weekday() != 6:
        start += dt.timedelta(days=1)
    while start <= stop:
        if start.day == 1:
            num_sundays_on_the_first += 1
        start += dt.timedelta(days=7)
    return num_sundays_on_the_first

if __name__ == '__main__':
    assert problem019(dt.date(2009, 2, 1), dt.date(2009, 3, 31)) == 2
    print problem019(dt.date(1901, 1, 1), dt.date(2000, 12, 31))
