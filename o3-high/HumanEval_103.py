def rounded_avg(n, m):
    """Compute the average of the integers from n through m (inclusive),
    round to the nearest integer using bankers rounding (round-half-to-even),
    and return its binary representation. If n > m, return -1.
    """
    if n > m:
        return -1

    total = n + m  # The average of consecutive integers is (n + m) / 2
    if total % 2 == 0:
        avg_int = total // 2
    else:
        lower = total // 2  # Represents the .5 case (k.5)
        avg_int = lower if lower % 2 == 0 else lower + 1  # Tie-to-even rounding

    return bin(avg_int)