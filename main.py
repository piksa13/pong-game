import re
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong game")
screen.tracer(0) #turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

game_is_on = True

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    #Collision with the top/ bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Collision with paddles
    if ball.distance(r_paddle ) < 50 and ball.xcor() > 320 or ball.distance(l_paddle ) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect missing paddle
    if ball.distance(r_paddle ) > 50 and ball.xcor() > 320 or ball.distance(l_paddle ) > 50 and ball.xcor() < -320:
        ball.reset_position()

screen.exitonclick()