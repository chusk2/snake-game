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

half_width = scr.screensize()[0] / 2
half_height = scr.screensize()[1] / 2

max_posx = half_width - 20
min_posx = - half_width + 20

max_posy = half_height -20
min_posy = - half_height +20

# West  = setheading(0)
# East  = setheading(180)
# North = setheading(90)
# South = setheading(270)


def move_snake():

	for i in snake:
		posx = i.position()[0]
		posy = i.position()[1]
		direction = i.heading()
		if direction in [180, 0]:
			# return to left margin of canvas
			if direction == 0 and posx == max_posx:  # going righwards
				i.goto(min_posx, posy)
			# return to right margin of canvas
			elif direction == 180 and posx == min_posx:  # going leftwards
				i.goto(max_posx, posy)
			# limits not reached, just move on
			else:
				i.forward(20)

		if direction in [90, 270]:
			# return to left margin of canvas
			if direction == 90 and posy == max_posy:  # going upwards
				i.goto(posx, min_posy)
			# return to right margin of canvas
			elif direction == 270 and posy == min_posy:  # going downwards
				i.goto(posx, max_posy)
			# limits not reached, just move on
			else:
				i.forward(20)

	scr.update()
	time.sleep(0.1)


def move_up():

	# can move upwards only if moving horizontally
	direction = snake[0].heading()
	if direction in [0, 180]:

		head_posx = snake[0].position()[0]

		for step in range(len(snake)):
			for i in snake:
				# check if segment is at turning point
				if i.position()[0] == head_posx:
					# turn direction
					if direction == 0:
						i.setheading(90)
					elif direction == 180:
						i.setheading(0)
				# move forward once it has turned or not
				i.forward(20)

			scr.update()
			time.sleep(0.1)


def move_down():

	# can move upwards only if moving horizontally
	direction = snake[0].heading()
	if direction in [0, 180]:

		head_posx = snake[0].position()[0]

		for step in range(len(snake)):
			for i in snake:
				# check if segment is at turning point
				if i.position()[0] == head_posx:
					# turn direction
					if direction == 0:
						i.setheading(270)
					elif direction == 180:
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
