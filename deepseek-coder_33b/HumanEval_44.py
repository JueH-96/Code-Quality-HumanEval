def change_base(x: int, base: int):
    if x == 0:
        return '0'
    nums = []
    while x:
        x, r = divmod(x, base)
        nums.append(str(r))
    return ''.join(reversed(nums))