# Ryan Welch
# CS100 2017F Section 105
# HW 06, September 21, 2017

# Problem 2: 8.4
s = 'Monty Python'
fruit = 'banana'

# Problem 3: 8.8
word = 'banana'
newWord = word.upper()

# Finds the first index of the parameter
index = word.find('a')
name = 'bob'

# Problem 4: 8.11
def isReverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    
    # Fix was making j less than or equal to 0
    while j >= 0:
        print(i, j)
        
        if word1[i] != word2[j]:
            return False
        
        i = i + 1
        j = j - 1
    
    return True

# Problem 5
def uniqueCharacters(s):
    uniqueCharacterList = []
    
    for characters in s[::]:
        if characters not in uniqueCharacterList:
            uniqueCharacterList.append(characters)
    
    return uniqueCharacterList

# Problem 6
def numUniqueCharacters(s):
    print('Number of unique letters: ' + str(len(uniqueCharacters(s))))

if __name__ == '__main__':
    print('Beginning of 8.4\n')
    print(s[0:5])
    print(s[6:12])
    print(fruit[:3])
    print(fruit[3:])
    print(fruit[3:3])

    # fruit[:] is the whole string
    print(fruit[:])
    print('\nEnd of 8.4\n\nBeginning of 8.8')

    print(newWord)
    print(index)
    # Finds the first index of the parameter
    print(word.find('na'))
    # Finds the first index of the parameter specified at the starting point
    print(word.find('na', 3))
    # Finds the first index of the parameter specified at the starting point and going up to the ending point
    print(name.find('b', 1, 2))
    print('\nEnd of 8.8\n\nBeginning of 8.11\n')

    print(isReverse('pots', 'stop'))
    print('\nEnd of 8.11\n')

    print('Unique letters: ' + str(uniqueCharacters('Abracadabra')))
    numUniqueCharacters('Abracadabra')