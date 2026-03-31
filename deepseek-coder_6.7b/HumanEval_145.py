def order_by_points(nums):
    # Define a helper function that calculates sum of digits
    def digit_sum(n):
        return sum([int(i) for i in str(abs(n))])
    
    # Use Python's built-in 'sort' method with a custom key. 
    # First, by absolute value (for stability), then by original index.
    nums.sort(key=lambda x: (digit_sum(x), nums.index(x)))
    
    return nums