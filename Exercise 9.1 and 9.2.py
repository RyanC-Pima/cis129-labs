# Exercise 9.1
# Ryan Calles
# CIS 129
# Class average program with sentinel-controlled iteration and grade storage to plain text file

# initialization phase
total = 0  # sum of grades
grade_counter = 0  # number of grades entered

with open('grades.txt', mode='w') as grades:  # Open file for appending grades

    # processing phase
    grade = int(input('Enter grade, -1 to end: '))  # get one grade

    while grade != -1:
        total += grade
        grade_counter += 1
        grades.write(str(grade) + '\n')  # Write grade to file with newline
        grade = int(input('Enter grade, -1 to end: '))

# termination phase
if grade_counter != 0:
    average = total / grade_counter    
else:
    print('No grades were entered')

# Exercise 9.2
# Reads grades using text file from previous exercise and prints individual grades, total, count, and average    

with open('grades.txt', mode='r') as grades:
    print('\nGrades Entered: \n')
    for record in grades:        
        print(record.strip())
    print('')    
    print('Total =', total)
    print('Count =', grade_counter)
    print('Average =', average)