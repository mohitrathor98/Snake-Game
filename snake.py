from turtle import Turtle

MOVE_DISTANCE = 20
INTIAL_COORDINATES = [(0,0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snake = []
        self.create()
        self.head = self.snake[0]
        
    def create(self):
        for pos in INTIAL_COORDINATES:
            self.add_segment(pos)
        
    def add_segment(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.snake.append(s)
        
    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create()
        self.head = self.snake[0]
    
    def extend(self):
        # extends body of snake
        self.add_segment(self.snake[-1].position())
    
            
    def move(self):
        
        for s_num in range(len(self.snake)-1, 0, -1):
            # 3rd square goes to 2nd square position
            # and 2nd goes to 1st ones
            new_x = self.snake[s_num-1].xcor()
            new_y = self.snake[s_num-1].ycor()
            self.snake[s_num].goto(new_x, new_y)
        # 1st square moves forward    
        self.snake[0].forward(MOVE_DISTANCE)     
        
    def up(self):
        # if snake is going down then it can't 
        # move suddenly up. It should go 
        # left/right then up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)      