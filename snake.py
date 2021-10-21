from segment import Segment


class Snake:
	def __init__(self, size, margins):
		self.pieces = []
		self.snake_size = size
		self.margins = margins
		for i in range(self.snake_size):
			self.pieces.append(
				Segment(posx=20 * self.snake_size - i * 20, posy=0))

	def move(self):  # move the whole snake

		for i in self.pieces:
			# margins = [min_x, min_y, max_x, max_y]
			i.check_crossing_margin(self.margins)
			i.move_segment()

		# print(f'X orientation: {i.x_direct}, Y orientation: {i.y_direct}')
		# for i in snake:
		# 	print(i.position(), end=' ')
		# print('\n')

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
			for i in self.pieces:
				i.turning_points.append([head_position, key])

		# check if it is possible to turn in the entered direction
		head_snake = self.pieces[0]
		head_snake_pos = head_snake.position()
		heading_x = head_snake.x_direct
		heading_y = head_snake.y_direct
		# moving horizontally
		if heading_y == 0 and pressed_key in ['up', 'down']:
			make_turning_point(head_snake_pos, pressed_key)
		# moving horizontally
		elif heading_x == 0 and pressed_key in ['left', 'right']:
			make_turning_point(head_snake_pos, pressed_key)
