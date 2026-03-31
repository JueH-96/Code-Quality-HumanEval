def specialFilter(nums):
    def check_condition(n):
        str_n = str(abs(n))
        return n > 10 and len(str_n) > 1 and int(str_n[0]) % 2 != 0 and int(str_n[-1]) % 2 != 0
    return sum(check_condition(num) for num in nums)