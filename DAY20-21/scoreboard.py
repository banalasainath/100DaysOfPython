from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.score += 1

    def game_over(self):
        # since we are expecting the "GAME OVER" to print at the centre of the screen
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))