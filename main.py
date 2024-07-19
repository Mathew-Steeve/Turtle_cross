import time
from turtle import Screen
from turtle_creation import Turtle_Creation
from cars_generation import Car_Gen

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
car = Car_Gen()
turtle = Turtle_Creation()
game_is_on = True

screen.listen()
screen.onkey(turtle.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_seg()











screen.exitonclick()
