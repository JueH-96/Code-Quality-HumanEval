def exchange(lst1, lst2):
    if sum([n % 2 == 0 for n in lst1]) == len(lst1):
        return "YES"
    
    odd_nums = [n % 2 != 0 for n in lst1]
    even_nums = [m % 2 == 0 for m in lst2]
    
    if any(odd_nums) and any(even_nums):
        return "YES"
    
    return "NO"