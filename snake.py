import time
from turtle import Turtle, Screen
from segment import Segment



class Snake:
	def __init__(self, size):
		self.pieces = []
		self.snake_size = size
		for i in range(self.snake_size):
			self.pieces.append(Segment(posx=20 * self.snake_size - i * 20, posy=0))


	def move(self):

		for i in self.pieces:
			posx = i.xcor()
			posy = i.ycor()
			i.check_crossing_margin()
			i.move_segment()

		scr.update()
		# print(f'X orientation: {i.x_direct}, Y orientation: {i.y_direct}')
		# for i in snake:
		# 	print(i.position(), end=' ')
		# print('\n')
		time.sleep(0.1)

	def turn_snake(onkey):
		for i in snake:
			snake[i].make_turning_point(onkey)





	def turn():
		head_position = turning_points[0]  # position of head when asked to turn
		new_heading = turning_points[3]  # the new heading of the turn
		required_steps = len(snake) - 1
		for step in range(required_steps):
			for i in snake:
				# check if segment is at turning point
				if i.position() == head_position:
					i.change_segment_orientation(new_heading)
				# move forward once it has turned or not
				i.forward(20)
				if i == snake[-1] and step == (required_steps - 1):
					i.change_segment_orientation(new_heading)
			scr.update()
			time.sleep(0.1)

	# check if required turn is possible
	heading_x = turning_points[1]
	heading_y = turning_points[2]
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
