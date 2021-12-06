from turtle import Turtle

FONT = ("courier", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write_score()
        
    def write_score(self, score = 0):
        self.clear()
        self.write(f"Score: {score}", align= "center" ,font= FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font= FONT)