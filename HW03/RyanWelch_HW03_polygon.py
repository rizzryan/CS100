# Ryan Welch
# CS100 2017F Section 105
# HW 03 Polygon, September 21, 2017
import turtle

def drawShape(turtleObject, color, width, length, shape):
    turtleObject.width(width)
    turtleObject.color(color)
    
    s = shape.lower()
    
    if s == 'line':
        turtleObject.fd(length)
    elif s == 'square':
        for x in range(4):
            turtleObject.fd(length)
            turtleObject.lt(90)
    elif s == 'triangle':
        for t in range(3):
            turtleObject.fd(length)
            turtleObject.lt(120)

if __name__ == '__main__':
    t = turtle.Turtle()
    
    color = input('Enter in a color: ')
    width = int(input('Enter in a width: '))
    length = int(input('Enter in a length: '))
    shape = input('Pick a shape: line, triangle, or square: ')
    
    drawShape(t, color, width, length, shape)   

    turtle.mainloop()