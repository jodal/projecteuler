"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

What is the 10001st prime number?

From http://projecteuler.net/index.php?section=problems&id=7
"""

from eulerlib import bruteforce_prime

def problem007(n):
    for i, prime in enumerate(bruteforce_prime()):
        if i + 1 == n:
            return prime

if __name__ == '__main__':
    assert problem007(6) == 13
    print problem007(10001)
