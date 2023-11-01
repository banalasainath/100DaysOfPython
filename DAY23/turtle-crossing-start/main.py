import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_car()

    # Detecting the collision of the turtle with the car
    for car in car_manager.cars:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

    if player.is_finish_line():
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()
