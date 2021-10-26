from segment import Segment


class Snake:
	def __init__(self, size, margins):
		self.pieces = []
		self.snake_size = size
		self.margins = margins
		print('Starting coordinates of segments: ', end='')
		for i in range(self.snake_size, 0, -1):
			start_position = 20*i - 10
			self.pieces.append(
				Segment(posx=start_position, posy=10))
			print(self.pieces[-1].position(), end=' - ')
		print('\n')

	def move(self):  # move the whole snake

		for piece in self.pieces:
			# margins = [min_x, min_y, max_x, max_y]
			piece.check_crossing_margin(self.margins)
			piece.move_segment()

		# print(f'X orientation: {i.x_direct}, Y orientation: {i.y_direct}')
		# for i in snake:
		# 	print(i.position(), end=' ')
		# print('\n')

	def return_position(self):
		for i in range(self.snake_size):
			print(f'Segment {i}: ({self.pieces[i].position()[0]:.0f},'
			  f'{self.pieces[i].position()[1]:.0f})', end=' - ')
		print('\n')

	def turn_snake(self, pressed_key):
		"""
		creates a new turning point for the snake.
		There may be various turning points before
		the whole snake is completely straight.
		For that case, turning_points are added to a list
		so when every segment reaches a turning point, the segment
		changes its orientation and so on until all the turnings
		have been carried out
		"""

		def make_turning_point(head_position, key):
			# turning point: [head position, direction]
			# add the turning point to list of turning points
			# to be carried out by the segment
			for i in self.pieces:  # every segment gets a rotate order
				i.turning_points.append([head_position, key])
			print(f'Turning point created at {head_position}')

		# check if it is possible to turn in the entered direction
		head_snake = self.pieces[0]
		head_snake_pos = head_snake.position()

		# heading_x = head_snake.x_direct
		# heading_y = head_snake.y_direct
		# moving horizontally
		if head_snake.heading() in [0, 180] and \
			pressed_key in ['up', 'down']:
			make_turning_point(head_snake_pos, pressed_key)
		# moving horizontally
		elif head_snake.heading() in [90, 270] and \
			pressed_key in ['left', 'right']:
			make_turning_point(head_snake_pos, pressed_key)
