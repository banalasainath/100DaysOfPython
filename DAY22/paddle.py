from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position_co_ordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position_co_ordinates)

    def move_up(self):
        changed_y = self.ycor() + 20
        self.goto(self.xcor(), changed_y)

    def move_down(self):
        changed_y = self.ycor() - 20
        self.goto(self.xcor(), changed_y)
