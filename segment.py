from turtle import Turtle


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
        # add or sustract 20 px to compensate the following forward(20)
        # crossing the right side
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
        # if posx >= max_posx and self.heading() == 0:
        #     self.goto(min_posx - 20, posy)
        # # crossing the left side
        # elif posx == min_posx and self.heading() == 180:
        #     self.goto(max_posx + 20, posy)
        # # crossing the upper side
        # elif posy == max_posy and self.heading() == 90:
        #     self.goto(posx, min_posy - 20)
        # # crossing the bottom side
        # elif posy == min_posy and self.heading() == 270:
        #     self.goto(posx, max_posy + 20)

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
