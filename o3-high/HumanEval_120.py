def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    if k <= 0:
        return []
    from heapq import nlargest
    top_k = nlargest(k, arr)
    top_k.sort()
    return top_k