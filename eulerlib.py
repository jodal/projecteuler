import math

def fibonacci(max=None):
    a, b = 1, 1
    while max is None or a < max:
        yield a
        a, b = b, a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

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

def infinite_range(start=0, step=1):
    x = start
    while True:
        yield x
        x += step

def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def is_palindromic(n):
    return n == int(str(n)[::-1])

def triangle_numbers():
    sum = 0
    n = 1
    while True:
        sum += n
        yield sum
        n += 1

def get_divisors(n):
    divisors = []
    for i in xrange(n, 0, -1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    assert ncr(23, 10) == 1144066
    assert is_palindromic(121) == True
    assert is_palindromic(122) == False
