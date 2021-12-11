from common import *

def p1(inp):
	octopuses = [[int(y) for y in x] for x in inp]
	flashes = 0
	for i in range(100):
		flashed = [[False for _ in range(len(inp[0]))] for _ in range(len(inp))]
		for x in range(len(inp[0])):
			for y in range(len(inp)):
				octopuses[y][x] += 1
		done = False
		while not done:
			done = True
			for x in range(len(inp[0])):
				for y in range(len(inp)):
					if octopuses[y][x] > 9 and not flashed[y][x]:
						flashed[y][x] = True
						done = False
						flashes += 1
						for x2 in range(x-1,x+2):
							for y2 in range(y-1,y+2):
								if x2 >= 0 and x2 < len(inp[0]) and y2 >= 0 and y2 < len(inp) and not (x2 == x and y2 == y):
									octopuses[y2][x2] += 1
		for x in range(len(inp[0])):
			for y in range(len(inp)):
				if flashed[y][x]:
					octopuses[y][x] = 0
	return flashes

def p2(inp):
	octopuses = [[int(y) for y in x] for x in inp]
	flashes = 0
	i = 0
	while True:
		i += 1
		flashed = [[False for _ in range(len(inp[0]))] for _ in range(len(inp))]
		for x in range(len(inp[0])):
			for y in range(len(inp)):
				octopuses[y][x] += 1
		done = False
		while not done:
			done = True
			for x in range(len(inp[0])):
				for y in range(len(inp)):
					if octopuses[y][x] > 9 and not flashed[y][x]:
						flashed[y][x] = True
						done = False
						flashes += 1
						for x2 in range(x-1,x+2):
							for y2 in range(y-1,y+2):
								if x2 >= 0 and x2 < len(inp[0]) and y2 >= 0 and y2 < len(inp) and not (x2 == x and y2 == y):
									octopuses[y2][x2] += 1
		for x in range(len(inp[0])):
			for y in range(len(inp)):
				if flashed[y][x]:
					octopuses[y][x] = 0
		if sum(sum(x) for x in flashed) == len(inp) * len(inp[0]):
			return i

example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

run(example, 1656, p1,
	example, 195, p2,
	lines, True)
