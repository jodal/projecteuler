# coding: utf-8
"""
Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20×20 grid?

From http://projecteuler.net/index.php?section=problems&id=15
"""

from eulerlib import ncr

def problem015(n):
    """
    The grid is a directed graph where all vertical lines have direction
    down and all horisontal lines have direction right.

    After quite a bit of staring on paper, i noticed the following:
    If you place the tip of Pascal's triangle in the destination node, the
    number at each node indicates how many possible paths from there to the
    destination. In other words, the number in the start node is the answer.
    """

    return ncr(n * 2, n)

if __name__ == '__main__':
    assert problem015(2) == 6
    assert problem015(3) == 20
    assert problem015(4) == 70
    print problem015(20)
