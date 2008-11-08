def fib(max):
    a, b = 0, 1
    while b < max:
        yield b
	a, b = b, a + b

def problem2(max):
    return sum([i for i in fib(max) if i % 2 == 0])

if __name__ == '__main__':
    print problem2(4000000)



