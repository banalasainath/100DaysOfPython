from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
colors = ["red", "blue", "green", "yellow", "orange", "violet", "pink", "indigo", "black"]
angles = [90, 180, 270, 360]
turtle.pensize(10)
turtle.speed("fast")
screen.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk(n):
    for i in range(n):
        turtle.color(random_color())
        rand_ang = random.choice(angles)
        turtle.forward(100)
        # enables to move either right or left
        turtle.setheading(rand_ang)


def polygon(sides):
    turtle.color(random.choice(colors))
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(360 // sides)


#random_walk(50)
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#
# for i in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# for sides in range(3, 11):
#     polygon(sides)

#program to draw the circle in a circular shape
turtle.pensize(1)
turtle.speed("fastest")
cnt_of_circles = int(input("Enter no of circles : "))
tilt_for_each_time = int(360/cnt_of_circles)
for i in range(0,361,tilt_for_each_time):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(i)



screen.exitonclick()
