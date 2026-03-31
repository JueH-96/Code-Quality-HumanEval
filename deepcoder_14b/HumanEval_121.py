def solution(lst):
    total = 0
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 != 0:
            total += num
    return total