import turtle
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = SCREEN_WIDTH
TARGET_WIDTH = 25
TARGET_LLEFT_X = random.randint(-(SCREEN_WIDTH // 2) + TARGET_WIDTH * 2, SCREEN_WIDTH // 2 - TARGET_WIDTH * 2)
TARGET_LLEFT_Y = random.randint(-(SCREEN_HEIGHT // 2) + TARGET_WIDTH * 2, SCREEN_HEIGHT // 2 - TARGET_WIDTH * 2)
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WES = 180

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()

turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WES)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)

turtle.penup()
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.speed(PROJECTILE_SPEED)
turtle.pendown()
turtle.showturtle()

angle = float(input("Введите угол направления:\n"))
length = float(input("Введите длину полета снаряда:\n"))

turtle.setheading(angle)
turtle.forward(length)

if (TARGET_LLEFT_X <= turtle.xcor() <= TARGET_LLEFT_X + TARGET_WIDTH
        and TARGET_LLEFT_Y <= turtle.ycor() <= TARGET_LLEFT_Y + TARGET_WIDTH):
    print("Ты выиграл!")
else:
    print("Ты проиграл!")

turtle.done()
