# Ryan Welch
# CS100 2017F Section 105
# HW 09, November 30th, 2017

def orOther(x, y):
    if x != 0:
        return x
    else:
        return y

def assertion(thing):
    try:
        if thing != None:
            pass
    except TypeError:
        raise
