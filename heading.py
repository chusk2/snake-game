from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()


def get_heading():
    print(f'Heading: {tim.heading()}')


def move():
    tim.forward(20)


def move_up():
    tim.setheading(90)


def move_down():
    tim.setheading(270)


def move_left():
    tim.setheading(180)


def move_right():
    tim.setheading(0)


scr.onkeypress(get_heading, 'h')
scr.onkeypress(move, 'space')
scr.onkeypress(move_up, 'Up')
scr.onkeypress(move_down, 'Down')
scr.onkeypress(move_left, 'Left')
scr.onkeypress(move_right, 'Right')
scr.listen()

scr.exitonclick()
