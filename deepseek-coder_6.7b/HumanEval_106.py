def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact


def sum_to_i(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


def f(n):
    result = []
    
    for i in range(n):
         if (i % 2) == 0:   # even index
             result.append(factorial(i))
         else:                # odd index
             result.append(sum_to_i(i))
                   
    return result
print(f(5))