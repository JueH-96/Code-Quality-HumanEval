def eat(number, need, remaining):
    eatable = min(need, remaining)
    total_eaten = number + eatable
    left = remaining - eatable
    return [total_eaten, left]