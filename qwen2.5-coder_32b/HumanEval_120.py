def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    if k == 0:
        return []
    # Find the k largest elements
    max_k_elements = heapq.nlargest(k, arr)
    # Return them sorted
    return sorted(max_k_elements)