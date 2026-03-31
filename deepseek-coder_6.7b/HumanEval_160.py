def do_algebra(operator, operand):
    result = str(operand[0])
    for i in range(1, len(operand)):
        result += ' ' + operator[i-1] + ' ' + str(operand[i])
    
    return eval(result)