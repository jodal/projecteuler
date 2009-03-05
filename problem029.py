def problem029(a_start, a_stop, b_start, b_stop):
    combinations = set()
    for a in range(a_start, a_stop + 1):
        for b in range(b_start, b_stop + 1):
            combinations.add(a ** b)
    return len(combinations)

if __name__ == '__main__':
    assert problem029(2, 5, 2, 5) == 15
    print problem029(2, 100, 2, 100)
