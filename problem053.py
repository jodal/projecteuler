# coding: utf-8
"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^(5)C_(3) = 10.

In general,

^(n)C_(r) = n! / (r!(n−r)!),

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: ^(23)C_(10) =
1144066.

How many, not necessarily distinct, values of  ^(n)C_(r), for 1 ≤ n ≤ 100, are
greater than one-million?

From http://projecteuler.net/index.php?section=problems&id=53
"""

from eulerlib import ncr

def problem053(n_min, n_max, ncr_min):
    counter = 0
    for n in range(n_min, n_max + 1):
        for r in range(1, n + 1):
            x = ncr(n, r)
            if x > ncr_min:
                counter += 1
    return counter

if __name__ == '__main__':
    print problem053(1, 100, 1000000)
