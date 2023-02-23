import math

student_grade = int(input('Enter student\'s grade here (type \'-1\' to quit): '))
number_grades = 0
passing_grades = 0

while student_grade != -1:
    if 70 <= student_grade <= 100:
        print('Passing grade.')
        number_grades += 1
        passing_grades += 1
        student_grade = int(input('Enter student\'s grade here (type \'-1\' to quit): '))

    elif 0 <= student_grade < 70:
        print('Not a passing grade.')
        number_grades += 1
        student_grade = int(input('Enter student\'s grade here (type \'-1\' to quit): '))

    else:
        print('Invalid grade inserted!')
        student_grade = int(input('Enter student\'s grade here (type \'-1\' to quit): '))

grades_percentage = int((passing_grades / number_grades) * 100)

print('You entered {} passing grades.'.format(passing_grades))
print('{:.1f}% of the valid grades inserted are passing.'.format(grades_percentage))
