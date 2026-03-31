def get_odd_collatz(n):
    odd_nums = []
    while n != 1:
        if n % 2 == 1:
            odd_nums.append(n)
            n = 3*n + 1
        else:
            n //= 2
    odd_nums.append(1)
    return sorted(set(odd_nums))