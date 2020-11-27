from turtle import Turtle
from car_manager import WIDTH, HEIGHT
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x=-WIDTH/2 + 30, y=HEIGHT/2 - 30)
        self.round = 1
        self.write(arg=f"Round {self.round}", font=FONT)

    def display_score(self):
        self.clear()
        self.write(arg=f"Round {self.round}", font=FONT)

    def level_up(self):
        self.round += 1
        self.display_score()
