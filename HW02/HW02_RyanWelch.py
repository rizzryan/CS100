# Ryan Welch
# CS100 2017F Section 105
# HW 02, September 21, 2017
import turtle
import math


# Exercise 4.1 Stack diagram for the variables arc_length, n, angle, step_length, and step_angle
"""
Arc length: 628.3185307179587
N: 158
Step length: 3.9766995615060674
Step angle: 2.278481012658228
Angle: 2.278481012658228
Angle: 2.278481012658228
"""

# Exercise 4.2
def line(turtleObject, numSegments, length, angle):
    for x in range(numSegments):
        turtleObject.forward(length)
        turtleObject.left(angle)
#
def arc(turtleObject, radius, innerAngle):
    arcLength = 2 * math.pi * radius * innerAngle / 360
    n = int(arcLength / 4) + 1
    stepLength = arcLength / n
    stepAngle = float(innerAngle) / n
    turtleObject.left(stepAngle/2)
    line(t, n, stepLength, stepAngle)
    turtleObject.right(stepAngle/2)

def curve(turtleObject, radius, innerAngle):
    for x in range(2):    
        arc(turtleObject, radius, innerAngle)
        turtleObject.left(180-innerAngle)
    
def flower(turtleObject, radius, innerAngle, numPetals):
    # For loop to create x petals
    for n in range(numPetals):
        curve(turtleObject, radius, innerAngle)
        turtleObject.left(360 / numPetals)
        
#-----------------------------------------------------------------------------------
# Exercise 4.3
def triangle(turtleObject, l, angle):
    # l is length of segment/side
    turtleObject.right(angle)
    turtleObject.forward(l)
    turtleObject.left(90 + angle)
    # Trigonometry - purpose is to essentially rotate by the degrees
    turtleObject.forward(2 * (l * math.sin(angle * math.pi / 180)))
    turtleObject.left(90 + angle)
    turtleObject.forward(l)
    turtleObject.left(180 - angle)
    
def compositeShape(turtleObject, numSegments, l):
    angle = 360.0 / numSegments
    for i in range(numSegments):
        triangle(t, l, angle / 2)
        t.left(angle)    
#---------------------------------------------------------------------------------
# Exercise 4.4
def drawA(t):
    t.forward(15)
    t.left(180)
    t.forward(30)
    t.right(-45)
    t.forward(30)
    t.backward(50)
    t.penup()
    t.home()
    t.forward(15)
    t.right(45)
    t.pendown()
    t.forward(30)
    t.backward(50)
    t.penup()
    t.home()
    
def drawB(t):
    t.circle(20, 180)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.circle(20, -180)
    t.left(90)
    t.forward(40)
    t.penup()
    t.home()

def drawC(t):
    t.circle(20, -180)
    t.penup()
    t.home()
    
def drawD(t):
    t.circle(20, 180)
    t.home()
    
def drawE(t):
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(30)
    t.penup()
    t.home()

def drawF(t):
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.left(90)
    t.penup()
    t.home()
    
def drawG(t):
    t.circle(40, -180)
    t.penup()
    t.home()
    t.left(90)
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(15)
    
def drawH(t):
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.left(180)
    t.forward(90)
    t.penup()
    t.home()
    t.left(180)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.left(180)
    t.forward(90)
    t.penup()
    t.home()
    
def drawI(t):
    t.forward(20)
    t.left(180)
    t.forward(40)
    t.penup()
    t.home()
    t.left(90)
    t.pendown()
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.left(180)
    t.forward(40)
    t.penup()
    t.right(90)
    t.home()
    
