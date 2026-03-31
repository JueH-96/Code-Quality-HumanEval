def fizz_buzz(n: int):
    total = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            s = str(i)
            total += s.count('7')
    return total