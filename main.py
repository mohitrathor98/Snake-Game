from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

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
-- control the snake == done
-- create snake food == done
-- detect collision with food == done
-- create a scoreboard == done
-- detect collision with wall
-- detect collision with tail

'''

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# moving snake body
game_is_on = True
cur_score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect snake food
    # snake's head is 20*20 in dimension
    # so, we are taking 15 pixels distance 
    # between snake and food as collision
    if snake.head.distance(food) < 15:
        food.refresh()
        cur_score += 1
        score.write_score(cur_score)


screen.exitonclick()