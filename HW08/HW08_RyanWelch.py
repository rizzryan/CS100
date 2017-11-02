# Ryan Welch
# CS100 2017F Section 105
# HW 08, November 2nd, 2017

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
    d = {}
    val = 0

    for l in f:
        wL = l.split()

        for words in wL:
            stripped = words.lower().strip(',')

            if stripped not in d:
                d[stripped] = [val]
            else:
                d[stripped].append(val)
        val += 1
    return d

    f.close()


if __name__ == '__main__':
    fileName = input('Enter in a filename: ')
    print(lineOccurences(fileName))
