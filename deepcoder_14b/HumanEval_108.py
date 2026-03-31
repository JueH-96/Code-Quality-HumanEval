def count_nums(arr):
    count = 0
    for num in arr:
        if num == 0:
            continue
        total = 0
        if num < 0:
            s = str(abs(num))
            for i, c in enumerate(s):
                digit = int(c)
                if i == 0:
                    total -= digit
                else:
                    total += digit
        else:
            for c in str(num):
                total += int(c)
        if total > 0:
            count += 1
    return count

# Example usage:
print(count_nums([-1, 11, -11]))  # Output: 1
print(count_nums([1, 1, 2]))      # Output: 3