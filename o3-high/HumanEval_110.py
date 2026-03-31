def exchange(lst1, lst2):
    """Determine whether it's possible to exchange elements between two lists so
    that all elements in lst1 become even numbers.

    An odd element in lst1 can be swapped with an even element from lst2. This
    is feasible if and only if the number of odd elements currently in lst1
    does not exceed the number of even elements available in lst2.

    Args:
        lst1 (list): First list of numbers.
        lst2 (list): Second list of numbers.

    Returns:
        str: "YES" if such an exchange is possible, otherwise "NO".
    """
    odd_in_lst1 = sum(1 for x in lst1 if x % 2)
    even_in_lst2 = sum(1 for x in lst2 if x % 2 == 0)
    return "YES" if odd_in_lst1 <= even_in_lst2 else "NO"