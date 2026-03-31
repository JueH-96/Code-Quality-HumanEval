def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0  # or raise an error for empty input as per requirements

    current_min = overall_min = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        overall_min = min(overall_min, current_min)
    return overall_min