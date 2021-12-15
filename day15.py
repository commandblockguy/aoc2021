from common import *
from queue import PriorityQueue

def p1(inp):
	poses = PriorityQueue()
	poses.put((0, (0,0)))
	maxx = len(inp[0])-1
	maxy = len(inp)-1
	visited = set()
	while not poses.empty():
		cost, (x,y) = poses.get()
		if (x,y) in visited: continue
		visited.add((x,y))
		newcost = cost + int(inp[y][x])
		if (x,y) == (maxx, maxy):
			return newcost - int(inp[0][0])
		else:
			if x != 0:
				poses.put((newcost, (x-1,y)))
			if x != maxx:
				poses.put((newcost, (x+1,y)))
			if y != 0:
				poses.put((newcost, (x,y-1)))
			if y != maxy:
				poses.put((newcost, (x,y+1)))

def p2(inp):
	newinp = []
	for y in range(5):
		for line in inp:
			newline = []
			for x in range(5):
				newline += [((int(c) + x + y - 1) % 9) + 1 for c in line]
			newinp.append(newline)
	inp = newinp
	for line in inp:
		print(''.join(str(x) for x in line))
	poses = PriorityQueue()
	poses.put((0, (0,0)))
	maxx = len(inp[0])-1
	maxy = len(inp)-1
	visited = set()
	while not poses.empty():
		cost, (x,y) = poses.get()
		if (x,y) in visited: continue
		visited.add((x,y))
		newcost = cost + int(inp[y][x])
		if (x,y) == (maxx, maxy):
			return newcost - int(inp[0][0])
		else:
			if x != 0:
				poses.put((newcost, (x-1,y)))
			if x != maxx:
				poses.put((newcost, (x+1,y)))
			if y != 0:
				poses.put((newcost, (x,y-1)))
			if y != maxy:
				poses.put((newcost, (x,y+1)))

example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

run(example, 40, p1,
	example, 315, p2,
	lines, True)
