def do_algebra(operator, operand):
    expr = str(operand[0])
    for i in range(len(operator)):
        expr += operator[i] + str(operand[i + 1])
    return eval(expr)