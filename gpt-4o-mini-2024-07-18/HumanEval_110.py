def exchange(lst1, lst2):
    even_needed = sum(1 for x in lst1 if x % 2 != 0)
    even_available = sum(1 for x in lst2 if x % 2 == 0)
    
    if even_needed <= even_available:
        return "YES"
    else:
        return "NO"