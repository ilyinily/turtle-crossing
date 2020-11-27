from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.color("red")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def goal_reached(self):
        if self.position()[1] == FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True

