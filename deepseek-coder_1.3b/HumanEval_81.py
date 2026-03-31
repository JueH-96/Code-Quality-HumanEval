def numerical_letter_grade(grades):
    return ['A+', 'B-', 'C-', 'D'] if g >= 9 and (g < 10 or m == '.') else \
           ['F' for g in grades[::]] # default case: fail all subjects, i.e., no mapping