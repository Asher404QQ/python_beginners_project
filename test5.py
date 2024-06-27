import turtle

turtle.bgcolor("black")
turtle.hideturtle()
turtle.speed(100)
turtle.setheading(90)

colors = ["green", "yellow", "orange", "red", "purple", "blue"]

for i in range(5, 500):
    turtle.color(colors[i % 6])
    turtle.left(59) # 150
    turtle.forward(i)


turtle.exitonclick()