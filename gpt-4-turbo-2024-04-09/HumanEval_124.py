def valid_date(date):
    if not date:
        return False
    
    # Check the format mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    
    # Split the date into components
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    month, day, year = parts
    
    # Check if month, day, year are numeric
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        return False
    
    month = int(month)
    day = int(day)
    year = int(year)
    
    # Check valid month
    if month < 1 or month > 12:
        return False
    
    # Check valid day based on month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return False
    elif month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    
    return True