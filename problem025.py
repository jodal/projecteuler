from eulerlib import fibonacci

def problem025(n):
    for i, f in enumerate(fibonacci()):
        if len(str(f)) >= n:
            return i + 1

if __name__ == '__main__':
    assert problem025(3) == 12
    print problem025(1000)
