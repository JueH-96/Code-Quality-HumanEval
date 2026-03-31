def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read input intervals
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = max(a[0], b[0])
e = min(a[1], b[1])

if e > s:
    length = e - s
    if is_prime(length):
        print("YES")
    else:
        print("NO")
else:
    print("NO")