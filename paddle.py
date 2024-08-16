from turtle import Turtle

PADDLE_WIDTH = 4
PADDLE_LENGTH = 1
PADDLE_1 = -350
PADDLE_2 = 350


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(PADDLE_WIDTH, PADDLE_LENGTH)
        self.goto(position, 0)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)







