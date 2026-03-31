def sequence_value(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        dp = [0, 0, 1]  # Represents the first three terms (n=0,1,2)
        for i in range(3, n + 1):
            next_val = sum(dp[:i-1])  # Sum all elements except the last one
            dp.append(next_val)
        return dp[n]

# Example usage:
n = int(input())
print(sequence_value(n))