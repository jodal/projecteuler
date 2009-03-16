"""
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same
way?

From http://projecteuler.net/index.php?section=problems&id=28
"""

def problem028(n):
    odd_squares = [i ** 2 for i in range(n + 1) if i % 2 == 1]
    result = 0
    step = 0
    i = 1
    while i < n ** 2:
        i += step
        result += i
        if i in odd_squares:
            step += 2
    return result

if __name__ == '__main__':
    assert problem028(5) == 101
    print problem028(1001)
