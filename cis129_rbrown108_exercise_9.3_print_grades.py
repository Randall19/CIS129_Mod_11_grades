"""
This exercise demonstrates the ability to read data one line at a time into
a csv type file named 'grades.csv' using the open, with, writer, and writerow methods.
After the file is created, the contents are printed out one line at a time using
the csv.reader method.  Each row contains the first name, last name,
and a list of the student's three test score results.
CIS129 instructor: Brittany Griwzow  author:  Randall Brown rbrown108
"""

import csv

def main():
    # open (or create if new) grades.csv file with assigned variable name commaGrades
    with open('grades.csv', mode='w', newline='') as commaGrades:
        writer = csv.writer(commaGrades)# assign to writer the call to function csv.writer
        writer.writerow(['Joe', 'Smith', [99,88,77]])   # begin writing in each row of data
        writer.writerow(['Mary', 'Jane', [66,88,77]])
        writer.writerow(['Harry', 'Chest', [55,82,44]])
        writer.writerow(['Lucky', 'Strike', [90,88,100]])
        writer.writerow(['Joe', 'Camel', [80,88,77]])

    
    # open the grades.csv file known as commaGrades
    with open('grades.csv', 'r', newline='') as commaGrades:
        print(f'{"First_Name":<15}{"Last_Name":<15}{"Grades":>15}') # print headings
        reader = csv.reader(commaGrades) # assign the csv.reader function to reader
        for entry in reader:
            First_Name, Last_Name, Grades = entry  # assign variable names to row elements
            print(f'{First_Name:<15}{Last_Name:<15}{Grades:>15}') # print each row in the file

main()
