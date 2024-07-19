from turtle import Turtle
MOVE_DIS = 10
POS = (0, -280)


class Turtle_Creation(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(POS)
        self.setheading(90)

    def go_up(self):
        self.fd(MOVE_DIS)

    def refresh(self):
        self.goto(POS)