"""
The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.

Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... +
1000^(1000).

From http://projecteuler.net/index.php?section=problems&id=48
"""

def problem048(n):
    return str(sum([i ** i for i in range(1, n + 1)]))[-10:]

if __name__ == '__main__':
    assert problem048(10) == '0405071317'
    print problem048(1000)
