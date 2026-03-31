def eat(number, need, remaining):
    total_eaten = min(number + need, remaining)
    remaining_carrots = remaining - total_eaten
    return [total_eaten, remaining_carrots]