# Ryan Welch
# CS100 2017F Section 105
# HW 05 Pig, September 21, 2017

def pigLatin(word, vowels):
    for vowelLength in range(len(vowels)):
        if word[0] in vowels:
            # Concatenating the ending onto the word
            word += 'hay'
            
            print(word)
            break
        else:
            # Concatenating the ending onto the word
            word +=  word[0] + 'ay'
            # Replacing the first letter so that it is empty
            word = word.replace(word[0], '', 1)
            
            print(word)
            break

if __name__ == '__main__':
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    while True:
        word = input('Give me a word: ')
        if len(word) > 0:
            pigLatin(word, vowels)
        else:
            break  