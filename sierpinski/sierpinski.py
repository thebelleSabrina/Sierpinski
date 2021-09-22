"""
File: sierpinski.py
Name: Sabrina Wang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the order of Sierpinski Triangle
	:param length: length of order 1 Sierpinski Triangle
	:param upper_left_x: upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: upper left y coordinate of order 1 Sierpinski Triangle
	:return: the Sierpinski Triangle with order that user inputs
	"""
	if order == 0:
		pass
	else:
		# gets the order-1 sierpinski triangle
		upper_right_x = upper_left_x+length  # upper right's point
		upper_right_y = upper_left_y
		side = GLine(upper_left_x, upper_left_y, upper_right_x, upper_right_y)
		window.add(side)

		low_x = upper_left_x + length*0.5  # lower side's point
		low_y = upper_right_y + length*0.866
		side2 = GLine(upper_left_x, upper_left_y, low_x, low_y)
		window.add(side2)

		side3 = GLine(upper_right_x, upper_right_y, low_x, low_y)
		window.add(side3)

		# with one more order, the length will be half of the last order
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)

		sierpinski_triangle(order - 1, length / 2, upper_left_x+(length/2), upper_left_y)

		sierpinski_triangle(order - 1, length / 2, upper_left_x + (length/2*0.5), upper_right_y + (length/2*0.866))


if __name__ == '__main__':
	main()