from turtle import Turtle

BLOCKS_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        # creating a variable pointing to the head of the snake, which is used to control the whole movement of snake
        self.head = self.blocks[0]

    def create_snake(self):
        # creating a snake with 3 squares attaching one each other
        for position in BLOCKS_POSITION:
            self.add_block(position)

    # function to create and add a block
    def add_block(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        new_block.speed("slow")
        self.blocks.append(new_block)

    # function to extend the snake by one block after eating the food
    def extend(self):
        # position of the last block of the snake
        last_block_pos = self.blocks[-1].position()
        self.add_block(last_block_pos)

    def move(self):
        # Just moving the position of all blocks to the before blocks except the first block, first block will change
        # according to the input provided
        for i in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[i - 1].xcor()
            new_y = self.blocks[i - 1].ycor()
            self.blocks[i].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # since in the original game, we are not allowed to go in the opposite direction, we'll check the direction of
        # snake before changing the direction of the snake, to check the direction we have turtle.heading()
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
