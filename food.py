from turtle import Turtle, Screen
from random import randint


class Food(Turtle):
    def __init__(self, board_size):
        super().__init__()
        self.limit = board_size
        self.shape('circle')
        self.color('red')
        self.x, self.y = 0, 0
        # generate a new random position to start food
        while self.x == 0 and self.y == 0:
            self.generate_random_pos()
        self.penup()
        self.goto(self.x, self.y)

    def generate_random_pos(self):
        # new position must be multiple of 20
        self.x = 10 * round(randint(-self.limit, self.limit) / 10)
        self.y = 10 * round(randint(-self.limit, self.limit) / 10)

    def move(self):
        self.generate_random_pos()
        self.goto(self.x, self.y)

