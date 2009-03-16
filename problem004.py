# coding: utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

From http://projecteuler.net/index.php?section=problems&id=4
"""

from eulerlib import is_palindromic

def problem004(min, max):
    max = 0
    for i in range(min, max + 1):
        for j in range(min, max + 1):
            product = i * j
            if is_palindromic(product) and product > max:
                max = product
    return max

if __name__ == '__main__':
    print problem004(100, 999)
