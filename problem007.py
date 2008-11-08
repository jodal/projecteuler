from eulerlib import bruteforce_prime

def problem7(n):
    for i, prime in enumerate(bruteforce_prime()):
        if i + 1 == n:
            return prime

if __name__ == '__main__':
    assert problem7(6) == 13
    print problem7(10001)
