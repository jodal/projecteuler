def problem016(n):
    return sum(map(int, list(str(2 ** n))))

if __name__ == '__main__':
    assert problem016(15) == 26
    print problem016(1000)
