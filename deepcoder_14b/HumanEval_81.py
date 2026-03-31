def calculate_grade(gpa):
    grades = [
        (4.0, 'A+'),
        (3.7, 'A'),
        (3.3, 'A-'),
        (3.0, 'B+'),
        (2.7, 'B'),
        (2.3, 'B-'),
        (2.0, 'C+'),
        (1.7, 'C'),
        (1.3, 'C-'),
        (1.0, 'D+'),
        (0.7, 'D'),
        (0.5, 'D-'),
        (0.0, 'F')
    ]
    for cutoff, grade in grades:
        if gpa >= cutoff:
            return grade
    return 'F'  # This line is theoretically unreachable

# Example usage:
gpa = float(input("Enter your GPA: "))
print(f"Your grade is {calculate_grade(gpa)}")