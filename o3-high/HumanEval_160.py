def do_algebra(operator, operand):
    """
    Evaluate an algebraic expression defined by a list of operators and operands.

    Parameters:
    operator (list of str): List containing algebraic operators as strings.
    operand (list of int): List containing integer operands.

    Returns:
    int: The result of the evaluated algebraic expression.
    """
    if not operator or len(operand) != len(operator) + 1:
        raise ValueError("Invalid input: operators and operands counts do not match the requirement.")

    # Build the expression string
    expr_parts = [str(operand[0])]
    for op, val in zip(operator, operand[1:]):
        expr_parts.append(op)
        expr_parts.append(str(val))
    expression = ' '.join(expr_parts)

    # Safely evaluate the expression
    return eval(expression, {"__builtins__": None}, {})