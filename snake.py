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


class Segment(Turtle):
	def __init__(self, posx, posy):
		super().__init__()
		self.pencolor('blue')
		self.shape('square')
		self.x_direct = +1
		self.y_direct = 0
		self.posx = posx
		self.posy = posy
		self.penup()
		self.goto(self.posx, self.posy)

	def cross_margin(self, side):
		self.speed(0)
		self.hideturtle()
		posx = self.position()[0]
		posy = self.position()[1]
		if side == 'left':
			self.goto(max_posx-10, posy)
		elif side == 'right':
			self.goto(-max_posx+10, posy)
		elif side == 'upper':
			self.goto(posx, - max_posy + 10)
		elif side == 'bottom':
			self.goto(posx, max_posy - 10)

		self.speed(3)
		self.showturtle()
		
	def turn_segment(self, key):

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
					self.y_direct = -1

		# moving vertical
		elif self.x_direct == 0:
			# moving up
			if self.y_direct == 1:  # up
				if key == 'left':
					self.left(90)
					self.x_direct = -1
					self.y_direct = 0
				elif key == 'right':
					self.right(90)
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


# create segments of turtle
snake_size = 4
snake = []
for i in range(snake_size):
	snake.append(Segment(posx=20 * snake_size - i * 20, posy=0))


def move_snake():

	for i in snake:
		posx = i.position()[0]
		posy = i.position()[1]
		if posx >= max_posx:  # crossing the right side
			i.cross_margin('right')
		elif posx <= min_posx:  # crossing the left side
			i.cross_margin('left')
		elif posy >= max_posy:  # crossing the upper side
			i.cross_margin('upper')
		elif posy <= min_posy:  # crossing the bottom side
			i.cross_margin('bottom')
		i.forward(20)

	scr.update()
	print(f'X orientation: {i.x_direct}, Y orientation: {i.y_direct}')
	for i in snake:
		print(i.position(), end=' ')
	print('\n')
	time.sleep(0.1)


def turn_snake(key_pressed):

	head_pos = snake[0].position()
	# check if
	def turn(k):
		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_pos:
					i.turn_segment(k)
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					i.turn_segment(k)
			scr.update()
			time.sleep(0.1)

	# check if required turn is possible
	heading_x = snake[0].x_direct
	heading_y = snake[0].y_direct
	# moving horizontally
	if heading_y == 0 and key_pressed in ['up', 'down']:
		turn(key_pressed)
	# moving horizontally
	elif heading_x == 0 and key_pressed in ['left', 'right']:
		turn(key_pressed)


# Event listeners
scr.onkeypress(lambda: turn_snake('up'), 'Up')
scr.onkeypress(lambda: turn_snake('down'), 'Down')
scr.onkeypress(lambda: turn_snake('left'), 'Left')
scr.onkeypress(lambda: turn_snake('right'), 'Right')
scr.onkeypress(move_snake, 'space')

scr.listen()


while True:
	move_snake()


scr.exitonclick()
