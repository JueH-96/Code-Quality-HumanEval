def odd_count(lst):
    """Given a list of strings, where each string consists of only digits,
    return a list with each element being the sentence
    "the number of odd elements in the string i of the input."
    in which all occurrences of 'i' are replaced by the number of odd digits
    in that string.
    """
    result = []
    template = "the number of odd elements in the string i of the input."
    for s in lst:
        count_odds = sum(int(d) % 2 == 1 for d in s)
        replaced = template.replace('i', str(count_odds))
        result.append(replaced)
    return result