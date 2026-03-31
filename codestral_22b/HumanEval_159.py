def eat(number, need, remaining):
    """
    You're a hungry rabbit...
    """
    if need <= remaining:
        number += need
        remaining -= need
    else:
        number += remaining
        remaining = 0
    return [number, remaining]