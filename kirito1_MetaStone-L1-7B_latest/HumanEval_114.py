def find_min_subarray_sum(nums):
    if not nums:
        return None  # Assuming the problem guarantees non-empty input
    
    min_current = nums[0]
    min_total = nums[0]
    
    for num in nums[1:]:
        option_start_new = num
        option_include_prev = min_current + num
        
        new_min = min(option_start_new, option_include_prev)
        
        if new_min < min_total:
            min_total = new_min
        
        min_current = new_min
    
    return min_total