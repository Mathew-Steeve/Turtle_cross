import time
from turtle import Screen
from turtle_creation import Turtle_Creation
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
turtle = Turtle_Creation()
game_is_on = True

screen.listen()
screen.onkey(turtle.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()











screen.exitonclick()
