def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        raise ValueError("Input list must not be empty")
    current_min = overall_min = nums[0]
    for n in nums[1:]:
        current_min = min(n, current_min + n)
        overall_min = min(overall_min, current_min)
    return overall_min