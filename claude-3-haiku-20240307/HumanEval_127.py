def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals intersect
    if start1 > end2 or start2 > end1:
        return "NO"

    # Calculate the intersection
    start = max(start1, start2)
    end = min(end1, end2)
    length = end - start + 1

    # Check if the length of the intersection is a prime number
    if length > 1:
        for i in range(2, int(length ** 0.5) + 1):
            if length % i == 0:
                return "NO"
        return "YES"
    else:
        return "NO"