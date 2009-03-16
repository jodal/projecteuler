"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

From http://projecteuler.net/index.php?section=problems&id=1
"""

def problem001(max):
    return sum([i for i in range(max) if i % 3 == 0 or i % 5 == 0])

if __name__ == '__main__':
    assert problem001(10) == 23
    print problem001(1000)