def drawJ(t):
    t.right(90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.circle(10, 180)
    t.penup()
    t.pendown()
    t.forward(20)
    t.left(90)
    t.forward(20)
    
def drawK(t):
    t.left(90)
    t.forward(20)
    t.backward(40)
    t.home()
    t.right(45)
    t.forward(30)
    t.home()
    t.left(45)
    t.forward(30)
    t.home()
    
def drawL(t):
    t.left(180)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.penup()
    t.home()

def drawM(t):
    t.penup()
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.forward(45)
    t.left(90)
    t.pendown()
    t.forward(90)
    t.backward(160)
    t.penup()
    t.home()
    t.backward(45)
    t.left(90)
    t.pendown()
    t.forward(90)
    t.backward(160)
    t.penup()
    t.home()
    
def drawN(t):
    t.left(90)
    t.forward(40)
    t.right(130)
    t.forward(60)
    t.left(130)
    t.forward(45)
    
def drawO(t):
    t.circle(30)
    
def drawP(t):
    t.circle(20, 180)
    t.home()
    t.right(90)
    t.forward(20)
    t.penup()
    t.home()
    
def drawQ(t):
    t.circle(30)
    t.right(45)
    t.forward(20)
    t.penup()
    t.home()
    
def drawR(t):
    t.circle(20, 180)
    t.home()
    t.right(90)
    t.forward(20)
    t.penup()
    t.home()
    t.pendown()
    t.right(45)
    t.forward(30)
    t.penup()
    t.home()
def drawS(t):
    t.circle(20, -180)
    t.penup()
    t.home()
    t.pendown()
    t.left(180)
    t.circle(20, -180)
    
def drawT(t):
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(45)
    t.left(180)
    t.forward(90)
    t.penup()
    t.left(180)
    t.home()

def drawU(t):
    t.right(90)
    t.forward(30)
    t.circle(25, 180)
    t.forward(30)
    t.penup()
    t.home()
    
def drawV(t):
    t.penup()
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(45)
    t.pendown()
    t.home()
    
def drawW(t):
    t.penup()
    t.left(-90)
    t.forward(90)
    t.left(-90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.left(-90)
    t.forward(90)
    t.right(-90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.forward(45)
    t.left(-90)
    t.pendown()
    t.forward(90)
    t.backward(160)
    t.penup()
    t.home()
    t.backward(45)
    t.left(-90)
    t.pendown()
    t.forward(90)
    t.backward(160)
    t.penup()
    t.home()
    
def drawX(t):
    t.penup()
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(45)
    t.pendown()
    t.home()
    
def drawY(t):
    t.penup()
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(45)
    t.pendown()
    t.home()
    t.penup()
    t.right(90)
    t.forward(90)
    t.forward(45)
    t.pendown()
    t.home()
    
def drawZ(t):
    t.forward(30)
    t.penup()
    t.left(180)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.pendown()
    t.forward(30)
    t.home()
    
#-----------------------------------------------------------------------------
# Exercise 4.5
def spiral(turtleObject, lines):
    # Formula for Archimedian spiral is r = a + b*th
    
    # Value of th will need to be updated in a for loop
    th = 0.0
    a = 0.1
    b = 0.0002
    length = 3
    
    for x in range(lines):
        turtleObject.forward(length)
        
        # Value of dTh will be added on to th
        dTh = 1 / (a + (b * th))
        
        turtleObject.left(dTh)
        th += dTh

#----------------------------------------------------------------------------
# Two Circles
def twoCircles(t, radius):
    t.circle(radius)
    t.penup()
    t.forward(radius * 2)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.home()
    
# Inscribed Hexagon
def inscribedHexagon(t, sideLen):
    for x in range(6):
        t.forward(sideLen)
        t.left(60)
    t.forward(sideLen / 2)
    
    r = (math.sqrt(3) * sideLen) / 2
    t.circle(r)
#-------------------------------------------------------------------------------
    
if __name__ == '__main__':
    # Turtle object instantiated
    t = turtle.Turtle()
    
    # 4.2
    r = float(input('Enter in a radius: '))
    iA = float(input('Enter in an inner angle in degrees: '))
    p = int(input('Enter in the number of petals:'))
    
    flower(t, r, iA, p)
    t.reset()
    
    # 4.3
    length = int(input('Enter in the length of the sides: '))
    n = int(input('Enter in the number of segments: '))
    compositeShape(t, n, length)
    t.reset()
    
    # 4.4
    # Change the drawA(t) method to drawB(t) etc
    drawA(t)
    t.reset()
    
    # 4.5
    lines = int(input('Enter in the number of lines to be drawn: '))
    
    spiral(t, lines)
    t.reset()
    
    # Two Circles
    radius = int(input('Enter in a radius: '))
    
    twoCircles(t, radius)
    t.reset()
    
    # Inscribed Hexagon
    sideLen = int(input('Enter in a side length of the hexagon: '))
    
    inscribedHexagon(t, sideLen)
    t.reset()
    # Window closes when user clicks on the exit button 
    turtle.mainloop()