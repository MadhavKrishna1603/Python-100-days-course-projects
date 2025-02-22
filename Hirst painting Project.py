import turtle
from turtle import Turtle,Screen
import random
screen = Screen()
timmy = Turtle()

turtle.colormode(255)

color = [(239, 233, 75), (209, 161, 103), (226, 70, 133), (217, 155, 10), (176, 78, 24), (204, 136, 186), (115, 168, 236), (224, 235, 2), (79, 177, 36), (72, 98, 224), (238, 164, 193), (69, 34, 26), (51, 120, 42), (241, 53, 32), (151, 66, 140), (132, 197, 131), (188, 20, 9), (52, 101, 150), (207, 6, 52), (149, 217, 173), (155, 184, 242), (24, 95, 22), (240, 172, 162), (138, 214, 234), (84, 72, 38), (65, 42, 151)]
timmy.up()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
for i in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

screen.exitonclick()
