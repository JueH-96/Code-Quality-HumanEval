def exchange(lst1, lst2):
    total_evens = sum(1 for num in lst1 if num % 2 == 0) + sum(1 for num in lst2 if num % 2 == 0)
    return "YES" if total_evens >= len(lst1) else "NO"