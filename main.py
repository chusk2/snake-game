import time
from turtle import Turtle, Screen
from snake import Snake
scr = Screen()
scr.setup(height=800, width=800)
# scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)


def create_grid(dimensions):
    scr.tracer(0)
    number_turtles = 2 * dimensions // 20
    for i in range(number_turtles+1):  # +1 to fill the borders of grid
        x_t = Turtle()  # turtle to draw horizontal lines
        y_t = Turtle()  # turtle to draw vertical lines
        x_t.pencolor('black')
        y_t.pencolor('black')
        # set turtles in their starting positions without painting
        x_t.penup()
        y_t.penup()
        # starting positions
        y_t.goto(-dimensions + 20 * i, -dimensions)  # vertical lines
        x_t.goto(-dimensions, -dimensions + 20 * i)  # horizontal lines
        x_t.pendown()
        y_t.pendown()
        # draw lines until end of canvas
        x_t.goto(dimensions, x_t.ycor())
        y_t.goto(y_t.xcor(), dimensions)
        x_t.hideturtle()
        y_t.hideturtle()


def start_game():

    scr.clearscreen()
    # Dimensions of canvas
    dimensions = 300
    max_posx = dimensions - 20
    min_posx = - dimensions + 20
    max_posy = dimensions - 20
    min_posy = - dimensions + 20
    margins = [min_posx, min_posy, max_posx, max_posy]

    create_grid(dimensions)

    scr.update()

    # create a snake of size 3 and restrain its movement
    # to the margins of the canvas
    snk = Snake(10, margins)

    # Event listeners
    scr.onkeypress(lambda: snk.turn_snake('up'), 'Up')
    scr.onkeypress(lambda: snk.turn_snake('down'), 'Down')
    scr.onkeypress(lambda: snk.turn_snake('left'), 'Left')
    scr.onkeypress(lambda: snk.turn_snake('right'), 'Right')
    scr.onkeypress(snk.return_position, 'p')
    scr.onkeypress(snk.move, 'space')
    scr.onkeypress(start_game, 's')
    scr.listen()

    while True:
        snk.move()
        scr.update()
        time.sleep(0.1)
    scr.onkeypress()


start_game()
