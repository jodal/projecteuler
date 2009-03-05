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
