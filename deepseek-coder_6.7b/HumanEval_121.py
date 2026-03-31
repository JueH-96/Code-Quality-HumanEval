def solution(lst):
    return sum(el for i, el in enumerate(lst) if i % 2 == 0 and el % 2 != 0)