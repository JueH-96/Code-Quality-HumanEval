def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    # Check if the date string is empty
    if not date:
        return False

    # Make sure the date is in the format mm-dd-yyyy by splitting with '-'
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    month_str, day_str, year_str = parts
    
    # All parts must be digits and of appropriate lengths (could be 1 or 2 digits for month and day, and at least 4 digits for year, but no explicit check on year length is mentioned)
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False

    # Convert to integers
    month = int(month_str)
    day = int(day_str)
    # year is not used for determining day limits in this implementation
    # But conversion is done to ensure valid integer value is provided.
    year = int(year_str)

    # Check month validity
    if month < 1 or month > 12:
        return False

    # Define valid day ranges for each month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return False
    elif month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        # February is allowed up to 29 days regardless of leap year
        if day < 1 or day > 29:
            return False

    return True