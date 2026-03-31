def count_nums(arr):
    def sum_digits(n):
        return sum(map(int, str(abs(n))))

    return sum(sum_digits(i) > 0 for i in arr)