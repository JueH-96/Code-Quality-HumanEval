def is_equal_to_sum_even(n):
    if n < 10 or n % 2 != 0:
        return False
    for i in range(2, n//2+1, 2):
        if is_equal_to_sum_even(i) and is_equal_to_sum_even(n-i):
            return True
    return False
```