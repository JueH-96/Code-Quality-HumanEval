import re

def valid_date(date):
    """Validate a date string in the mm-dd-yyyy format."""
    # Rule 1: non-empty string
    if not isinstance(date, str) or not date:
        return False

    # Rule 4: must match exactly mm-dd-yyyy with two digits for m & d
    match = re.fullmatch(r'(\d{2})-(\d{2})-(\d{4})', date)
    if not match:
        return False

    month, day, year = map(int, match.groups())

    # Rule 3: month range
    if not 1 <= month <= 12:
        return False

    # Rule 2: day range depending on month
    if day < 1:
        return False

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return day <= 31
    elif month in {4, 6, 9, 11}:
        return day <= 30
    else:  # February
        return day <= 29