def sort_by_ones(arr):
    def count_ones(n):
        return bin(abs(n)).count('1')
    return sorted(arr, key=lambda x: (count_ones(x), x))