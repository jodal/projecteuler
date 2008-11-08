from eulerlib import fibonacci

def problem104(n, first=False, last=False):
    # XXX: Works, but have no solution after 16h
    assert first or last
    digits = set(map(str, range(1, n + 1)))
    for i, f in enumerate(fibonacci()):
        f = str(f)
        if first and not set(f[:n]) == digits:
            continue
        if last and not set(f[-n:]) == digits:
            continue
        return i + 1

if __name__ == '__main__':
    assert problem104(9, last=True) == 541
    assert problem104(9, first=True) == 2749
    print problem104(9, first=True, last=True)
