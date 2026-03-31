def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    overall_min = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        overall_min = min(overall_min, current_sum)
        
    return overall_min