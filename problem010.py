from problem7 import sieve_prime

def problem10(max):
    prime_sum = 0
    for prime in sieve_prime(max=max):
        if prime < max:
            prime_sum += prime
        else:
            break
    return prime_sum

if __name__ == '__main__':
    assert problem10(10) == 17
    print problem10(2000000)
