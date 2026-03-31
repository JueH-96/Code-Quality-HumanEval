def order_by_points(nums):
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))

    nums_with_index = [(i, num) for i, num in enumerate(nums)]
    sorted_nums = sorted(nums_with_index, key=lambda x: (digit_sum(x[1]), x[0]))
    return [num for _, num in sorted_nums]