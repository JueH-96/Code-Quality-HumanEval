def can_make_all_even(lst1, lst2):
    # Count the number of odd numbers in lst1
    count_odds_lst1 = sum(1 for x in lst1 if x % 2 != 0)
    
    # Calculate total even numbers available (from both lists)
    evens_lst1 = len(lst1) - count_odds_lst1
    odds_lst2 = sum(1 for x in lst2 if x % 2 != 0)
    evens_lst2 = len(lst2) - odds_lst2
    
    total_evens = evens_lst1 + evens_lst2
    
    # Check if we have enough even numbers to convert all odds in lst1
    return total_evens >= count_odds_lst1

# Example usage:
# lst1 = [3, 5]
# lst2 = [4, 6]
# print(can_make_all_even(lst1, lst2))  # Output: True