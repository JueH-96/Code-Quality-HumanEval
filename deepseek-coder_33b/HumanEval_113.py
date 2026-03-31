def odd_count(lst):
    result = []
    for i in lst:
        count = 0
        for c in i:
            if int(c) % 2 != 0:
                count += 1
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, count, count, count))
    return result