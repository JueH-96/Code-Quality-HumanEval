def count_nums(arr):
    return len([x for x in arr if sum(int(digit) for digit in str(abs(x))) > 0])