from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # changing the ball direction when hit the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detecting the collision of the ball with the paddle
    if (ball.xcor() >= 330 and ball.distance(right_paddle) < 50) or \
            (ball.xcor() <= -330 and ball.distance(left_paddle) < 50):
        ball.bounce_x()
        # increasing the speed of the ball whenever the ball touches the paddle
        ball.increase_speed()

    # Detecting the ball misses from a paddle and goes out of the screen for the right player
    if ball.xcor() >= 400:
        ball.reset_player()
        score.left_increment()

    # Detecting the ball misses from a paddle and goes out of the screen for the left player
    if ball.xcor() <= -400:
        ball.reset_player()
        score.right_increment()

screen.exitonclick()
