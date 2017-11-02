import datetime
import random

def guestbook(file, option):
    arr = []
    randomList = []

    print(str(len(f.readlines())) + ' lines in the file {}.'.format(file))

    if option.upper() == 'R':
        f = open(file, 'r')

        for elems in f.readlines():
            arr.append(elems.split(','))

        for elems in arr:
            randomList.append('At ' + elems[0] + ', ' + elems[1] + ' wrote' + " '{}'".format(elems[2]))

        print(randomList[random.randint(0, len(randomList))])

    else:
        f = open(file, 'a')

        name = input('What is your name? ')
        message = input('Enter in your message: ')
        
        currentDate = datetime.datetime.now().strftime('%I:%M%p on %B %d %Y')

        f.write(currentDate + ',' + name + ',' + message)

    f.close()

if __name__ == '__main__':
    userOption = input('Enter N for new entry or R for random entry: ')
    fileName = input('Enter the file name: ')

    guestbook(fileName, userOption)
