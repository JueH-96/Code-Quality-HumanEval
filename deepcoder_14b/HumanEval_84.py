def sum_binary_digits(n):
    if n == 0:
        return "0"
    s = str(n)
    sum_d = sum(int(d) for d in s)
    return bin(sum_d)[2:]