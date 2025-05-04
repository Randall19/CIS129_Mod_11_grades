""" In this exercise a user is recording grades into a ledger as a teacher might do for a class.
I first ask if the user wants to start a new record or continue with the pre-existing copy of the
record.  If the user enters "false", then he will append to his pre-existing grades.txt file.
If the user enters "true", then write mode is used to over-right the file and start a fresh record.
I do this by assigning "write" for new record or "append" for pre-existing record.
I validate for valid input requiring "false" or "true" to be the only acceptable entries.
I ask the user to input integer grades between 0 and 100.  I validate for proper input, first as
integer, and then in the proper range.  The grades.txt file is printed out as each entry is made.
When the user is done inputing, he can quit with '+1'.  The program notifies the user of the termination
action and the grades.txt file is copied to a list.  The items in the list, converted to integers, are
summed and averaged, and the list and the average grade are printed out.
I used ChatGpt to help me with boolean evaluation for the decision on "write" or "append" decision.
I used ChatGpt to help with the construction of the getValidRange function.
CIS129 Instructor Brittany Griwzow Authors Randall Brown rbrown108 and ChatGpt Open AI
"""


# declare variables
sumGrades = 0
rawGrade =''
sentinel = 0
message1 = ("Enter True to write new record or False to append existing record or +1 to quit:\n").strip().lower()
message2 = ('Enter a student\'s grade between 0 and 100, or +1 to quit: \n')

# Integer Input Validation Function
def getValidRange(msg): 
    while True:
        rGrade = input(msg)
        try:
            rGradeInt = int(rGrade)
            print('you provided integer input')
            
        except ValueError:
            print('Incorrect entry, please enter a interger number between 0 and 100 or +1 to quit')
            continue
        
        if rGrade == '+1':
            print('You have terminated')
            return rGrade
        elif rGradeInt <0:
            print('Too low, please enter number between 0 and 100')
        elif rGradeInt > 100:
            print('too high, please enter number between 0 and 100')
        else:
            print('Valid entry')
            return rGrade
        
# Boolean Input Validation Function
def semesterCheck(msg):
    while True:
        nsInput = input(msg).strip().lower()
        if nsInput == 'true':
            newSemester = True
            break
        elif nsInput == 'false':
            newSemester = False
            break
        else:
            print('You must enter True to write new record or False to append')
    print('newSemester Value is ', newSemester)
    print('newSemester type is ', type(newSemester))
    return newSemester   

# Outer While loop for sentinel flag and new record write or old record append decision
while True:
    if sentinel > 0:
        print('You have decided to end the data entry session')
        break
    newSemester = semesterCheck(message1)
    
    # Inner While loop to collect grades from user
    while rawGrade != '+1':
        
        rawGrade = getValidRange(message2)
        if rawGrade == '+1':
            sentinel = 1
            break
        gradeStr = rawGrade.strip()
        print('gradeStr is', gradeStr)
        entry = gradeStr + '\n'
        print('entry is', entry, 'type is', type(entry))
       
        # conditional statements to write new record or append existing record
        if newSemester:
            print('newSemester value is ', newSemester)
            print('mode is writing')
            with open('grades.txt', mode='w') as testGrade:
                testGrade.write(entry)
                newSemester = False  # only overwrite once
        elif newSemester == False:
            print('mode is appending')
            with open('grades.txt', mode='a') as testGrade:
                testGrade.write(entry)
                
        # statement to display the contents of file
        with open('grades.txt', mode='r') as testGrade:
            print(f'     {"Grades":>6}')
            for grade in testGrade:
                print(f'  {grade.strip():>6}')  # Display output
                
    # check for user decision to quit
    if rawGrade == '+1':
        sentinel = 1                   
        print('sentinel is flagged')            # Display sentinel trigger

# Summarization of the grades.txt contents

# create a list of the grade values
lines =[]
with open ('grades.txt', mode='r' ) as file:
   lines = file.readlines()
   print('Here is a marker for position')
   lines = [line.strip()for line in lines]
   
# Calculate the sum and display grades and the class average 
for item2 in lines:
    print('The added item2 value is ', item2)
    sumGrades += int(item2)
averageGrade = sumGrades/len(lines)
print('The number of grades is  ', len(lines))
print(f'The average grade is {averageGrade:>9.1f}')
           
    
           


        

       
