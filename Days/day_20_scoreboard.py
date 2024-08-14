from turtle import Turtle
import random

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=0, y=260)
        self.write(arg=f"Score: {self.score}".format(self.score), move=False, align='center', font=("Courier", 20, "normal"))
        self.goto(x=55, y=260)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER".format(self.score), move=False, align='center',
                   font=("Courier", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.write_score()


