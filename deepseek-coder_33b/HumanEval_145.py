def order_by_points(nums):
    def sum_of_digits(n):
        return sum(map(int, str(abs(n))))

    return sorted(range(len(nums)), key=lambda i: (sum_of_digits(nums[i]), i))