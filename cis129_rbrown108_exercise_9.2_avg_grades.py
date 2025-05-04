"""
In the first part of this exercise the program writes a new text file grades.txt known as grades that inputs
grade values as strings with line break characters following
so that each grade value will be entered on an individual line in the text file.
In the second part of the exercise, the text file is read, the line break character
is striped, and the value converted to an integer.  Then the for loop will
process the interger value to calculate the running sum and average of grades.
The output displays each grade, the running sum of grades,
and the running average of grades.
CIS129 instructor Brittany Griwzow author Randall Brown rbrown108
"""
# declare variables
total = 0
gradeCounter = 0

# write grades to file
with open('grades.txt', mode='w') as grades:
    grades.write('97\n')
    grades.write('88\n')
    grades.write('72\n')

# open file to read
with open('grades.txt', mode='r') as grades:
    print('grades.txt file contents\n')
    for grade in grades:
        # strip grade of end line and covert to integer
        gradeVal=int(grade.strip('\n'))
        print(f'this is gradeVal:         {gradeVal:>20}')
        # generate running total of sum of grades
        total += int(gradeVal)
        # generate running total of number of grades
        gradeCounter += 1
        # calculate grade average
        average = total/gradeCounter
        # display sum of grades, number of grades, and average grade
        print(f'the sum of grades is:     {total:>20}')
        print(f'the number of grades is:  {gradeCounter:>20}')
        print(f'the running average is:      {average:>20.2f}')
        print()

