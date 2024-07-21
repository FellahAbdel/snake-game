from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()


def should_play_again(fun):
    should_play = screen.textinput("Should play", "Do you want to play again ? (Yes/No)").lower()
    if should_play == "yes":
        screen.clear()
        fun()

def play_game():
    screen.title("My snake game")
    screen.bgcolor("green")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    """
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    segments = []
    
    for position  in starting_positions:
        new_segement = Turtle(shape="square")
        new_segement.penup()
        new_segement.color("white")
        new_segement.goto(position)
        segments.append(new_segement)
    
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
    
        for num_of_seg in range(len(segments) - 1, 0, -1):
            new_x = segments[num_of_seg - 1].xcor()
            new_y = segments[num_of_seg - 1].ycor()
            segments[num_of_seg].goto(new_x, new_y)
    
        segments[0].forward(20)
        segments[0].left(90)
    
    """

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()


        # Deteck colision with food
        if snake.head.distance(food) < 18:
            food.refresh()
            snake.increase_segment()
            scoreboard.refresh_score()

        # Detect colision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_score()
            snake.reset_snake()


        # detect colision with its own tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10 :
                scoreboard.reset_score()
                snake.reset_snake()

    screen.exitonclick()

play_game()