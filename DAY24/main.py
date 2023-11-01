# creating a snake game using turtle module
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns off the screen activity

snake = Snake()
food = Food()
score = ScoreBoard()

# To move the snake according to the key pressed
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    # shows/refreshes the screen after all the blocks are moved to a specific position, with this func itself we can
    # see the changes in the screen after screen.tracer()
    screen.update()
    snake.move()
    time.sleep(0.1)
    # detecting the collision of snake and food by using distance method to find distance b/w two turtle objects
    if snake.head.distance(food) <= 15:
        food.recreate()
        snake.extend()
        score.update_score()

    # detecting the collision of snake with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # when ever the snake hits the wall resetting the high score and resetting the snake
        snake.reset_snake()
        score.update_high_score()

    # detecting the collision of snake with its own blocks
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            snake.reset_snake()
            score.update_high_score()

screen.exitonclick()
