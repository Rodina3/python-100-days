import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
speed = 0.2
while game_is_on:
    screen.update()

    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score_board.increase_score()
        if speed > 0.1:
            speed -= 0.02

    if snake.head.xcor() > 280 \
            or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 \
            or snake.head.ycor() < -280:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

score_board.game_over()

screen.exitonclick()
