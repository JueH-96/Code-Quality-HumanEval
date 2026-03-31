def is_valid_date(date):
    if not date:
        return False
    
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    mm_str, dd_str, yyyy_str = parts[0], parts[1], parts[2]
    
    # Check each part's length
    if len(mm_str)!=2 or len(dd_str)!=2 or len(yyyy_str)!=4:
        return False
    
    # Ensure all characters in month and day are digits
    if not (mm_str.isdigit() and dd_str.isdigit()):
        return False
    
    try:
        month = int(mm_str)
        day = int(dd_str)
        year = int(yyyy_str)  # Year is converted but not further validated beyond being four digits
    except ValueError:
        return False
    
    if month < 1 or month > 12:
        return False
    
    # Determine maximum days based on the month
    if month == 2:
        max_days = 29
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31
    
    if day < 1 or day > max_days:
        return False
    
    return True