def count_nums(arr):
    def sum_of_digits(n):
        return sum(int(d) for d in str(abs(n))) - (n < 0 and int(str(n)[1:]) > 9) * 2 * int(str(n)[1:])

    return sum(sum_of_digits(num) > 0 for num in arr)