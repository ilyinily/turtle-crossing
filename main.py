import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import WIDTH, HEIGHT, STARTING_NUMBER
from scoreboard import FONT
from random import choice

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

runner = Player()
scoreboard = Scoreboard()
cars = []
for i in range(STARTING_NUMBER):
    cars.append(CarManager())


def level_up():
    cars.append(CarManager())
    scoreboard.level_up()


screen.listen()
screen.onkeypress(key="Up", fun=runner.move)
screen.onkeypress(key="w", fun=scoreboard.level_up)
screen.onkeypress(key="t", fun=level_up)

game_is_on = True
while game_is_on:
    for car in cars:
        for round_counter in range(scoreboard.round):
            car.move()
        if car.distance(runner) <= 25:
            game_is_on = False
    if runner.goal_reached():
        scoreboard.round += 1
        scoreboard.display_score()
        cars.append(CarManager())
    for car in cars:
        car.reached_border()
    time.sleep(0.1)
    screen.update()

scoreboard.clear()
scoreboard.write(f"Game over in round {scoreboard.round}.", font=FONT)

screen.exitonclick()