from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong game")
screen.tracer(0) #turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_is_on = True

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

while game_is_on:
    screen.update()

screen.exitonclick()