def valid_date(date):
    import re
    if not date:  # Check if the date string is empty
        return False

    # Regular expression to match the format mm-dd-yyyy
    pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$"
    match = re.match(pattern, date)
    if not match:  # Check if the format is correct
        return False

    month, day, year = map(int, date.split('-'))

    # Validate month range
    if month < 1 or month > 12:
        return False

    # Validate day range for each month
    if (month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31)) or \
       (month in [4, 6, 9, 11] and (day < 1 or day > 30)) or \
       (month == 2 and (day < 1 or day > 29)):
        return False

    # If all checks pass, the date is valid
    return True