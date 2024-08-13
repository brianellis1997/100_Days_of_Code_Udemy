from turtle import Turtle, Screen
import numpy as np

tim = Turtle()
screen = Screen()

# angle = 0
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def counter_clock():
#     tim.left(10)
#
# def clock():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key = 'w', fun = move_forwards)
# screen.onkey(key = 's', fun = move_backwards)
# screen.onkey(key = 'a', fun = counter_clock)
# screen.onkey(key = 'd', fun = clock)
# screen.onkey(key = 'c', fun = clear)

# Turtle Racing
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
start_y = -100

# Tim already initialized
tim.penup()
tim.shape('turtle')
tim.goto(x=-230, y=start_y)
tim.color(user_bet)
colors.remove(user_bet)
turtles = [tim]

for i in range(len(colors)):
    start_y += 40
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors.pop())
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y)
    turtles.append(new_turtle)

finish = [-230] * len(turtles)
is_racing = False

if user_bet:
    is_racing = True

while is_racing:
    for i, t in enumerate(turtles):
        dist = np.random.randint(0, 10)
        t.forward(dist)
        finish[i] += dist
        if finish[i] >= 200:
            winner = t.pencolor()
            is_racing = False

user_won = user_bet == winner

if user_won:
    print(f"Congrats! You're bet was correct, the {winner} turtle won!")
else:
    print(f"Sorry, you lost your bet. The {winner} turtle won.")



screen.exitonclick()
