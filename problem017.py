"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

From http://projecteuler.net/index.php?section=problems&id=17
"""

def problem017(n_min, n_max):
    sum = 0
    for n in range(n_min, n_max + 1):
        sum += len(in_words(n))
    return sum

wordmap = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
}

def in_words(number):
    assert 0 < number <= 1000
    words = []
    digits = map(int, list(str(number)))
    if len(digits) == 4:
        thousandth = digits.pop(0)
        words.append(wordmap.get(thousandth, ''))
        words.append('thousand')
    if len(digits) == 3:
        houndreth = digits.pop(0)
        if houndreth:
            words.append(wordmap.get(houndreth, ''))
            words.append('hundred')
        if digits[0] or digits[1]:
            words.append('and')
    if len(digits) == 2:
        tenth = digits.pop(0)
        if tenth:
            if tenth < 2:
                oneth = digits.pop(0)
                words.append(wordmap.get(tenth * 10 + oneth, ''))
            else:
                words.append(wordmap.get(tenth * 10, ''))
    if len(digits) == 1:
        words.append(wordmap.get(digits.pop(0), ''))
    return ''.join(words)

if __name__ == '__main__':
    assert in_words(1) == 'one'
    assert in_words(100) == 'onehundred'
    assert in_words(105) == 'onehundredandfive'
    assert in_words(115) == 'onehundredandfifteen'
    assert in_words(342) == 'threehundredandfortytwo'
    assert in_words(1000) == 'onethousand'
    assert problem017(1, 5) == 19
    print problem017(1, 1000)
