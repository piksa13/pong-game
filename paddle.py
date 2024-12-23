from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.position = position
        self.goto(self.position[0], self.position[1])


    def up(self):
        new_y = self.position[1] + 20
        self.goto(self.position[0], new_y)

    def down(self):
        new_y = self.position[1] - 20
        self.goto(self.position[0], new_y)