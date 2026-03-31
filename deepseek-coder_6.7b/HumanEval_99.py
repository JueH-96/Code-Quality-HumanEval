def closest_integer(value):
    num = float(value)
    floor_num = int(num // 1)
    ceil_num = floor_num if num % 1 < 0.5 else floor_num + 1
    return max(ceil_num, -floor_num)

# Test cases
print(closest_integer("10")) # should return 10
print(closest_integer("15.3")) # should return 15
print(closest_integer("-14.5")) # should return -15
print(closest_integer("14.5")) # should return 15