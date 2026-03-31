def specialFilter(nums):
    def is_first_last_odd(n):
        str_n = str(abs(n))
        return str_n[0] in '13579' and str_n[-1] in '13579'
    
    return sum(1 for num in nums if num > 10 and is_first_last_odd(num))