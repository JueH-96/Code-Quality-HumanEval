def get_odd_collatz(n):
    def collatz(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    result = []
    while n != 1:
        if n % 2 != 0:
            result.append(n)
        n = collatz(n)
    
    result.append(1) # appending 1 at the end as it's a part of collatz sequence
    return sorted(result[::2]) # returning every second element starting from first which are odd numbers in the sequence