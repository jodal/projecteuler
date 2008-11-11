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
