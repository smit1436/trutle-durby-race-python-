from turtle import Turtle, Screen
import random

is_race_on = True
random_pace = [5, 6, 7]
color = ["red", "blue", "green", "orange", "purple", "brown"]
screen = Screen()
screen.setup(height=400, width=500)
y_position = [-70, -40, -10, 20, 50, 80]

all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtle.append(new_turtle)

user_bet = Screen().textinput(title="select the color to bet", prompt="enter the color name to bet: ")

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print("you won")

            else:
                print(f"you lose, {wining_color} is winner")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
