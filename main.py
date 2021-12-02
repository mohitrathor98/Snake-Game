from turtle import Turtle, Screen
import time

from snake import Snake

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0)  # now screen will get updated only when update is called

'''
TODO:

-- Create a snake body == done
-- Move the snake == done
-- control the snake
-- create snake food
-- detect collision with food
-- create a scoreboard
-- detect collision with wall
-- detect collision with tail

'''

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# moving snake body
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()