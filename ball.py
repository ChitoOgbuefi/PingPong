from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 2
        self.y_move = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.teleport(0,0)
        self.x_bounce()

    def increase_speed(self):
        self.y_move *= 1.1
        self.x_move *= 1.1

    def speed_reset(self):
        self.x_move = 2
        self.y_move = 2





