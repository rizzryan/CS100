# Ryan Welch
# CS100 2017F Section 105
# HW 05 Longest, September 21, 2017

def longAndShort(words):
    '''
    max function returns the largest number. When the words and key equals len parameters are passed, the function will return the longest element.
    min function returns the smallest number. When the words and key equals len parameters are passed, the function will return the smallest element.
    '''
    
    print('Longest word: ' + '\'' + max(words, key=len) + '\'')
    print('Shortest word: ' + '\'' + min(words, key=len) + '\'')

if __name__ == '__main__':
    wordList = []
    
    while True:
        word = input('Give me a word: ')
        if len(word) > 0:
            wordList.append(word)
        else:
            break
    
    longAndShort(wordList)