from eulerlib import factorial

def problem020(n):
    return sum(map(int, list(str(factorial(n)))))

if __name__ == '__main__':
    print problem020(100)
