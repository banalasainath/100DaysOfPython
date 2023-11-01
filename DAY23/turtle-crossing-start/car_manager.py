from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = 5

    def generate_car(self):
        # Since we can't move the turtle while a new car generating for every 0.1 secs, we are trying to create a car
        # in one in 6 attempts
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            # giving 50px space for the start and end position of the turtle
            y_cor = random.randint(-250, 250)
            # creating the car at the left edge of the screen and random heights
            car.goto(300, y_cor)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.speed(self.car_speed)
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        # incrementing the speed of the cars after the turtle reaches the end_line
        self.car_speed += MOVE_INCREMENT

