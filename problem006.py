def problem6(min, max):
    sum_of_squares = sum([i**2 for i in range(min, max + 1)])
    square_of_sums = sum(range(min, max + 1)) ** 2
    return square_of_sums - sum_of_squares

if __name__ == '__main__':
    assert problem6(1, 10) == 2640
    print problem6(1, 100)
