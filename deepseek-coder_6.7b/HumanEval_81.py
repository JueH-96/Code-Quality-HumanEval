def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |  Letter grade
             4.0            A+
            >3.7            A 
            >3.3            A- 
            >3.0            B+
            >2.7            B 
            >2.3            B-
            >2.0            C+
            >1.7            C
            >1.3            C-
            >1.0            D+
            >0.7            D
            >0.0            E
    
    Example: numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """  
    letterGrades = []
    for gpa in grades:
        if gpa == 4.0:
            letterGrades.append('A+')
        elif gpa > 3.7:
            letterGrades.append('A')
        elif gpa > 3.3:
            letterGrades.append('A-')
        elif gpa >= 3.0:
            letterGrades.append('B+')
        elif gpa >= 2.7:
            letterGrades.append('B')
        elif gpa >= 2.3:
            letterGrades.append('B-')
        elif gpa >= 2.0:
            letterGrades.append('C+')
        elif gpa >= 1.7:
            letterGrades.append('C')
        elif gpa >= 1.3:
            letterGrades.append('C-')
        elif gpa >= 1.0:
            letterGrades.append('D+')
        elif gpa >= 0.7:
            letterGrades.append('D')
        elif gpa > 0.0:
            letterGrades.append('D-')
        else:
            letterGrades.append('E')
    return letterGrades