# Ryan Welch
# CS100 2017F Section 105
# HW 06, September 21, 2017
# 8.4 solutions
def any_lowercase1(s):
    # Essentially means for character in string
    for c in s:
        if c.islower():
            # True will be returned when the first instance of the character in the string is lowercase.
            return True
        else:
            # False will be returned when the first instance of the character in the string is not lowercase.
            return False

def any_lowercase2(s):
    # Essentially means for character in string
    for c in s:
        if 'c'.islower():
            # True will always be returned because 'c' is always lowercase
            return 'True'
        else:
            return 'False'
def any_lowercase3(s):
    # Essentially means for character in string
    for c in s:
        # Assigning True or False to the variable flag based on whether or not the last character is lowercaseor not.
        flag = c.islower()
    return flag

def any_lowercase4(s):
    
    flag = False
    # Essentially means for character in string
    for c in s:
        # flag is updated to True or False based on the capitalization of the current iteration
        flag = flag or c.islower()
    # True or False is returned based on the last character in the string
    return flag

def any_lowercase5(s):
    # Essentially means for character in string
    for c in s:
        # If not True or False based on the evaluation of the capitalization of the current character
        # Default boolean value is True
        if not c.islower():
            return False
    # True or False is returned based on the capitalization of the first character in the string
    return True

print(any_lowercase1('StRinG'))
#print(any_lowercase2('StoriEs'))
#print(any_lowercase3('Steak'))
print(any_lowercase4('SCHOOL'))
print(any_lowercase5('sdhsdk'))