def even_odd_palindrome(n):
    evens = []
    odds = []
    
    for num in range(1, n+1):
        str_num = str(num)
        if str_num == str_num[::-1]:  # Check if it's a palindrome.
            if len(str_num) % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
                
    return (len(evens), len(odds))