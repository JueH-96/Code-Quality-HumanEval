def get_odd_collatz(n):
    # Generate the Collatz sequence for n
    sequence = []
    current = n
    while True:
        sequence.append(current)
        if current == 1:
            break
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    
    # Collect all odd numbers in the sequence
    odds = [x for x in sequence if x % 2 != 0]
    
    # Return them sorted in increasing order
    return sorted(odds)