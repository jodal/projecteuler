"""
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?

From http://projecteuler.net/index.php?section=problems&id=16
"""

def problem016(n):
    return sum(map(int, list(str(2 ** n))))

if __name__ == '__main__':
    assert problem016(15) == 26
    print problem016(1000)
