from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_change = 10
        self.y_change = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_change
        y_cor = self.ycor() + self.y_change
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        # changing the direction of ball, by varying the y co-ordinates
        self.y_change *= -1

    def bounce_x(self):
        # changing the direction of ball, by varying the x co-ordinates
        self.x_change *= -1

    def reset_player(self):
        # when the ball goes out the screen, the ball will reverse the direction towards other player
        self.goto(0, 0)
        self.x_change *= -1
        # Normalizing the speed when ever the ball goes out the screen
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= 0.9

