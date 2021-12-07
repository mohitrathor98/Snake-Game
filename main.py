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
        score.cur_score += 1
        snake.extend()
        score.write_score()

    # detect collision with wall
    # here assuming after 290 px, snake will hit the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        
    # detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()