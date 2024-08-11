import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
# tim.color('magenta')
# for _ in range(4): # challenge 1
#     tim.left(90)
#     tim.forward(100)

# Challenge 2
# for _ in range(20):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# Challenge 3
# tim.color(1, .5, .5)
# for n in range(8):
#     angle = 360 / (n+3)
#     tim.color((1.1 * n+1) % 1, (2.7 * n+2) % 1, (1.3 * n + angle) % 1)
#     ang_sum = 0
#     while ang_sum < 360:
#         tim.forward(100)
#         tim.left(angle)
#         ang_sum += angle

# Challenge 4
# paths = ['left', 'right']
# tim.width(5)
# tim.speed(25)
# for n in range(350):
#     tim.color((1.1 * n + 1) % 1, (2.7 * n + 2) % 1, (1.3 * n + random.randint(1, 100)*3.14) % 1)
#     tim.forward(((n+ 1) * random.randint(1, 69)) % 40)
#     direction = random.choice(paths)
#     if direction == 'left':
#         tim.left(((n+1) * random.randint(1, 100)) % 180)
#     else:
#         tim.right(((n+1) * random.randint(1, 100)) % 180)


# Challenge 5
# tim.speed(100)
# angle = 1
# for n in range(350):
#     tim.circle(120, 360, 100)
#     tim.left(angle % 360)
#     tim.forward(10)
#     angle += 1

















# Hurst Painting Project
import colorgram
rgb_colors = []

colors = colorgram.extract('/Users/bdogellis/Library/Mobile Documents/com~apple~CloudDocs/Documents/Career Building/Projects/Udemy/100_Days_of_Code_Udemy/Hurst_Spot_Painting.jpg', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

t.colormode(255)
# 10x10 dots, 50 paces apart
direction = 1
for _ in range(10):  # cols
    for _ in range(10):  # rows
        tim.dot(10, random.choice(rgb_colors))
        tim.penup()
        tim.forward(30)
        tim.pendown()
    tim.dot(10, random.choice(rgb_colors))
    if direction % 2 == 0:
        tim.right(90)
        tim.penup()
        tim.forward(30)
        tim.right(90)
        tim.pendown()
    else:
        tim.left(90)
        tim.penup()
        tim.forward(30)
        tim.left(90)
        tim.pendown()
    direction += 1


screen = Screen()
screen.exitonclick()