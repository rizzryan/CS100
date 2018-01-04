# Ryan Welch
# CS100 2017F Section 105
# HW 09, November 30th, 2017

import sys
from library import *

def operation(value):
    assertion(value)
    print(orOther(value, 5))

def wrapper(value):
    try:
        operation(value)
    except:
        print('The operation was unsuccessful.')
        sys.exit()


wrapper(12)
