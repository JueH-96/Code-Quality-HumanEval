def add_elements(arr, k):
    return sum(n for n in arr[:k] if n < 100)