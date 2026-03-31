def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input."""
    
    def count_odd_digits(s):
        """Helper function to count odd digits in a string"""
        return sum(1 for digit in s if int(digit) % 2 != 0)
    
    result = []
    for i, string in enumerate(lst, start=1):
        odd_digits = count_odd_digits(string)
        # Replace 'i's with the number of odd digits and the index with the total count
        output_string = f"the number of odd elements {odd_digits}n the str{odd_digits}ng {odd_digits} of the {len(string)}nput."
        result.append(output_string)
    
    return result