from turtle import Turtle


class Segment(Turtle):
    def __init__(self, posx, posy):
        super().__init__()
        self.pencolor('green')
        self.shape('circle')
        self.x_direct = +1
        self.y_direct = 0
        self.posx = posx
        self.posy = posy
        self.penup()
        self.goto(self.posx, self.posy)
        self.turning_points = []

    def check_crossing_margin(self, margins):
        """ check if segment is crossing a border. If so, transport it
        to opposite border, maintaining orientation"""
        self.speed(0)
        self.hideturtle()
        posx = self.xcor()
        posy = self.ycor()

        # margins = [min_x, min_y, max_x, max_y]
        min_posx = margins[0]
        min_posy = margins[1]
        max_posx = margins[2]
        max_posy = margins[3]

        if posx >= max_posx:  # crossing the right side
            self.goto(-max_posx + 10, posy)
        elif posx <= min_posx:  # crossing the left side
            self.goto(max_posx - 10, posy)
        elif posy >= max_posy:  # crossing the upper side
            self.goto(posx, - max_posy + 10)
        elif posy <= min_posy:  # crossing the bottom side
            self.goto(posx, max_posy - 10)

        self.speed(3)
        self.showturtle()

    def rotate_segment(self, direction):
        """ changes the orientation of the segment"""
        # moving horizontal
        if self.y_direct == 0:
            # moving left
            if self.x_direct == -1:  # leftwards
                if direction == 'up':
                    self.right(90)
                    self.x_direct = 0
                    self.y_direct = +1
                elif direction == 'down':
                    self.left(90)
                    self.x_direct = 0
                    self.y_direct = -1
            # moving right
            elif self.x_direct == +1:  # right
                if direction == 'up':
                    self.left(90)
                    self.x_direct = 0
                    self.y_direct = +1
                elif direction == 'down':
                    self.right(90)
                    self.x_direct = 0
                    self.y_direct = -1

        # moving vertical
        elif self.x_direct == 0:
            # moving up
            if self.y_direct == 1:  # up
                if direction == 'left':
                    self.left(90)
                    self.x_direct = -1
                    self.y_direct = 0
                elif direction == 'right':
                    self.right(90)
                    self.x_direct = +1
                    self.y_direct = 0
            # moving down
            elif self.y_direct == -1:  # down
                if direction == 'left':
                    self.right(90)
                    self.x_direct = -1
                    self.y_direct = 0
                elif direction == 'right':
                    self.left(90)
                    self.x_direct = 1
                    self.y_direct = 0

    def move_segment(self):
        # if there are rotations still to be carried out

        if self.turning_points:
            print(self.turning_points)
            # turning point: [head position, direction]
            first_turn = self.turning_points[0]
            head_position = first_turn[0]
            direction = first_turn[1]
            # if segment has reached earliest turning point, rotate it
            if self.position() == head_position:
                self.rotate_segment(direction)
            # remove the turning point from segment's turning list
            self.turning_points.pop()
        self.forward(20)
