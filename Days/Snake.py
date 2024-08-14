from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

BODY_PARTS = 3

# Create Snake class
class Snake():

    def __init__(self):
        # Create Snake body
        self.snake_body = []
        self.x_coords = 0
        self.create_body()
        self.head = self.snake_body[0]

    def create_body(self):
        for position in range(BODY_PARTS):
            self.add_body(position)

    def add_body(self, position):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(x=self.x_coords, y=0)
        self.x_coords -= 20
        self.snake_body.append(t)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
