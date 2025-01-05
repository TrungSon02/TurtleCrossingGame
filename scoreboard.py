from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 0
        self.highest_score = 0
        self.check_highest_score()
        self.goto(-180,250)
        self.write("Current Score: 0",align="center",font=FONT)


    def add_score(self):
        self.score +=1
        self.change_highest_score()
        self.clear()
        self.goto(180, 250)
        self.write(f"Highest Score: {self.highest_score}", align="center", font=FONT)
        self.goto(-180, 250)
        self.write(f"Current Score: {self.score}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
        self.change_highest_score()

    def check_highest_score(self):
        with open("high_score.txt") as file:
            try:
                self.highest_score = int(file.read())
            except ValueError:
                pass
        self.goto(180,250)
        self.write(f"Highest Score: {self.highest_score}",align="center",font=FONT)


    def change_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.highest_score}")

