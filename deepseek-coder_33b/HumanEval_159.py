def eat(number, need, remaining):
    if remaining >= need - number:
        total_eaten = number + need
        remaining_carrots = remaining - (need - number)
    else:
        total_eaten = number + remaining
        remaining_carrots = 0
        
    return [total_eaten, remaining_carrots]