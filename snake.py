import time
from turtle import Turtle, Screen

scr = Screen()
scr.setup(height=600, width=600)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

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
snake_positions = []
orientation = 'E'

for i in range(snake_size):
	snake[i].shape('square')
	snake[i].color('white')
	snake[i].penup()
	# move each block 20px backwards
	snake[i].goto(-20*i, 0)


def move_snake():
	while True:
		scr.update()
		for i in snake:
			i.forward(20)
		time.sleep(0.1)

def move_vertical(direction):
	# can move upwards only if moving horizontally
	if direction in ['E', 'W']:

		head = snake[0]
		head_pos_x = head.position()[0]

		# set turning direction of snake head
		if direction == 'E':
			head.setheading(90)
		elif direction == 'W':
			head.setheading(0)
		head.forward(20)

		# move rest of snake segments
		while snake[-1].position != head.pos:
			for i in snake[1:]:

				# check if segment is at turning point
				if i.position()[0] != head_pos_x:
					i.forward(20)

				# turn segment direction at turning point
				else:

					if direction == 'E':
						i.setheading(90)
					elif direction == 'W':
						i.setheading(0)

					i.forward(20)


move_snake()

scr.exitonclick()
