def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12.
       The number of days is not less than 1 or higher than 30 days for months 4,6,9,11.
       The number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy
    """
    if not date:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    month_str, day_str, year_str = parts

    if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4:
        return False
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False

    month = int(month_str)
    day = int(day_str)

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    else:  # month == 2
        if not (1 <= day <= 29):
            return False

    return True