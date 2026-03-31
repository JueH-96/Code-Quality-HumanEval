def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    result = []
    template = "the number of odd elements in the string i of the input."
    for s in lst:
        count = sum(1 for ch in s if int(ch) % 2 == 1)
        count_str = str(count)
        result.append(template.replace("i", count_str))
    return result