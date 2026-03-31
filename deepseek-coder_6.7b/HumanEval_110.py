def exchange(lst1, lst2):
    odd_in_lst1 = [n for n in lst1 if n % 2 != 0]
    even_in_lst2 = [n for n in lst2 if n % 2 == 0]
    
    if len(odd_in_lst1) > len(even_in_lst2):
        return "NO"
    else:
        return "YES"