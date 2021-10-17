import time
from turtle import Turtle, Screen

scr = Screen()
scr.setup(height=800, width=800)
scr.bgcolor('black')
scr.title('Snake Game')
scr.tracer(0)

# create three segments of turtle
snake_size = 4

snake = [Turtle() for i in range(snake_size)]

# Dimensions of canvas
width = 260
height = 260
# size must be multiple of 20 in order to be able to move back to margin
# width = scr.screensize()[0]
# height = scr.screensize()[1]
max_posx = width - 20
print(max_posx)
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


def get_orientation(snk):
	head = snk[0]
	prehead = snk[1]
	head_x = head.position()[0]
	head_y = head.position()[1]
	prehead_x = prehead.position()[0]
	prehead_y = prehead.position()[1]
	x_axis = 0
	y_axis = 0
	# moving vertical
	if head_x == prehead_x:
		# print('head x = prehead x')
		if head_y > prehead_y:
			# print('head y > prehead y')
			y_axis = +1
			return [x_axis, y_axis]
		elif head_y < prehead_y:
			# print('head y < prehead y')
			y_axis = -1
			return [x_axis, y_axis]
	# moving horizontal
	elif head_y == prehead_y:
		# print('head y = prehead y')
		if head_x > prehead_x:
			# print('head x > prehead x')
			x_axis = +1
			return [x_axis, y_axis]
		elif head_x < prehead_x:
			# print('head x = prehead x')
			x_axis = -1
			return [x_axis, y_axis]
	else:
		return [0, 0]


def move_to_margin(block, side):
	block.speed(0)
	block.hideturtle()
	block.goto(side[0], side[1])
	block.speed(3)
	block.showturtle()


def move_snake():
	direction = get_orientation(snake)
	x_direc = direction[0]
	y_direc = direction[1]
	print(f'Head: {snake[0].position()}, Tail: {snake[1].position()}')
	for i in snake:
		posx = i.position()[0]
		posy = i.position()[1]

		if y_direc == 0:  # moving horizontal
			# return to left margin of canvas
			if x_direc == +1 and posx == max_posx:  # going rightwards
				move_to_margin(i, (-width, posy))
				continue
			# return to right margin of canvas
			elif x_direc == -1 and posx == min_posx:  # going leftwards
				move_to_margin(i, (+width, posy))
				continue
			# limits not reached, just move on

		elif x_direc == 0:  # moving vertical
			# return to bottom margin of canvas
			if y_direc == +1 and posy == max_posy:  # going upwards
				move_to_margin(i, (posx, -height))
				continue
			# return to right margin of canvas
			elif y_direc == -1 and posy == min_posy:  # going downwards
				move_to_margin(i, (posx, +height))
				continue
			# limits not reached, just move on

		i.forward(20)

	scr.update()
	for i in snake:
		print(i.position(), end=' ')
	print('\n')
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
	y_direc = direc[1]
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
	y_direc = direc[1]
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
#scr.onkeypress(move_snake, 'space')

scr.listen()


while True:
	move_snake()


scr.exitonclick()
