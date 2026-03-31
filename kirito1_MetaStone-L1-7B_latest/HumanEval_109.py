def canRotateToSorted(arr):
    n = len(arr)
    for i in range(n):
        candidate = arr[i:] + arr[:i]
        # Check if the candidate is sorted
        is_sorted = True
        for j in range(len(candidate) - 1):
            if candidate[j] > candidate[j+1]:
                is_sorted = False
                break
        if is_sorted:
            return True
    return False

# Example usage:
arr = [3, 4, 5, 1, 2]
print(canRotateToSorted(arr))  # Output: True