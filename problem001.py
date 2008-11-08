def problem1(max):
    return sum([i for i in range(max) if i % 3 == 0 or i % 5 == 0])

if __name__ == '__main__':
    assert problem1(10) == 23
    print problem1(1000)
