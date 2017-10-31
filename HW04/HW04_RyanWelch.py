# Ryan Welch
# CS100 2017F Section 105
# HW 04, September 21, 2017

def firstLast(seq):
    # return a tuple of length 2, where the first item in the tuple is the first item in seq, and the second item in tuple is the last item in seq.
    # If seq is empty, the function should return an empty tuple. If seq has only one element, the function should return a tuple containing just that element.

    if len(seq) > 1:
        return (seq[:1] + seq[-1:])
    elif len(seq) == 1:
        return seq[:1]
    else:
        return seq
    
def popMin(lst):
    # remove and return the smallest element of lst
    
    lst.sort(key = None, reverse = False)
    print(lst.pop(0))
    
def inOrder(lst):
    # use popMmin to remove and print the items of lst, in order of smallest to largest
    
    for length in range(len(lst)):
        popMin(lst)
        
def multiCount(target, mask):
    # returns a list of integers where each integer is equal to the count of the corresponding element at that index in mask within the elements of target.
    targetList = []
    
    if len(target) == 0 or len(mask) == 0:
        print('You have not entered in a word or list.')
    else:
        for letters in range(len(mask)):
            targetList.append(target.count(mask[letters]))
        return targetList
    
if __name__ == '__main__':
    print('Beginning of firstLast() function.\n')
    
    userTuple = ()
    
    uTInputs = int(input('How many elements do you want to enter? '))
    
    for numbers in range(uTInputs):
        uTNumber = int(input('Enter in a number: '))
        userTuple += (uTNumber,)
    
    print('Your tuple is {}'.format(userTuple))
    
    print(firstLast(userTuple))
    
    print('End of firstLast() function.\n\nBeginning of popMin() function.\n')
    
    popMinInputs = int(input('How many integers do you want to enter? '))
    
    pM = []
    
    for numbers in range(popMinInputs):
        pMNumber = int(input('Enter in a number: '))
        pM.append(pMNumber)
    
    print(pM)
    
    popMin(pM)
    
    print('End of popMin() function.\n\nBeginning of inOrder() function.\n')
    
    inOrderInputs = int(input('How many integers do you want to enter? '))
    
    iO = []
    
    for numbers in range(inOrderInputs):
        iONumber = int(input('Enter in a number: '))
        iO.append(iONumber)
    
    print(iO)
    
    inOrder(iO)
    
    print('End of inOrder() function.\n\nBeginning of multiCount() function.\n')
    
    lettersList = []
    lettersCount = int(input('How many letters do you want to input? '))
    
    for letters in range(lettersCount):
        letter = input('Enter in a letter: ')
        lettersList.append(letter)
    
    word = input('Enter in a word: ')
    
    multiCount(word, lettersList)
    
    print('End of multiCount() function.')