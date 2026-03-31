def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges
    that are distributed in a basket of fruit this basket contains
    apples, oranges, and mango fruits. Given the string that represents the total number of
    the oranges and apples and an integer that represent the total number of the fruits
    in the basket return the number of the mango fruits in the basket.
    """
    apple_index = s.find("apples") - 2
    orange_index = s.find("oranges") - 2
    apples = int(s[0:apple_index])
    oranges = int(s[apple_index + 6:orange_index])
    mangos = n - apples - oranges
    return mangos