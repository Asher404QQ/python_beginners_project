import turtle

turtle.hideturtle()
turtle.speed(100)

for i in range(10, 300, 5):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)

turtle.exitonclick()