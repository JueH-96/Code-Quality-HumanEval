def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_of_numbers = 0
    product_of_numbers = 1
    
    for num in numbers:
        sum_of_numbers += num
        product_of_numbers *= num
    
    if not numbers:
        return 0, 1
    else:
        return sum_of_numbers, product_of_numbers