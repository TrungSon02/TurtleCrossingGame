from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.number_of_car = 15     #15
        self.create_car(1)
        self.create_car(2)
        self.create_section_of_car(1)
        self.create_section_of_car(2)

    def create_car(self, section):
        for i in range(self.number_of_car):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color(random.choice(COLORS))
            turtle.penup()
            turtle.setheading(180)
            turtle.shapesize(stretch_wid=1, stretch_len=3)
            self.car_list.append(turtle)


    def create_section_of_car(self, section_number):
        if section_number % 2 == 1:
            start = 0
        else:
            start = self.number_of_car-1

        for i in range(start, start+self.number_of_car):
            position = random.randint(-250,250) + (section_number-1)*600, random.randint(-200,200)
            condition = True
            while condition and i > 0:
                condition = False
                for car in self.car_list[start:]:
                    if car.distance(position) < 100:
                        position = random.randint(-250, 250) + (section_number - 1) * 600, random.randint(-200, 200)
                        condition = True
                        break
            self.car_list[i].goto(position)

    def move(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -400:
                self.go_back(car)



    def go_back(self,a_car):
        position = random.randint(350,900), random.randint(-200,200)
        condition = True
        while condition:
            condition = False
            for car in self.car_list:
                if car.distance(position) < 100:
                    position = random.randint(350, 900), random.randint(-200, 200)
                    condition = True
                    break
        a_car.goto(position)

    def check_distance(self, player):
        for car in self.car_list:
            # if car.distance(player) < 25:
            # if (abs(car.ycor() - player.ycor()) < 25 and car.distance(player) < 25):
            # if (abs(car.xcor() - player.xcor()) < 25 or abs(car.ycor() - player.ycor()) < 25) and car.distance(player) < 27:
            #     print(abs(car.xcor() - player.xcor()))
            #     print(abs(car.ycor() - player.ycor()))
            #     print(car.distance(player))
            #     return True
            if car.distance(player) < 20:
                print("Case 1")
                print(car.distance(player))
                return True

            if car.distance(player) < 26 and 0 < car.ycor() - player.ycor() < 26:
                print("Case 2")
                print(car.distance(player))
                print(car.ycor() - player.ycor())
                return True

            if car.distance(player) < 27 and 0 < player.ycor() - car.ycor() < 18:
                print("Case 3")
                print(car.distance(player))
                print(player.ycor() - car.ycor())
                return True

            if abs(car.xcor() - player.xcor()) < 40 and car.distance(player) < 35 and abs(car.ycor() - player.ycor()) < 9:
                print("Case 4")
                print(abs(car.xcor() - player.xcor()))
                print(car.distance(player))
                print(abs(car.ycor() - player.ycor()))
                return True