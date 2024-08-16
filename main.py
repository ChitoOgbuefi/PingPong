from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from lives import Lives
from divider import Divider


screen = Screen()
screen.setup(800, 600)
screen.title("PingPong")
screen.bgcolor("black")
screen.tracer()

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
lives = Lives()
divider = Divider()


screen.listen()
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.xcor() > 380:
        ball.reset_ball()
        ball.x_bounce()
        lives.l_live_decrease()
        ball.speed_reset()
    if ball.xcor() < -380:
        ball.reset_ball()
        ball.x_bounce()
        lives.r_live_decrease()
        ball.speed_reset()
    if ball.distance(l_paddle) < 80 and ball.xcor() < -330 or ball.distance(r_paddle) < 80 and ball.xcor() > 330:
        ball.x_bounce()
        ball.increase_speed()
    if lives.l_lives == 0 or lives.r_lives == 0:
        game_is_on = False


if lives.l_lives == 0:
    winner = "Left user"
elif lives.r_lives == 0:
    winner = "Right user"
else:
    winner = "No one"

lives.game_over(winner)

screen.exitonclick()
