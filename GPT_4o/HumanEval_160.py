def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.
    """
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += f" {operator[i]} {operand[i + 1]}"
    return eval(expression)