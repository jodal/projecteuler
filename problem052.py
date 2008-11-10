from eulerlib import infinite_range

def problem052(multipliers):
    for x in infinite_range(start=1):
        candidate = True
        products = []
        for m in multipliers:
            product = list(str(x * m))
            product.sort()
            if len(products) == 0 or len(products) == products.count(product):
                products.append(product)
            else:
                candidate = False
                break
        if candidate:
            return x

if __name__ == '__main__':
    assert problem052([1, 2]) == 125874
    print problem052([1, 2, 3, 4, 5, 6])
