# Ryan Welch
# CS100 2017F Section 105
# HW 00, Sept 7, 2017

# Variable assignment 1
userUniversityName = 'NJIT'

# Variable assignment 2
userGPA = 3.019

# Variable assignment 3
userAge = 17

# Variable assignments for storing name values and printing stored values 
firstName = 'Ryan'
lastName = 'Welch'

print('{} {}\n'.format(firstName, lastName))
print('{1}, {0}\n'.format(firstName, lastName))

# Variable assignment used to store the value of 'na ' repeated 16 times
repeatedString = 'na ' * 16

print('{} batman'.format(repeatedString))

#--------------------------------------------

# Exercises
## Exercise 1.1
# 1. When you leave out one of the parentheses, you would receive a syntax error detailing that you are missing parentheses to call 'print'. When you leave out both parentheses, a syntax error will be present, detailing that there is an unexpected End of File, or EOF, while parsing.

# 2. When you leave out one of the quotation marks, you would receive a syntax error detailing an End of Line, or EOL, while scanning string literal. When you leave out both parentheses, you would receive a name error detailing that the parameter in the print function is not defined.

# 3. When you put a plus sign in front of the number, the plus sign is dropped because 2 and +2 are the same number. The plus sign indicates that the number is a positive number. When you print out 2++2, the sum will still be 4 because you are adding positive 2 to 2.

# 4. When you have a leading 0 in Python, you would get a syntax error stating that there is an invalid token.

# 5. When you have two values with no operator between them, you would receive an error stating that there is invalid syntax.

## Exercise 1.2
# 1. 2562 seconds in 42 minutes and 42 seconds.

# 2. 6.211180124223602 miles in 10 kilometers.

# 3. 0.0024243482139826703 miles per second. 0.14546089283896022 miles per minute. Average speed is 8.727653570337614 miles per hour.

## Exercise 2.1
# 1. 42 = n is illegal because you cannot have a number as the variable assignment of a value that can be mutable. The error present is a syntax error stating that you cannot assign to literal.

# 2. x = y = 1 is fine when printed out because you are assigning x the value of y = 1.

# 3. When you put a semi colon at the end of a statement, nothing is effected.

# 4. When you put a semi colon at the end of a statement, you will get an invalid syntax error. Using an period is needed when you want to call a method on an object.

# 5. When you try to multiply two variables as 'xy' and print out the product, there will be a name error stating that the variable xy is not defined.

## Exercise 2.2
# 1. The volume of the sphere is 523.5987755982989 units cubed.

# 2. Total wholesale cost is $945.45 for 60 copies after the discount and the added shipping price.

# 3. You will get home at 7:30:06 am for breakfast.