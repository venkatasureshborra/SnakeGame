from turtle import Turtle
ALIGNMENT="center"
FONT=("courier", 20, "bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.goto(0, 270)
        self.color("white")
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score> self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.score_update()

    def  increase_score(self):
        self.score+=1
        self.score_update()

