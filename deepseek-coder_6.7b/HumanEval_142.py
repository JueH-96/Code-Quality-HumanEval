def sum_squares(lst):
    return sum([num**2 if i%3==0 and i%4<>0 else num**3 for i, num in enumerate(lst)])