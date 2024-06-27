import turtle

CIRCLE_RADIUS = 100
ANGLE = 10

colors = ["green", "yellow", "orange", "red", "purple", "blue"]
turtle.bgcolor("black")
turtle.hideturtle()
turtle.speed(100)

for i in range(40):
    turtle.color(colors[i % 6])
    turtle.circle(CIRCLE_RADIUS)
    turtle.left(ANGLE)

turtle.exitonclick()