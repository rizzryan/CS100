import turtle

donny = turtle.Turtle()
donny.shape('turtle')

for x in range(1000):
    donny.down()
    donny.forward(x)
    donny.right(x)
    donny.up()
    print(x)
    
# Write a function given a turtle and a size that will deraw a square around the center
# Draw a backwards L using three squares