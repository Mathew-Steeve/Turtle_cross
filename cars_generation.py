from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
DIS = 5
INCREMENT = 10


class Car_Gen:
    def __init__(self):

        self.all_seg = []
        self.car_speed = DIS

    def new_seg(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car_seg = Turtle()
            car_seg.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            car_seg.shape("square")
            car_seg.shapesize(1, 2)
            car_seg.penup()
            car_seg.goto(320, new_y)
            self.all_seg.append(car_seg)

    def move_seg(self):
        for seg in self.all_seg:
            seg.bk(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT
