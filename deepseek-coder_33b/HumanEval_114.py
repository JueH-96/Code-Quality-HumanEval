def minSubArraySum(nums):
    current_sum = nums[0]
    min_sum = nums[0]
    
    for num in nums[1:]:
        # If the current number is greater than the sum, then start from that number.
        if current_sum > 0:
            current_sum = num
        else:
            current_sum += num 
        
        min_sum = min(min_sum, current_sum)
    
    return min_sum