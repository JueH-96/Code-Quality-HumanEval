def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum and current sum to positive infinity
    min_sum = float('inf')
    
    # Iterate over all possible sub-arrays of nums
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            
            # Update the minimum sum if the current sum is smaller
            min_sum = min(min_sum, current_sum)
    
    return min_sum