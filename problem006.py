# coding: utf-8
"""
The sum of the squares of the first ten natural numbers is,

1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

From http://projecteuler.net/index.php?section=problems&id=6
"""

def problem006(min, max):
    sum_of_squares = sum([i**2 for i in range(min, max + 1)])
    square_of_sums = sum(range(min, max + 1)) ** 2
    return square_of_sums - sum_of_squares

if __name__ == '__main__':
    assert problem006(1, 10) == 2640
    print problem006(1, 100)
