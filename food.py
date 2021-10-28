from turtle import Turtle, Screen
from random import randint


class Food(Turtle):
    def __init__(self, board_size):
        super().__init__()
        self.limit = board_size
        self.shape('circle')
        self.color('red')
        self.x, self.y = 10, 10
        # generate a new random position to start food
        self.penup()
        self.move()

    def move(self):
        # new position must be multiple of 20
        # and initially shifted 10 px in both directions
        new_x = 20 * randint(-10, 10) + 10
        new_y = 20 * randint(-10, 10) + 10
        self.goto(new_x, new_y)

    def return_position(self):
        print(f'Food position: {self.position()}')
