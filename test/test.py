from student import *

# for x in range(2):
#     name = input('Enter in your name: ')
#     studentID = input('Enter in your student ID: ')
#     gpa = float(input('Enter in your gpa out of a 4.0 scale: '))
#
#     if x == 0:
#         s1 = Student(name, studentID, gpa)
#     else:
#         s2 = Student(name, studentID, gpa)

# s1.displayInfo()
# s2.displayInfo()

def makeStdList(fileName):
    f = open(fileName)
    lines = f.readlines()

    for content in lines:
        print(content.split())

    f.close()

makeStdList('student.txt')
