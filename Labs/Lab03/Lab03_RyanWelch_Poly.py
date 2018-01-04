import turtle

# START VERIFICATION
def coordinatesVerification(fileName):
    f = open(fileName)
    lines = f.readlines()

    openParenthesesCount = 0
    closedParenthesesCount = 0

    for content in lines:
        if content.count('(') >= 3 and content.count(')') >= 3 and content.count('(') == content.count(')'):
            pass
        else:
            raise ValueError('There are not three or more pairs.')

    f.close()

def lineWeightVerification(fileName):
    f = open(fileName)
    lines = f.readlines()

    contentArr = []
    lineWeightArr = []

    for content in lines:
        contentArr.append(content.split('|'))
        lineWeightArr.append(contentArr[len(lines) - 1][1])

    for lineWeight in lineWeightArr:
        try:
            int(lineWeight)
        except:
            raise ValueError('Line weight is not an integer.')

    f.close()


def verticalLineVerification(fileName):
    f = open(fileName)
    lines = f.readlines()

    vLineCount = 0

    for content in lines:
        if '|' in content:
            vLineCount = content.count('|')

    if vLineCount != 3:
        raise ValueError('Incorrect number of attributes.')
    else:
        lineWeightVerification(fileName)
        coordinatesVerification(fileName)

    f.close()

def lineVerification(fileName):
    f = open(fileName)
    lines = f.readlines()

    if len(lines) == 0:
        raise ValueError('File is empty.')
    else:
        verticalLineVerification(fileName)

    f.close()
# END VERIFICATION

# Draw polygon
def poly(fileName, turtleObject):
    f = open(fileName)
    lines = f.readlines()

    contentArr = []
    coordinateArr = []
    newCoordinateArr = []
    lineColor = []
    lineWeightArr =[]
    fillColorArr = []
    splitCommaList = []

    for content in lines:
        contentArr.append(content.split('|'))
    #
    for content in contentArr:
        coordinateArr.append(content[0])
    #
    for content in coordinateArr:
        newCoordinateArr.append(content.split(','))

    # print(coordinateArr)

    # for x in range(len(lines)):
    #     xCoordinate = newCoordinateArr[x][2].replace('(', '')
    #     yCoordinate = newCoordinateArr[x][3].replace(')', '')

        #

    # print(newCoordinateArr)
    for x in range(len(newCoordinateArr)):
        xCoordinate = newCoordinateArr[x][0].replace('(', '')
        yCoordinate = newCoordinateArr[x][1].replace(')', '')
        print('x: ' + xCoordinate, 'y: ' + yCoordinate)

    # for i in range(len)
    # coord = tuple(xCoordinate, yCoordinate)

    # turtleObject.setx(xCoordinate)
    # turtleObject.sety(yCoordinate)
    # print(coord)








if __name__ == '__main__':
    t = turtle.Turtle()
    # fileName = input('Enter in the file name: ')
    fileName = 'polyfield.txt'

    # lineVerification(fileName)
    poly(fileName, t)

    # turtle.mainloop()
