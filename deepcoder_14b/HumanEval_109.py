def generate_rotations(arr):
    n = len(arr)
    return [arr[-k:] + arr[:-k] for k in range(n)]