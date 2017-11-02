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

# Problem 3 INCOMPLETE
def lineOccurences(filename):
    f = open(fileName)
    fR = f.readlines()
    for l in fR:
        index = len(l) - 1
        for i in range(index):
            word = l
            k = word.lower().replace(',', '').replace('\n', '')
            val = 0
            d = dict({k:index})
            index -= 1
    print(d)

    f.close()


if __name__ == '__main__':
    fileName = input('Enter in a filename: ')
    lineOccurences(fileName)
