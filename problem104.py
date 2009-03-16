# coding: utf-8
"""
The Fibonacci sequence is defined by the recurrence relation:

    F_(n) = F_(n−1) + F_(n−2), where F_(1) = 1 and F_(2) = 1.

It turns out that F_(541), which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F_(2749), which contains 575
digits, is the first Fibonacci number for which the first nine digits are 1-9
pandigital.

Given that F_(k) is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.

From http://projecteuler.net/index.php?section=problems&id=104
"""

from eulerlib import fibonacci

def problem104(n, first=False, last=False):
    """XXX: Works, but have no solution after 16h"""

    assert first or last
    digits = set(map(str, range(1, n + 1)))
    for i, f in enumerate(fibonacci()):
        f = str(f)
        if first and not set(f[:n]) == digits:
            continue
        if last and not set(f[-n:]) == digits:
            continue
        return i + 1

if __name__ == '__main__':
    assert problem104(9, last=True) == 541
    assert problem104(9, first=True) == 2749
    print problem104(9, first=True, last=True)
