from eulerlib import ncr

def problem053(n_min, n_max, ncr_min):
    counter = 0
    for n in range(n_min, n_max + 1):
        for r in range(1, n + 1):
            x = ncr(n, r)
            if x > ncr_min:
                counter += 1
    return counter

if __name__ == '__main__':
    print problem053(1, 100, 1000000)
