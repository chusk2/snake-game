import time
from turtle import Turtle, Screen

scr = Screen()
scr.setup(height=800, width=800)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

# Dimensions of canvas
width = 260
height = 260
# width = scr.screensize()[0]
# height = scr.screensize()[1]
max_posx = width - 20
min_posx = - width + 20
max_posy = height - 20
min_posy = - height + 20

# draw margins
x = Turtle()
x.pencolor('blue')
x.penup()
x.goto(-width, -height)
x.pendown()
x.goto(-width, height)
x.right(90)
x.goto(width, height)
x.right(90)
x.goto(width, - height)
x.right(90)
x.goto(-width, -height)
x.hideturtle()

# West  = setheading(0)
# East  = setheading(180)
# North = setheading(90)
# South = setheading(270)

# define the segment object

class Segment(Turtle, posx, posy):
	def __init__(self):
		super().color('blue')
		super().shape('square')
		self.x_direct = +1
		self.y_direct = 0
		self.posx = posx
		self.posy = posy
		super().penup()
		self.goto(self.posx, self.posy)

	def cross_margin(self, side):
		if side == 'left':
			posx = max_posx -10
			self.goto(self.posx, self.posy)
		elif side == 'right':
			posx = - max_posx + 10
			self.goto(self.posx, self.posy)
		elif side == 'up':
			self.posy = - max_posy + 10
			self.goto(self.posx, self.posy)
		elif side == 'down':
			self.posy = max_posy - 10
			self.goto(self.posx, self.posy)
		
	def turn(self, direction, key):
		# HLWU: moving horizontally LEFTWARDS and then turn UP
		# HLWU: moving horizontally LEFTWARDS and then turn DOWN
		# HRWU: moving horizontally RIGHTWARDS and then turn UP
		# HRWD: moving horizontally RIGHTWARDS and then turn DOWN

		# VUWL: moving vertically UPWARDS and then turn LEFT
		# VUWR: moving vertically UPWARDS and then turn RIGHT
		# VDWL: moving vertically DOWNWARDS and then turn LEFT
		# VDWR: moving vertically DOWNWARDS and then turn RIGHT

		# movements = {'HLWU': ['R', (0, -1)], 'HLWD': ['L', (0, -1)],
		# 			'HRWU': ['L', (0, 1)], 'HRWD': ['R', (0, 1)],
		# 			'VUWL': ['L', (-1, 0)], 'VUWR': ['R', (1, 0)],
		# 			'VDWL': ['R', (-1, 0)],  'VDWR': ['L', (1, 0)],
		# 			}

		# moving horizontal
		if self.y_direct == 0:
			# moving left
			if self.x_direct == -1:  # leftwards
				if key == 'up':
					self.right(90)
					self.x_direct = 0
					self.y_direct = +1
				elif key == 'down':
					self.left(90)
					self.x_direct = 0
					self.y_direct = -1
			# moving right
			elif self.x_direct == +1:  # right
				if key == 'up':
					self.left(90)
					self.x_direct = 0
					self.y_direct = +1
				elif key == 'down':
					self.right(90)
					self.x_direct = 0
					self.y_direct = +1

		# moving vertical
		elif self.x_direct == 0:
			# moving up
			if self.y_direct == 1:  # up
				if key == 'left':
					self.left(90)
					if self == snake[0]:
						self.x_direct = -1
						self.y_direct = 0
				elif key == 'right':
					self.right(90)
					if self == snake[0]:
						self.x_direct = +1
						self.y_direct = 0
			# moving down
			elif self.y_direct == -1:  # down
				if key == 'left':
					self.right(90)
					self.x_direct = -1
					self.y_direct = 0
				elif key == 'right':
					self.left(90)
					self.x_direct = 1
					self.y_direct = 0

# create three segments of turtle
snake_size = 4

snake = [Turtle() for i in range(snake_size)]
# def get_orientation(snk):
# 	head = snk[0]
# 	prehead = snk[1]
# 	head_x = head.position()[0]
# 	head_y = head.position()[1]
# 	prehead_x = prehead.position()[0]
# 	prehead_y = prehead.position()[1]
# 	x_axis = 0
# 	y_axis = 0
# 	# moving vertical
# 	if head_x == prehead_x:
# 
# 		if head_y > prehead_y:
# 			y_axis = +1
# 			return [x_axis, y_axis]
# 		elif head_y < prehead_y:
# 			y_axis = -1
# 			return [x_axis, y_axis]
# 	# moving horizontal
# 	elif head_y == prehead_y:
# 
# 		if head_x > prehead_x:
# 			x_axis = +1
# 			return [x_axis, y_axis]
# 		elif head_x < prehead_x:
# 			x_axis = -1
# 			return [x_axis, y_axis]
# 	else:
# 		return [0, 0]


def move_to_margin(block, side):
	block.speed(0)
	block.hideturtle()
	block.goto(side[0], side[1])
	block.speed(3)
	block.showturtle()


def move_snake():
	# direction = get_orientation(snake)
	x_direc = direction[0]
	y_direc = direction[1]
	for i in snake:
		posx = i.position()[0]
		posy = i.position()[1]

		

		i.forward(20)

	scr.update()
	print(f'X orientation: {x_direc}, Y orientation: {y_direc}')
	for i in snake:
		print(i.position(), end=' ')
	print('\n')
	time.sleep(0.1)

# start moving horizontal rightwards
# x_direc = +1
# y_direc = 0


direction = [+1, 0]


def turn_segment(segment, direct, key):
	# left: 	x_direct + -1
	# right:	x_direct = +1
	# up:		y_direct = +1
	# down:		y_direct + -1

	x_direct = direct[0]
	y_direct = direct[1]


	return direct


def move_up():
	# can move upwards only if moving horizontally
	# direc = get_orientation(snake)
	y_direc = direction[1]
	head_pos = snake[0].position()
	if y_direc == 0:  # moving horizontal

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					direction = turn_segment(i, direc, 'up')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					direction = turn_segment(i, direc, 'up')
			scr.update()
			time.sleep(0.1)


def move_down():
	# can move upwards only if moving horizontally
	direc = get_orientation(snake)
	y_direc = direc[1]
	head_pos = snake[0].position()
	if y_direc == 0:  # moving horizontal
		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					direction = turn_segment(i, direc, 'down')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					direction = turn_segment(i, direc, 'down')
			scr.update()
			time.sleep(0.1)


def move_left():
	# can move upwards only if moving vertically
	direc = get_orientation(snake)
	x_direc = direc[0]
	head_pos = snake[0].position()
	if x_direc == 0:  # moving vertical

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					direction = turn_segment(i, direc, 'left')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					direction = turn_segment(i, direc, 'left')
			scr.update()
			time.sleep(0.1) 


def move_right():
	# can move upwards only if moving vertically
	direc = get_orientation(snake)
	x_direc = direc[0]
	head_pos = snake[0].position()
	if x_direc == 0:  # moving vertical

		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					direction = turn_segment(i, direc, 'right')
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					direction = turn_segment(i, direc, 'right')
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
scr.onkeypress(move_snake, 'space')

scr.listen()


# while True:
# 	move_snake()


scr.exitonclick()
