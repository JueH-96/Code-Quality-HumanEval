def remove_repeats(numbers):
    from collections import defaultdict
    freq = defaultdict(int)
    for num in numbers:
        freq[num] += 1
    res = []
    for num in numbers:
        if freq[num] == 1:
            res.append(num)
    return res