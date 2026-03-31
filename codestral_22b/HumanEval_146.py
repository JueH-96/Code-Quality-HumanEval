def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and both
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def is_special(num):
        return num > 10 and abs(num) % 10 in {1, 3, 5, 7, 9} and int(str(abs(num))[0]) in {1, 3, 5, 7, 9}
    return sum(is_special(num) for num in nums)