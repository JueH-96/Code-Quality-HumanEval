def eat(number, need, remaining):
    """
    You're a hungry rabbit and have already eaten `number` carrots. You still need
    to eat `need` more. There are `remaining` carrots in stock.
    
    Returns a list:
      [ total carrots eaten after eating, carrots left in stock ]
    
    If there aren't enough carrots left, you eat all that remain but do not meet
    your needed amount.
    """
    # How many carrots can actually be eaten now
    can_eat = min(need, remaining)
    
    # Update totals
    total_eaten = number + can_eat
    left_in_stock = remaining - can_eat
    
    return [total_eaten, left_in_stock]