# coding: utf-8
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

From http://projecteuler.net/index.php?section=problems&id=14
"""

def problem014(n_max):
    max_seq_len = 0
    max_seq_start = None
    for seq_start in xrange(n_max):
        seq_len = get_seq_len(seq_start)
        if seq_len > max_seq_len:
            max_seq_len = seq_len
            max_seq_start = seq_start
    return max_seq_start

cache = {}

def get_seq_len(start):
    result = 1
    n = start
    while n > 1:
        if n in cache:
            result += cache[n]
            break
        else:
            result += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    if start not in cache:
        cache[start] = result
    return result

if __name__ == '__main__':
    assert get_seq_len(13) == 10
    print problem014(1000000)
