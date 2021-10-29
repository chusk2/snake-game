from turtle import Turtle
from food import Food

class Segment(Turtle):
    def __init__(self, posx, posy):
        super().__init__()
        self.color('green', 'green')
        self.shape('square')
        # self.x_direct = +1
        # self.y_direct = 0
        self.posx = posx
        self.posy = posy
        self.penup()
        self.goto(self.posx, self.posy)
        self.turning_points = []

    def check_crossing_margin(self, limit):
        """ check if segment is crossing a border. If so, transport it
        to opposite border, maintaining orientation"""
        self.speed(0)
        self.hideturtle()
        posx = self.xcor()
        posy = self.ycor()

        # Dimensions of canvas
        max_posx = limit - 10
        min_posx = - limit + 10
        max_posy = limit - 10
        min_posy = - limit + 10

        if posx > max_posx:
            self.goto(min_posx, posy)
        # crossing the left side
        elif posx < min_posx:
            self.goto(max_posx, posy)
        # crossing the upper side
        elif posy > max_posy:
            self.goto(posx, min_posy)
        # crossing the bottom side
        elif posy < min_posy:
            self.goto(posx, max_posy)

        self.speed(3)
        self.showturtle()

    def rotate_segment(self, direction):
        """ changes the orientation of the segment"""

        # moving horizontal
        if self.heading() in [0, 180]:
            # moving left
            if direction == 'up':
                self.setheading(90)
            elif direction == 'down':
                self.setheading(270)

        # moving vertical
        elif self.heading() in [90, 270]:
            if direction == 'left':
                self.setheading(180)

            elif direction == 'right':
                self.setheading(0)

    def move_segment(self):
        # if there are rotations still to be carried out

        if self.turning_points:

            # turning point: [head position, direction]
            first_turn = self.turning_points[0]
            head_position = first_turn[0]
            direction = first_turn[1]

            # if segment has reached earliest turning point, rotate it
            if self.position() == head_position:
                self.rotate_segment(direction)
                # IMPORTANT: REMOVE TURNING POINT FROM LIST ONLY IF
                # THE TURN WAS MADE!!!
                # remove the turning point from segment's turning list
                del self.turning_points[0]
        self.forward(20)


class Snake:
    def __init__(self, snake_size, canvas_size):
        self.pieces = []
        self.snake_size = snake_size
        self.limit = canvas_size
        self.apple = Food(self.limit)
        # print('Starting coordinates of segments: ', end='')
        for i in range(self.snake_size, 0, -1):
            start_pos = 20 * i - 10
            self.pieces.append(Segment(posx=start_pos, posy=10))
            # paint in blue the head of snake
            if i == self.snake_size:
                self.pieces[0].color('blue')
        # self.pieces_position = []
        # for i in self.pieces:
        #     self.pieces_position.append(i.position())
        # self.write_position(self.pieces_position)

    def new_tail(self):
        tail = self.pieces[-1]
        posx = tail.pos()[0]
        posy = tail.pos()[1]
        # determine orientation
        if tail.heading() == 0:  # going left
            new_x = posx - 20
            new_y = posy
        elif tail.heading() == 180:  # going right
            new_x = posx + 20
            new_y = posy
        elif tail.heading() == 90:  # going up
            new_x = posx
            new_y = posy - 20
        elif tail.heading() == 270:  # going down
            new_x = posx
            new_y = posy + 20
        # add the new tail at new position
        self.pieces.append(Segment(new_x, new_y))
        new_tail = self.pieces[-1]
        # set heading of new tail to follow snake body
        new_tail.setheading(tail.heading())
        # make new_tail to turn at designed points
        if tail.turning_points:
            new_tail.turning_points = tail.turning_points


    def move(self):  # move the whole snake
        for index, piece in enumerate(self.pieces):
            # check if the head eats the apple
            if index == 0 and self.apple.eaten_food(piece.position()):
                    print('Match')
                    self.new_tail()
                    self.apple.move()
            piece.move_segment()
            # self.pieces_position[index] = piece.position()
            piece.check_crossing_margin(self.limit)

    def return_position(self):
        print(f'Head: {self.pieces[0].position()[0]:.0f},'
              f'{self.pieces[0].position()[1]:.0f}', end=' - ')
        print(f'Apple: {self.apple.return_position()}')

    def write_position(self, content):
        with open('positions.txt', 'a') as file:
            file.writelines(f'{str(content)}\n')

    def turn_snake(self, pressed_key):
        """creates a new turning point for the snake.
        There may be various turning points before the whole snake is completely straight.
        For that case, turning_points are added to a list so when every segment reaches
        a turning point, the segment changes its orientation and so on until
        all the turnings have been carried out"""

        def make_turning_point(head_position, key):
            # turning point: [head position, direction]
            # add the turning point to list of turning points
            # to be carried out by the segment
            for i in self.pieces:  # every segment gets a rotate order
                i.turning_points.append([head_position, key])

        # check if it is possible to turn in the entered direction
        head_snake = self.pieces[0]
        head_snake_pos = head_snake.position()

        # moving horizontally
        if head_snake.heading() in [0, 180] and \
                pressed_key in ['up', 'down']:
            make_turning_point(head_snake_pos, pressed_key)
        # moving horizontally
        elif head_snake.heading() in [90, 270] and \
                pressed_key in ['left', 'right']:
            make_turning_point(head_snake_pos, pressed_key)
