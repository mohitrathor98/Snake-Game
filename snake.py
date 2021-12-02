from turtle import Turtle


class Snake:
    
    def __init__(self):
        self.snake = []
        
        for i in range(3):
            s = Turtle("square")
            s.color("white")
            s.penup()
            s.goto(-(20*i), 0)
            
            self.snake.append(s)
            
    def move(self):
        
        for s_num in range(len(self.snake)-1, 0, -1):
            # 3rd square goes to 2nd square position
            # and 2nd goes to 1st ones
            new_x = self.snake[s_num-1].xcor()
            new_y = self.snake[s_num-1].ycor()
            self.snake[s_num].goto(new_x, new_y)
        # 1st square moves forward    
        self.snake[0].forward(20)            