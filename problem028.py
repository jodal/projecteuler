def problem028(n):
    odd_squares = [i ** 2 for i in range(n + 1) if i % 2 == 1]
    result = 0
    step = 0
    i = 1
    while i < n ** 2:
        i += step
        result += i
        if i in odd_squares:
            step += 2
    return result

if __name__ == '__main__':
    assert problem028(5) == 101
    print problem028(1001)
