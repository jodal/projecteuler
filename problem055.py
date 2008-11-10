from eulerlib import is_palindromic

def problem055(max_n, max_iterations):
    counter = 0
    for n in range(1, max_n + 1):
        if is_lychrel(n, max_iterations):
            counter += 1
    return counter

def is_lychrel(n, max_iterations):
    for i in range(max_iterations):
        n += int(str(n)[::-1])
        if is_palindromic(n):
            return False
    return True

if __name__ == '__main__':
    assert is_lychrel(349, 2) == True
    assert is_lychrel(349, 3) == False
    assert is_lychrel(10677, 52) == True
    assert is_lychrel(10677, 53) == False
    print problem055(10000, 50)
