# Ryan Welch
# CS100 2017F Section 105
# HW 08, October 27, 2017

# Problem 2
def log(filename):
    f = open(filename, 'a')
    while True:
        name = input('What is your name? ')
        visit = input('What is the nature of your visit? ')
        if len(name) > 0 and len(visit) > 0:
            appendedStr = '{} | {}\n'.format(name, visit)
            f.write(appendedStr)
        else:
            break
    f.close()

# Problem 3
def lineOccurences(filename):
    f = open(fileName, 'r')
    wordDict = {}
    wordList = []
    numLine = []
    fileIndex = len(f.readlines())

    line = f.readlines()
    print(line)

    for word in f.read().split():
        wordList.append(word.lower().replace(',', ''))

    for nums in range(fileIndex):
        numLine.append(nums)

    f.close()

    # print(numLine)

if __name__ == '__main__':
    fileName = input('Enter in a filename: ')
    lineOccurences(fileName)
