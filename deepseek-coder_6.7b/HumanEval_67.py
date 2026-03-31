def fruit_distribution(s,n):
    num_apples = int(s.split(' ')[0])
    num_oranges = int(s.split('and')[1].split(' ')[1])
    return n - num_apples - num_oranges