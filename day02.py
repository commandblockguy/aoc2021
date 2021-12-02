from common import run

def p1(inp):
	depth = 0
	horiz = 0
	for line in inp:
		dir, num = line.split()
		num = int(num)
		if dir == 'forward':
			horiz += num
		if dir == 'back':
			horiz -= num
		if dir == 'up':
			depth -= num
		if dir == 'down':
			depth += num
	return depth * horiz
		

def p2(inp):
	aim = 0
	horiz = 0
	depth = 0
	for line in inp:
		dir, num = line.split()
		num = int(num)
		if dir == 'forward':
			horiz += num
			depth += aim * num
		if dir == 'back':
			horiz -= num
		if dir == 'up':
			aim -= num
		if dir == 'down':
			aim += num
	return depth * horiz

example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

run(example, 150, p1,
	example, 900, p2,
	'lines', True)
