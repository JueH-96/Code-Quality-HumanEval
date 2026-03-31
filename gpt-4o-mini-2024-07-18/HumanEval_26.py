def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = {}
    result = []
    for number in numbers:
        if number in seen:
            seen[number] += 1
        else:
            seen[number] = 1
    for number in numbers:
        if seen[number] == 1:
            result.append(number)
    return result