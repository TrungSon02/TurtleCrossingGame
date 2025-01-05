from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10 #10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.forward(-MOVE_DISTANCE)

    def cross_success(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)
            return True

