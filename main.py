from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

sc=Screen()
sc.setup(width=600, height=600)
sc.title("SNAKE GAME")
sc.tracer(0)
sc.bgcolor("black")

snake=Snake()
food=Food()
score=Score()

sc.listen()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()
    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    # collision with tail
    for seg in snake.segments[1 : ]:
         if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()






sc.exitonclick()
