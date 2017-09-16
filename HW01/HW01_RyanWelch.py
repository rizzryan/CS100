# Ryan Welch
# CS100 2017F Section 105
# HW 01, September 21, 2017

# Problem 2
gradesList = []
frequency = []

# For loop in order to assign values to letterGrades and append the letterGrades to the array gradesList
for letters in range(10):
    letterGrades = input('Enter in a letter grade: ')
    gradesList.append(letterGrades)

# Stores the value of the frequency of the letter A
letterGradeA = gradesList.count('A')
frequency.append(letterGradeA)

# Stores the value of the frequency of the letter B
letterGradeB = gradesList.count('B')
frequency.append(letterGradeB)

# Stores the value of the frequency of the letter C
letterGradeC = gradesList.count('C')
frequency.append(letterGradeC)

# Stores the value of the frequency of the letter D
letterGradeD = gradesList.count('D')
frequency.append(letterGradeD)

# Stores the value of the frequency of the letter F
letterGradeF = gradesList.count('F')
frequency.append(letterGradeF)

# Prints out the frequency of the letter grades in the array gradesList
print('\nProblem 2 answers:\n' + str(frequency) + '\n')

# --------------------------------------------------------------------------------------------------
# Problem 3
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
herding_dogs = dog_breeds[0:2]
print('Problem 3 answers:\n' + 'B. ' + str(herding_dogs) + '\n')

tiny_dogs = dog_breeds[-1]
print('C. ' + tiny_dogs + '\n')

if 'Persian' in dog_breeds:
    print('D. ' + str(True) + ', Persian is in the array dog_breeds.')
else:
    print('D. ' + str(False) + ', Persian is not in the array dog_breeds.')