from common import *

def p1(inp):
	cucumbers = {(x, y): c for y, line in enumerate(inp) for x, c in enumerate(line) if c in '>v'}
	map_height = len(inp)
	map_width = len(inp[0])
	moved = True
	i = 0
	while moved:
		moved = False
		new = {}
		for (x, y), c in cucumbers.items():
			new_x = (x + 1) % map_width
			if c == '>' and (new_x, y) not in cucumbers:
				new[(new_x, y)] = c
				moved = True
			else:
				new[(x, y)] = c
		cucumbers = new
		new = {}
		for (x, y), c in cucumbers.items():
			new_y = (y + 1) % map_height
			if c == 'v' and (x, new_y) not in cucumbers:
				new[(x, new_y)] = c
				moved = True
			else:
				new[(x, y)] = c
		cucumbers = new
		i += 1
	return i

def p2(inp):
	return None

example = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

run(example, 58, p1,
	example, 0, p2,
	lines, True)
