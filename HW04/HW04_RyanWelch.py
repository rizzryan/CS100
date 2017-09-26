# Ryan Welch
# CS100 2017F Section 105
# HW 04, September 21, 2017

def firstLast(seq):
    if len(seq) > 1:
        return (seq[0], seq[len(seq)-1])
    elif len(seq) == 1:
        return (seq)
    else:
        return (seq)
    
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
    if len(target) == 0 or len(mask) == 0:
        print('You have not entered in a word or list.')
    else:
        for letters in range(len(mask)):
            print(target.count(mask[letters]))
    
if __name__ == '__main__':
    tu = (1, 3, 5, 9)
    
    firstLast(tu)

    lt = [10, 9, 0, 3, 30, 99, 100]
    
    print(lt)
    
    popMin(lt)
    
    print('End of popMin() function.\n')
    
    inOrder(lt)
    
    print('End of inOrder() function.\n')
    
    lettersList = []
    lettersCount = int(input('How many letters do you want to input? '))
    
    for letters in range(lettersCount):
        letter = input('Enter in a letter: ')
        lettersList.append(letter)
    
    word = input('Enter in a word: ')
    
    multiCount(word, lettersList)
    
    print('End of multiCount() function.')