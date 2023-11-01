from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        high_score_file = open('high_score_store.txt')
        self.high_score = int(high_score_file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Your Score: {self.score} | High Score: {self.high_score}", align="center",
                   font=("Arial", 20, "normal"))

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score_store.txt', mode='w') as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.display_score()
