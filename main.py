import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING GAME")

screen.tracer(0)
car = CarManager()
screen.update()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="w", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="s", fun=player.move_down)


game_is_on = True
game_speed = 0.04
while game_is_on:
    time.sleep(game_speed)
    screen.update()

    car.move()

    #Check if player hits the cars
    if car.check_distance(player):
        game_is_on = False
        score.game_over()


    # Check if player finishes a level
    if player.cross_success():
        score.add_score()
        if score.score < 5:
            game_speed -= game_speed/10
        elif score.score < 10:
            game_speed -= game_speed/5
        elif score.score < 20:
            game_speed -= game_speed/3
        else:
            game_speed = game_speed/2















screen.exitonclick()