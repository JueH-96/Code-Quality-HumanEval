def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # Use eval function with a generated expression string
    # First, convert operators to their corresponding Python symbols
    op_map = {
        '+': '+',
        '-': '-',
        '*': '*',
        '//': '//' if all(o >= 0 for o in operand) else '/',
        '**': '**'
    }
    
    # Generate the expression string
    expr = str(operand[0])
    for op, num in zip(operator, operand[1:]):
        expr += f" {op_map[op]} {num}"
        
    # Evaluate and return the result
    return eval(expr)