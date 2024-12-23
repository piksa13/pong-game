from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")

paddle = Paddle()

screen.listen()
screen.onkey(fun=paddle.up, key="Up")
screen.onkey(fun=paddle.down, key="Down")


screen.exitonclick()