from turtle import Turtle
PS = (-240, 250)
FN = ('courier', 20, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(PS)
        self.write(f"Level {self.score}", False, ALIGNMENT, FN)
        self.ht()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", False, ALIGNMENT, FN)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over!!', False, ALIGNMENT, FN)
