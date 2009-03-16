"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

From http://projecteuler.net/index.php?section=problems&id=9
"""

def problem009(sum):
    c_min = sum // 3
    for c in range(c_min, sum):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == sum and is_pythagorean_triplet(a, b, c):
                    return a * b * c

def is_pythagorean_triplet(a, b, c):
    assert 0 < a < b < c
    return (a ** 2) + (b ** 2) == (c ** 2)

if __name__ == '__main__':
    print problem009(1000)
