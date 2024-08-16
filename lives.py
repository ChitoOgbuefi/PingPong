from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_lives = 3
        self.r_lives = 3
        self.update_scoreboard()

    def r_live_decrease(self):
        self.r_lives -= 1
        self.update_scoreboard()

    def l_live_decrease(self):
        self.l_lives -= 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.r_lives, True, "center", ("Fantasy", 40, "normal"))
        self.goto(100, 250)
        self.write(self.l_lives, True, "center", ("Fantasy", 40, "normal"))

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"GAME OVER! {winner} has won!", False, "center", ("Fantasy", 25, "normal"))






