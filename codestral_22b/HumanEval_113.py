def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        num_odds = sum(int(d) % 2 == 1 for d in s)
        sentence = f"the number of odd elements {num_odds}n the str{num_odds}ng {i+1} of the {i+1}nput."
        result.append(sentence)
    return result