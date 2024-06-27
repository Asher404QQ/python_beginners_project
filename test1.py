import turtle
import math

turtle.hideturtle()
turtle.speed(100)

for i in range(9999):
    turtle.forward(math.sqrt(i)*10)
    turtle.left(55)

turtle.done()