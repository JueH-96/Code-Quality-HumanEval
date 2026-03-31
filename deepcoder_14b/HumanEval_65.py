def rotate_right(s: str, shift: int = 1) -> str:
    if not s or len(s) == 0:
        return s
    n = len(s)
    k = shift % n
    if k == 0:
        return s
    return s[-k:] + s[:-k]