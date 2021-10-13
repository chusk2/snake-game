from turtle import Turtle, Screen

src = Screen()
src.setup(height=600, width=600)
src.bgcolor('black')
src.title('Snake Game')

# create three segments of turtle
snake_size = 3

# class Block(Turtle):
# 	def __init__(self):
# 		self.shape('square')
# 		self.color('white')
# 		self.penup()
# 		self.posx = 0
# 		self.posy = 0
# 		self.pos = [self.posx, self.posy]


snake = [Turtle() for i in range(snake_size)]
for i in range(snake_size):
	snake[i].shape('square')
	snake[i].color('white')
	snake[i].penup()
	# move each block 20px backwards
	snake[i].goto(-20*i,0)

src.exitonclick()