from turtle import Turtle

FONT = ("courier", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.cur_score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.cur_score} High Score: {self.high_score}", align= "center" ,font= FONT)
        
    def reset(self):
        if self.cur_score > self.high_score:
            self.high_score = self.cur_score
        self.cur_score = 0
        self.write_score()
        with open("data.txt", "w") as data:
            data.write(f"{self.high_score}")

        