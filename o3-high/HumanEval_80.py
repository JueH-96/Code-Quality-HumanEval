def is_happy(s):
    """Check if the string s is 'happy'.

    A string is happy if:
    1. Its length is at least 3.
    2. Every substring of length 3 contains three distinct characters.

    Examples:
        is_happy("a")    -> False
        is_happy("aa")   -> False
        is_happy("abcd") -> True
        is_happy("aabb") -> False
        is_happy("adb")  -> True
        is_happy("xyy")  -> False
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return False
    return True