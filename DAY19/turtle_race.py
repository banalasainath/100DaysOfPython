from turtle import Turtle, Screen
import random
race_stop = True
screen = Screen()
screen.setup(height=500, width=500)
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
turtles = []
user_choice = screen.textinput(title="Turtle's Race",prompt="Enter the color of the turtle, which you think would win the race: ")
for i, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-50 + (i * 30))
    turtles.append(new_turtle)
#checking whether the user has entered the input
if user_choice:
    race_stop = False
#Looping until race stop is True
while not race_stop:
    #checking if any one of the turtle reaches the end
    for turtle in turtles:
        #checking the turtle's x-coordeinate
        if turtle.xcor() >= 230:
            race_stop = True
            if turtle.pencolor() == user_choice:
                print("You have chosen the correct turtle")
            else:
                print(f"You Lose,{turtle.pencolor()} turtle won the race")
            break

    for turtle in turtles:
        steps = random.randint(0, 10)
        turtle.forward(steps)


screen.exitonclick()
