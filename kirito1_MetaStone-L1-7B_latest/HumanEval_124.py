def valid_date(date):
    if len(date) != 10:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False
    mm_str, dd_str, yyyy_str = parts[0], parts[1], parts[2]

    if (len(mm_str) != 2 or 
        len(dd_str) != 2 or
        len(yyyy_str) != 4):
        return False

    if not mm_str.isdigit() or not dd_str.isdigit() or not yyyy_str.isdigit():
        return False

    try:
        mm = int(mm_str)
        dd = int(dd_str)
        yyyy = int(yyyy_str)
    except ValueError:
        return False

    if mm < 1 or mm > 12:
        return False

    is_leap_year = (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0)

    if mm == 2:
        max_d = 29 if is_leap_year else 28
    else:
        if mm in [4, 6, 9, 11]:
            max_d = 30
        else:
            max_d = 31

    return dd >= 1 and dd <= max_d