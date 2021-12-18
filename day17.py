from common import *

def p1(inp):
	(xmin, xmax), (ymin, ymax) = ((int(y) for y in x.split('..')) for x in inp[15:].split(', y='))
	print(xmin, xmax, ymin, ymax)
	result = ymin
	for guess_x in range(1, xmax):
		for guess_y in range(100):
			dx, dy = guess_x, guess_y
			x, y = 0, 0
			max_height = ymin
			while dx > 0 or y > ymin:
				x += dx
				y += dy
				max_height = max(max_height, y)
				dx = max(0, dx - 1)
				dy -= 1
			if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
				result = max(result, max_height)
	return result

def p2(inp):
	(xmin, xmax), (ymin, ymax) = ((int(y) for y in x.split('..')) for x in inp[15:].split(', y='))
	print(xmin, xmax, ymin, ymax)
	result = 0
	found = []
	for guess_x in range(0, xmax+1):
		for guess_y in range(ymin,200):
			dx, dy = guess_x, guess_y
			x, y = 0, 0
			while dy > 0 or y >= ymin:
				x += dx
				y += dy
				dx = max(0, dx - 1)
				dy -= 1
				if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
					result += 1
					found.append((guess_x, guess_y))
					break
	return result

example = """target area: x=20..30, y=-10..-5"""

run(example, 45, p1,
	example, 112, p2,
	None, True)
