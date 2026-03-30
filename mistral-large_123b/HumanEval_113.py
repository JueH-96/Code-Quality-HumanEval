def odd_count(lst):
    result = []
    for s in lst:
        count_odd = sum(1 for char in s if int(char) % 2 != 0)
        modified_string = f"the number of odd elements {count_odd}n the str{count_odd}ng {count_odd} of the {count_odd}nput."
        result.append(modified_string)
    return result