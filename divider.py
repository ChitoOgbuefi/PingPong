from turtle import Turtle


class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for num in range(300, -300, -20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)