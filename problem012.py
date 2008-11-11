from eulerlib import triangle_numbers, get_divisors

def problem012(min_num_divisors):
    # XXX Too slow, speed up get_divisors
    for n in triangle_numbers():
        num_divisors = len(get_divisors(n))
        if num_divisors > min_num_divisors:
            return n
        if num_divisors > 100:
            print n, num_divisors

if __name__ == '__main__':
    assert problem012(5) == 28
    print problem012(500)
