from turtle import Turtle, Screen
import subprocess
turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def clock_wise():
    turtle.right(10)


def anti_clock_wise():
    turtle.left(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.onkey(key='f', fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="a", fun=anti_clock_wise)
screen.onkey(key="c", fun=clock_wise)
screen.onkey(key='r', fun=clear_screen)
screen.listen()

screen.exitonclick()

