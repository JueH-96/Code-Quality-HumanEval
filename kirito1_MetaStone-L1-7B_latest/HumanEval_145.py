def points_and_sorting(nums):
    def digit_sum(x):
        return sum(int(d) for d in str(abs(x)))
    
    indexed_nums = [(digit_sum(num), idx, num) for idx, num in enumerate(nums)]
    sorted_nums = sorted(indexed_nums, key=lambda x: (x[0], x[1]))
    result = [num for (s, i, num) in sorted_nums]
    return result