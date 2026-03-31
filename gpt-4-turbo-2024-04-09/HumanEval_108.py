def count_nums(arr):
    def sum_of_digits(n):
        if n < 0:
            return -int(str(n)[1]) + sum(int(d) for d in str(n)[2:])
        else:
            return sum(int(d) for d in str(n))
    
    return sum(1 for x in arr if sum_of_digits(x) > 0)