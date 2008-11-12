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
