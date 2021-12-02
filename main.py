from turtle import Turtle, Screen, getscreen
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)  # now screen will get updated only when update is called

'''
TODO:

-- Create a snake body == done
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
    s = Turtle("square")
    s.color("white")
    s.penup()
    s.goto(-(20.0*i), 0)
    
    snake.append(s)


# moving snake body
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for s_num in range(len(snake)-1, 0, -1):
        # 3rd square goes to 2nd square position
        # and 2nd goes to 1st ones
        new_x = snake[s_num-1].xcor()
        new_y = snake[s_num-1].ycor()
        snake[s_num].goto(new_x, new_y)
    # 1st square moves forward    
    snake[0].forward(20)
    
screen.exitonclick()