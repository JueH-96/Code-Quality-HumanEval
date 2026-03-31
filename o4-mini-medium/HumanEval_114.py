def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        raise ValueError("nums must contain at least one element")
    current_min = min_sum = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)
    return min_sum