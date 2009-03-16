"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

From http://projecteuler.net/index.php?section=problems&id=3
"""

from eulerlib import bruteforce_prime

def problem003(n):
    for prime in bruteforce_prime():
        if n % prime == 0:
            n = n / prime
            if n == 1:
                return prime

if __name__ == '__main__':
    assert problem003(13195) == 29
    print problem003(600851475143)
