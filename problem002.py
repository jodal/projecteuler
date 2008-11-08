from eulerlib import fibonacci

def problem2(max):
    return sum([i for i in fibonacci(max) if i % 2 == 0])

if __name__ == '__main__':
    print problem2(4000000)



