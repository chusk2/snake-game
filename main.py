from turtle import Turtle, Screen

scr = Screen()
scr.setup(height=800, width=800)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

# Dimensions of canvas
size = 260
max_posx = size - 20
min_posx = - size + 20
max_posy = size - 20
min_posy = - size + 20

# create grid
number_turtles = 2 * size // 20
for i in range(number_turtles+1):  # +1 to fill the borders of grid
    x_t = Turtle()  # turtle to draw horizontal lines
    y_t = Turtle()  # turtle to draw vertical lines
    x_t.pencolor('blue')
    y_t.pencolor('blue')
    # set turtles in their starting positions without painting
    x_t.penup()
    y_t.penup()
    # starting positions
    y_t.goto(-size + 20*i, -size)  # vertical lines
    x_t.goto(-size, -size + 20 * i)  # horizontal lines
    x_t.pendown()
    y_t.pendown()
    # draw lines until end of canvas
    x_t.goto(size, x_t.ycor())
    y_t.goto(y_t.xcor(), size)
    x_t.hideturtle()
    y_t.hideturtle()

scr.update()
scr.exitonclick()