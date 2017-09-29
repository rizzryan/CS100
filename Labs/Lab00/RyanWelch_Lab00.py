# Ryan Welch
# CS100 2017F Section 105
# Lab00, Sept 28, 2017
import math
import turtle

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(abs((b*b) - (4*a*c)))) / (2*a)
    x2 = (-b - math.sqrt(abs((b*b) - (4*a*c)))) / (2*a)

    return x1, x2
    
def venn(a, b):
    firstList = []
    secondList = []
    thirdList = []
    
    for x in a:
        if x not in b:
            firstList.append(x)
            
    for x in a:
        if x in b:
            secondList.append(x)
            
    for x in b:
        if x not in a:
            thirdList.append(x)
        
    return (firstList, secondList, thirdList)

def drawTick(turtleObject, tickLen):
    turtleObject.lt(90)
    turtleObject.fd(tickLen)
    turtleObject.pu()
    turtleObject.backward(tickLen)
    turtleObject.rt(90)
                
def drawTicks(turtleObject, tickLen, numTicks, distance):
    for ticks in range(numTicks):
        drawTick(turtleObject, tickLen)
        turtleObject.fd(distance)
        turtleObject.pd()
    turtleObject.pu()
    turtleObject.back(distance)
    
def rps(p0, p1):
    if p0 == 'R' and p1 == 'S':
        return 1
    elif p0 == 'S' and p1 == 'R':
        return 0
    elif p0 == 'P' and p1 == 'R':
        return 1
    elif p0 == 'R' and p1 == 'P':
        return 0
    elif p0 == 'S' and p1 == 'P':
        return 1
    else:
        return 0
    
def play():
    player1 = input('Player 1 enter in R, P, or S: ')
    player2 = input('Player 2 enter in R, P, or S: ')
    
    print(rps(player1, player2))
    
    if rps(player1, player2) == 1:
        print('Player 1 wins.')
    elif rps(player1, player2) == 0:
        print('Player 2 wins.')
    else:
        print('There is a tie.')
    
if __name__ == '__main__':
    a = int(input('Enter in the value for a: '))
    b = int(input('Enter in the value for b: '))
    c = int(input('Enter in the value for c: '))
    
    print(quadratic(a, b, c))
    
    list1 = []
    list2 = []
    
    numContentsList1 = int(input('How many numbers should go into list1? '))
    numContentsList2 = int(input('How many numbers should go into list2? '))
    
    for num1 in range(numContentsList1):
        list1Element = int(input('Enter an integer: '))
        list1.append(list1Element)
        
    for num2 in range(numContentsList2):
        list2Element = int(input('Enter an integer: '))
        list2.append(list2Element)
        
    print(venn(list1, list2))
    
    t = turtle.Turtle()
    
    tickLen = int(input('Enter in a tick length: '))
    numTicks = int(input('Enter in the number of ticks: '))
    distance = int(input('Enter in the spacing amount: '))
    
    drawTicks(t, tickLen, numTicks, distance)
    
    turtle.mainloop()
    
    play()
    