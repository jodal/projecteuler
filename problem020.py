# coding: utf-8
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

Find the sum of the digits in the number 100!

From http://projecteuler.net/index.php?section=problems&id=20
"""

from eulerlib import factorial

def problem020(n):
    return sum(map(int, list(str(factorial(n)))))

if __name__ == '__main__':
    print problem020(100)
