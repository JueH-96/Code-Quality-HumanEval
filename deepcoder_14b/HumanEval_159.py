def eat(number, need, remaining):
    amount_eaten = min(need, remaining)
    total = number + amount_eaten
    rem_left = remaining - amount_eaten
    return [total, rem_left]