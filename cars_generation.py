from turtle import Turtle
import random


class Car_Gen(Turtle):
    def __init__(self):
        super().__init__()
        self.new_y = random.randint(-300, 300)
        self.new_x = 320
        self.new_seg()

    def new_seg(self):
        self.shape("square")
        self.shapesize(1, 3)
        self.penup()
        self.goto(self.new_x, self.new_y)

    def move_seg(self):
        self.bk(20)
