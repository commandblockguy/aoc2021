from common import *
from bitstring import BitArray

def p1(inp):
	algo, image = inp
	print(algo)
	pixels = {(x, y) for y, row in enumerate(image.splitlines()) for x, p in enumerate(row) if p == '#'}
	invert = False
	for i in range(2):
		newpixels = set()
		invert_new = invert ^ (algo[0] == '#')
		visited = set()
		for x1, y1 in pixels:
			for x2 in range(x1-1,x1+2):
				for y2 in range(y1-1,y1+2):
					if (x2, y2) in visited: continue
					visited.add((x2, y2))
					val = BitArray([(p in pixels) ^ invert for p in [(x3,y3) for y3 in range(y2-1,y2+2) for x3 in range(x2-1,x2+2)]]).uint
					if (algo[val] == '#') ^ invert_new:
						newpixels.add((x2, y2))
		pixels = newpixels
		invert = invert_new
		print(i+1)
		for y in range(min(y for _, y in pixels), max(y for _, y in pixels)):
			print(''.join('#' if ((x, y) in pixels) ^ invert else '.' for x in range(min(x for x, _ in pixels), max(x for x, _ in pixels))))
	return len(pixels)

def p2(inp):
	algo, image = inp
	pixels = {(x, y) for y, row in enumerate(image.splitlines()) for x, p in enumerate(row) if p == '#'}
	invert = False
	for i in range(50):
		newpixels = set()
		invert_new = invert ^ (algo[0] == '#')
		visited = set()
		for x1, y1 in pixels:
			for x2 in range(x1-1,x1+2):
				for y2 in range(y1-1,y1+2):
					if (x2, y2) in visited: continue
					visited.add((x2, y2))
					val = BitArray([(p in pixels) ^ invert for p in [(x3,y3) for y3 in range(y2-1,y2+2) for x3 in range(x2-1,x2+2)]]).uint
					if (algo[val] == '#') ^ invert_new:
						newpixels.add((x2, y2))
		pixels = newpixels
		invert = invert_new
	return len(pixels)

example = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

run(example, 35, p1,
	example, 3351, p2,
	dbl_lines, True)
