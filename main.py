import re
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong game")
screen.tracer(0) #turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Collision with the top/ bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddles
    if ball.distance(r_paddle ) < 50 and ball.xcor() > 320 or ball.distance(l_paddle ) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect missing right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    #Detect missing left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()

screen.exitonclick()