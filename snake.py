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
direction = 'E'


def move_snake():
	for i in snake:
		i.forward(20)
	scr.update()
	time.sleep(0.1)


def move_up():

	# can move upwards only if moving horizontally
	if direction in ['E', 'W']:

		head_posx = snake[0].position()[0]

		for step in range(len(snake)):
			for i in snake:
				# check if segment is at turning point
				if i.position()[0] == head_posx:
					# turn direction
					if direction == 'E':
						i.setheading(90)
					elif direction == 'W':
						i.setheading(0)
				# move forward once it has turned or not
				i.forward(20)

			scr.update()
			time.sleep(0.1)


def move_down():

	# can move upwards only if moving horizontally
	if direction in ['E', 'W']:

		head_posx = snake[0].position()[0]

		for step in range(len(snake)):
			for i in snake:
				# check if segment is at turning point
				if i.position()[0] == head_posx:
					# turn direction
					if direction == 'E':
						i.setheading(270)
					elif direction == 'W':
						i.setheading(180)
				# move forward once it has turned or not
				i.forward(20)
			scr.update()
			time.sleep(0.1)


for i in range(snake_size):
	snake[i].shape('square')
	snake[i].color('white')
	snake[i].penup()
	# move each block 20px backwards
	snake[i].goto(-20*i, 0)

scr.onkeypress(move_up, 'Up')
scr.onkeypress(move_down, 'Down')
scr.listen()


while True:
	move_snake()


scr.exitonclick()
