"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?

From http://projecteuler.net/index.php?section=problems&id=5
"""

def problem005(max):
    i = max
    while True:
        for j in xrange(max, 1, -1):
            if i % j == 0:
                if j == 2:
                    return i
                continue
            else:
                i += max
                break

if __name__ == '__main__':
    assert problem005(10) == 2520
    print problem005(20)
