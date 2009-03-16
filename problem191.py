"""
A particular school offers cash rewards to children with good attendance and
punctuality. If they are absent for three consecutive days or late on more than
one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of
L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be
formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?

From http://projecteuler.net/index.php?section=problems&id=191
"""

from eulerlib import factorial

def problem191(n):
    num_possible_combinations = 3 ** n
    # TODO
    return 0

if __name__ == '__main__':
    assert problem191(4) == 43
    print problem191(30)
