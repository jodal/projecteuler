def problem5(max):
    i = max
    while True:
        for j in xrange(max, 1, -1):
            if i % j == 0:
                if j == 2:
                    return i
                continue
            else:
                i += max
                break

if __name__ == '__main__':
    print problem5(20)
