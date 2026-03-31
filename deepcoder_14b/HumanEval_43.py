def pairs_sum_to_zero(l):
    seen = set()
    for num in l:
        if num == 0:
            if 0 in seen:
                return True
            else:
                seen.add(num)
        else:
            if -num in seen:
                return True
            else:
                seen.add(num)
    return False