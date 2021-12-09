from common import *
from collections import defaultdict
from math import prod

def p1(inp):
	row = [10 for x in range(len(inp[0]) + 2)]
	inp = [row] + [[10] + [int(y) for y in x] + [10] for x in inp] + [row]
	count = 0
	for x in range(1, len(inp[0])-1):
		for y in range(1, len(inp)-1):
			if min(inp[y+1][x], inp[y-1][x], inp[y][x+1], inp[y][x-1]) > inp[y][x]:
				count += inp[y][x] + 1
	return count

def p2(inp):
	row = [10 for x in range(len(inp[0]) + 2)]
	inp = [row] + [[10] + [int(y) for y in x] + [10] for x in inp] + [row]
	basins = defaultdict(int)
	for xi in range(1, len(inp[0])-1):
		for yi in range(1, len(inp)-1):
			x,y = xi,yi
			if inp[y][x] == 9: continue
			while min(inp[y+1][x], inp[y-1][x], inp[y][x+1], inp[y][x-1]) <= inp[y][x]:
				m = min(inp[y+1][x], inp[y-1][x], inp[y][x+1], inp[y][x-1])
				if m == inp[y+1][x]:
					y += 1
					continue
				if m == inp[y-1][x]:
					y -= 1
					continue
				if m == inp[y][x+1]:
					x += 1
					continue
				if m == inp[y][x-1]:
					x -= 1
					continue
			basins[(x,y)] += 1
	return prod(x[1] for x in sorted(basins.items(), key = lambda x: -x[1])[:3])

example = """2199943210
3987894921
9856789892
8767896789
9899965678"""

run(example, 15, p1,
	example, 1134, p2,
	lines, True)
