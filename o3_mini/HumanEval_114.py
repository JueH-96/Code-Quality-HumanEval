def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize current minimum sum and overall minimum sum
    current_min = nums[0]
    overall_min = nums[0]
    
    # Iterate from the second element
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        overall_min = min(overall_min, current_min)
        
    return overall_min