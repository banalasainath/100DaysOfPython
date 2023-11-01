import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Since we have inherited Turtle class, we can use the methods of the  Turtle class
        self.shape("circle")
        self.color("white")
        # since each block of snake is of 20px, we are reducing the size of food to half of the block size
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()
        self.recreate()

    def recreate(self):
        # since our whole screen of size (600,600) i.e., x and y lies in b/w (-300,300)
        # since we assume that the food shouldn't be at the edge
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.setpos(x, y)
