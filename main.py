from turtle import Turtle, Screen, getscreen

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Xenzia')

'''
TODO:

-- Create a snake body
-- Move the snake
-- create snake food
-- detect collision with food
-- create a scoreboard
-- detect collision with wall
-- detect collision with tail

'''

# creating a snake body -- 3 white sqaures with default size
snake = []
for i in range(3):
    t = Turtle("square")
    t.color("white")
    t.setx(-(20.0*i))
    
    snake.append(t)

    
screen.exitonclick()