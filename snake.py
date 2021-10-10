from turtle import Turtle, Screen

src = Screen()
src.setup(height=600, width=600)
src.bgcolor('black')
src.title('Snake Game')

snake = [Turtle() for i in range(3)]
for i in range(3):
	block = snake[i]
	block.shape("square")
	block.color('white')
	# default turtle size is 20px
	block.penup()
	# move each block 20px backwards
	block.setpos(-20*i,0)

src.exitonclick()