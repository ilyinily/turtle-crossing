from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WIDTH = 600
HEIGHT = 600
STARTING_NUMBER = 5


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.penup()
        self.setposition(x=WIDTH/2, y=randint(-HEIGHT/2 + 40, HEIGHT/2 - 40))
        self.setheading(180)
        self.shapesize(stretch_len=3, stretch_wid=1)

    def move(self):
        if randint(0, 20) == 20:
            self.forward(MOVE_INCREMENT)

    def reached_border(self):
        if self.position()[0] <= -WIDTH/2:
            self.setposition(-self.position()[0], self.position()[1])
