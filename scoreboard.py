from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        # self.high_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score : {self.high_score}", align= ALIGNMENT, font= FONT)

    def reset_score(self):
        if self.score > self.high_score :
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            # self.score
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !", align= ALIGNMENT, font= FONT)

    def refresh_score(self):
        self.score += 1
        self.update_score()