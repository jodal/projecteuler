def palindrome():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            straight = list(str(product))
            reverse = list(str(product))
            reverse.reverse()
            if straight == reverse and product > max:
                max = product
    return max

if __name__ == '__main__':
    print palindrome()
