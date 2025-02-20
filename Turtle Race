from turtle import Turtle,Screen
import random
screen = Screen()
timmy = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
jimmy = Turtle(shape="turtle")
thanku = Turtle(shape="turtle")
thakkudu = Turtle(shape="turtle")
minnu = Turtle(shape="turtle")
colours = ["red","blue","purple","green","yellow","orange"]
user_bet=screen.textinput("Make your bets","Which turtle is gonna win? your Guess: ")
screen.screensize(400,500)
turtles = [timmy,tommy,jimmy,thanku,thakkudu,minnu]
n = -1
for i in turtles:
    n+=1
    i.up()
    i.color(colours[n])
timmy.goto(x=-250,y=-100)
tommy.goto(x=-250,y=-50)
jimmy.goto(x=-250,y=0)
thanku.goto(x=-250,y=50)
thakkudu.goto(x=-250,y=100)
minnu.goto(x=-250,y=150)
screen = Screen()
is_game_on = False
if user_bet:
    is_game_on = True
while is_game_on:

    for j in turtles:
        if j.xcor() > 250:
            win_colour = j.pencolor()
            if win_colour == user_bet.lower():
                print(f"You Win! {j.pencolor()} colour turtle won!")
            else:
                print(f"You Lost! The winner is {j.pencolor()} colour turtle")
            is_game_on = False

        rand_num = random.randint(0, 10)
        j.forward(rand_num)

screen.screensize(400,500)
screen.exitonclick()
