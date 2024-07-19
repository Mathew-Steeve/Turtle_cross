import time
from turtle import Screen
from turtle_creation import Turtle_Creation
from cars_generation import Car_Gen
from score_board import Score
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
car_man = Car_Gen()
turtle = Turtle_Creation()
game_is_on = True
score = Score()
screen.listen()
screen.onkeypress(turtle.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.new_seg()
    car_man.move_seg()

    for car in car_man.all_seg:
        if car.distance(turtle) < 25:
            game_is_on = False
            score.game_over()

    if turtle.ycor() > 300:
        score.update()
        turtle.refresh()
        car_man.level_up()









screen.exitonclick()
