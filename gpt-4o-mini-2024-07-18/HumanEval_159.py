def eat(number, need, remaining):
    if remaining >= need:
        total_eaten = number + need
        left = remaining - need
    else:
        total_eaten = number + remaining
        left = 0
    return [total_eaten, left]