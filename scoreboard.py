from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.write_score()
        
    def write_score(self, score = 0):
        self.clear()
        self.write(f"Score: {score}")