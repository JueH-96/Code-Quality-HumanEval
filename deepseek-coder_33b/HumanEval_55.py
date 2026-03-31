def fib(n: int):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1 or n == 2:
        return 1
    else:
        prev_num = 1
        current_num = 1
        for i in range(3, n + 1):
            next_num = prev_num + current_num
            prev_num = current_num
            current_num = next_num
        return current_num