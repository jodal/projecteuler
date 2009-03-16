"""
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7^(th) triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?

From http://projecteuler.net/index.php?section=problems&id=12
"""

from eulerlib import triangle_numbers, get_divisors

def problem012(min_num_divisors):
    # XXX Too slow, speed up get_divisors
    for n in triangle_numbers():
        num_divisors = len(get_divisors(n))
        if num_divisors > min_num_divisors:
            return n
        if num_divisors > 100:
            print n, num_divisors

if __name__ == '__main__':
    assert problem012(5) == 28
    print problem012(500)
