from common import *
import re

def p1(inp):
	m = {}
	for line in inp:
		x1,y1,x2,y2 = [int(x) for x in re.split(',| -> ', line)]
		if x1 == x2:
			for y in range(min(y1, y2), max(y1, y2) + 1):
				if (x1, y) in m:
					m[(x1, y)] += 1
				else:
					m[(x1, y)] = 1
		elif y1 == y2:
			for x in range(min(x1, x2), max(x1, x2) + 1):
				if (x, y1) in m:
					m[(x, y1)] += 1
				else:
					m[(x, y1)] = 1
	return sum(1 for v in m.values() if v > 1)

def sign(x):
	if x == 0: return 0
	if x > 0: return 1
	return -1


def p2(inp):
	m = {}
	for line in inp:
		x1,y1,x2,y2 = [int(x) for x in re.split(',| -> ', line)]
		dx = sign(x2 - x1)
		dy = sign(y2 - y1)
		x, y = x1, y1
		while x != x2 or y != y2:
			if (x, y) in m:
				m[(x, y)] += 1
			else:
				m[(x, y)] = 1
			x += dx
			y += dy
		if (x, y) in m:
			m[(x, y)] += 1
		else:
			m[(x, y)] = 1
	return sum(1 for v in m.values() if v > 1)

example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

run(example, 5, p1,
	example, 12, p2,
	lines, True)
