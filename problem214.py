# coding: utf-8
"""
Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the
number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

By iterating φ, each positive integer generates a decreasing chain of numbers
ending in 1. E.g. if we start with 5 the sequence 5,4,2,1 is generated.

Here is a listing of all chains with length 4:

5,4,2,1
7,6,2,1
8,4,2,1
9,6,2,1
10,4,2,1
12,4,2,1
14,6,2,1
18,6,2,1

Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40000000 which generate a chain of
length 25?

From http://projecteuler.net/index.php?section=problems&id=214
"""

from eulerlib import sieve_prime, gcd

def problem214(chain_len, prime_max):
    # FIXME Too slow
    result = 0
    for prime in sieve_prime(max=prime_max):
        print prime
        if len(totient_chain(prime)) == chain_len:
            result += prime
    return result

CACHE_ENABLED = False
cache = {}

def totient_chain(n):
    result = [n]
    while result[-1] != 1:
        if CACHE_ENABLED and result[-1] in cache:
            result += cache[result[-1]][1:]
        else:
            result.append(totient(result[-1]))
    if CACHE_ENABLED and n not in cache:
        cache[n] = result
    return result

def totient(n):
    result = 0
    for k in xrange(1, n + 1):
        if gcd(k, n) == 1:
            result += 1
    return result

if __name__ == '__main__':
    assert problem214(4, 20) == 12
    print problem214(25, 40000000)
