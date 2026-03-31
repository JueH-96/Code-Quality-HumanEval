def eat(number, need, remaining):
    eaten_in_meal = min(need, remaining)
    total_eaten = number + eaten_in_meal
    remaining_left = remaining - eaten_in_meal
    return [total_eaten, remaining_left]