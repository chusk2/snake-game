import time
from turtle import Turtle, Screen

scr = Screen()
scr.setup(height=1000, width=1000)
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

# Dimensions of canvas
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


def get_orientation(snake):
	head = snake[0]
	tail = snake[-1]
	head_x = head.position()[0]
	head_y = head.position()[1]
	tail_x = tail.position()[0]
	tail_y = tail.position()[1]
	x_axis = 0
	y_axis = 0
	# moving vertical
	if head_x == tail_x:
		if head_y > tail_y:
			y_axis = +1
		elif head < tail_y:
			y_axis = -1
		orientation = [0, y_axis]
		return orientation

	# moving horizontal
	elif head_y == tail_y:
		if head_x > tail_x:
			x_axis = +1
		elif head_x < tail_x:
			x_axis = -1
		orientation = [x_axis, 0]
		return orientation


def move_snake():

	for i in snake:
		posx = i.position()[0]
		posy = i.position()[1]
		direction = get_orientation(snake)
		x_direc = direction[0]
		y_direc = direction[1]

		if y_direc == 0:  # moving horizontal
			# return to left margin of canvas
			if x_direc == +1 and posx == max_posx:  # going righwards
				i.goto(min_posx, posy)
			# return to right margin of canvas
			elif x_direc == -1 and posx == min_posx:  # going leftwards
				i.goto(max_posx, posy)
			# limits not reached, just move on
			else:
				i.forward(20)

		if x_direc == 0:  # moving vertical
			# return to bottom margin of canvas
			if y_direc == +1 and posy == max_posy:  # going upwards
				i.goto(posx, min_posy)
			# return to right margin of canvas
			elif y_direc == -1 and posy == min_posy:  # going downwards
				i.goto(posx, max_posy)
			# limits not reached, just move on
			else:
				i.forward(20)

	scr.update()
	time.sleep(0.1)


def turn_segment(segment, direction, key):
	# left: 	x_direct + -1
	# right:	x_direct = +1
	# up:		y_direct = +1
	# down:		y_direct + -1

	x_direct = direction[0]
	y_direct = direction[1]

	# moving horizontal
	if y_direct == 0:
		# moving left
		if x_direct == -1:  # left
			if key == 'up':
				segment.right(90)
			elif key == 'down':
				segment.left(90)
		# moving right
		elif x_direct == +1:  # right
			if key == 'up':
				segment.left(90)
			elif key == 'down':
				segment.right(90)
	# moving vertical
	elif x_direct == 0:
		# moving up
		if y_direct == 1:  # up
			if key == 'left':
				segment.left(90)
			elif key == 'right':
				segment.right(90)
		# moving down
		elif y_direct == -1:  # down
			if key == 'left':
				segment.right(90)
			elif key == 'right':
				segment.left(90)


def move_up():
	# can move upwards only if moving horizontally
	direc = get_orientation(snake)
	x_direc = direc[0]
	y_direc = direc[1]
	key = 'up'  # key pressed is 'up' arrow
	head_pos = snake[0].position()
	if y_direc == 0:  # moving horizontal

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					turn_segment(i, direc, 'up')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					turn_segment(i, direc, 'up')
			scr.update()
			time.sleep(0.1)


def move_down():
	# can move upwards only if moving horizontally
	direc = get_orientation(snake)
	x_direc = direc[0]
	y_direc = direc[1]
	key = 'down'  # key pressed is 'up' arrow
	head_pos = snake[0].position()
	if y_direc == 0:  # moving horizontal

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					turn_segment(i, direc, 'down')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					turn_segment(i, direc, 'down')
			scr.update()
			time.sleep(0.1)


def move_left():
	# can move upwards only if moving vertically
	direc = get_orientation(snake)
	x_direc = direc[0]
	y_direc = direc[1]
	key = 'left'  # key pressed is 'left' arrow
	head_pos = snake[0].position()
	if x_direc == 0:  # moving vertical

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					turn_segment(i, direc, 'left')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					turn_segment(i, direc, 'left')
			scr.update()
			time.sleep(0.1)


def move_right():
	# can move upwards only if moving vertically
	direc = get_orientation(snake)
	x_direc = direc[0]
	y_direc = direc[1]
	key = 'right'  # key pressed is 'left' arrow
	head_pos = snake[0].position()
	if x_direc == 0:  # moving vertical

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					turn_segment(i, direc, 'right')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					turn_segment(i, direc, 'right')
			scr.update()
			time.sleep(0.1)


for k in range(snake_size):
	snake[k].shape('square')
	snake[k].color('green')
	snake[k].penup()
	# move each block 20px backwards
	snake[k].goto(-20 * k, 0)
	snake[0].color('blue')

# Event listeners
scr.onkeypress(move_up, 'Up')
scr.onkeypress(move_down, 'Down')
scr.onkeypress(move_left, 'Left')
scr.onkeypress(move_right, 'Right')
scr.listen()


while True:
	move_snake()


scr.exitonclick()
