def is_perfect_cube(n):
    if n == 0:
        return True
    abs_n = abs(n)
    low = 1
    high = abs_n
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        if cube == abs_n:
            return True
        elif cube < abs_n:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Example usage:
n = int(input("Enter an integer: "))
if is_perfect_cube(n):
    print(f"{n} is a perfect cube.")
else:
    print(f"{n} is not a perfect cube.")