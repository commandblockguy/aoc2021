from common import *

def p1(inp):
	dots = {tuple(int(y) for y in x.split(',')) for x in inp[0].splitlines()}
	folds = [(x[11], int(x[13:])) for x in inp[1].splitlines()]
	for axis, pos in folds:
		if axis == 'x':
			dots = {(dot[0] if dot[0] < pos else 2*pos - dot[0], dot[1]) for dot in dots}
		else:
			dots = {(dot[0], dot[1] if dot[1] < pos else 2*pos - dot[1]) for dot in dots}
		break
	return len(dots)

def p2(inp):
	dots = {tuple(int(y) for y in x.split(',')) for x in inp[0].splitlines()}
	folds = [(x[11], int(x[13:])) for x in inp[1].splitlines()]
	for axis, pos in folds:
		if axis == 'x':
			dots = {(dot[0] if dot[0] < pos else 2*pos - dot[0], dot[1]) for dot in dots}
		else:
			dots = {(dot[0], dot[1] if dot[1] < pos else 2*pos - dot[1]) for dot in dots}
	for y in range(0, 6):
		print(''.join(('#' if (x,y) in dots else '.') for x in range(50)))
	# not bothering to automate this, I've got eyes
	return 0

example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

run(example, 17, p1,
	example, 0, p2,
	dbl_lines, False)
