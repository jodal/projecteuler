def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def problem191(n):
    num_possible_combinations = 3 ** n
    # TODO
    return 0

if __name__ == '__main__':
    assert problem191(4) == 43
    print problem191(30)
