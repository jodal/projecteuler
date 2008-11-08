from problem7 import bruteforce_prime

def problem3(n):
    for prime in bruteforce_prime():
        if n % prime == 0:
            n = n / prime
            if n == 1:
                return prime

if __name__ == '__main__':
    assert problem3(13195) == 29
    print problem3(600851475143)
