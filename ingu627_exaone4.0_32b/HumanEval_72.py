def will_it_fly(q, w):
    # Check if the list is a palindrome
    is_palindrome = q == q[::-1]
    # Check if the sum of elements is <= w
    sum_leq_w = sum(q) <= w
    # Return True only if both conditions are met
    return is_palindrome and sum_leq_w