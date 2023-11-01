from turtle import Turtle, Screen
from color_generation import final_colors
import random

# printing one row of dots
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.speed("fastest")
# moving to the centre of the screen
turtle.right(135)
turtle.penup()
turtle.forward(300)
turtle.left(135)
# to know turtle position after setting it to the centre, After getting the value we use them in the loop to
# change the position of the turtle after printing each row
print(turtle.position())
for i in range(10):
    for j in range(10):
        turtle.dot(20, random.choice(final_colors))
        turtle.penup()
        turtle.forward(50)
    turtle.setpos(-212.13, -212.13 + 50 * (i + 1))

screen.exitonclick()
