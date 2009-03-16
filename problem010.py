"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

From http://projecteuler.net/index.php?section=problems&id=10
"""

from eulerlib import sieve_prime

def problem010(max):
    prime_sum = 0
    for prime in sieve_prime(max=max):
        if prime < max:
            prime_sum += prime
        else:
            break
    return prime_sum

if __name__ == '__main__':
    assert problem010(10) == 17
    print problem010(2000000)
