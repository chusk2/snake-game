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

# draw margins
x = Turtle()
x.pencolor('blue')
x.penup()
x.goto(-size, -size)
x.pendown()
for i in range(4):
    x.forward(size)
    x.left(90)
x.hideturtle()

# create grid
number_turtles = 2 * size // 20
for i in range(number_turtles):
    t = Turtle()
    t.penup()
    t.goto(-size + 20*i, -size)
    t.pendown()
    t.goto(t.xcor(), size)
    t.hideturtle()