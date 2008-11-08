def problem048(n):
    return str(sum([i ** i for i in range(1, n + 1)]))[-10:]

if __name__ == '__main__':
    assert problem048(10) == '0405071317'
    print problem048(1000)
