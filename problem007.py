import math

def sieve_prime(max=100000000):
    candidates = range(max)
    for candidate in candidates:
        if candidate is None or candidate < 2:
            continue
        else:
            yield candidate
            for j in range(candidate, max, candidate):
                candidates[j] = None

def bruteforce_prime():
    yield 2
    i = 3
    while True:
        is_prime = True
        for j in range(2, i / 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
        i += 2

def problem7(n):
    for i, prime in enumerate(bruteforce_prime()):
        if i + 1 == n:
            return prime

if __name__ == '__main__':
    assert problem7(6) == 13
    print problem7(10001)
