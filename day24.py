from common import *
from collections import defaultdict

def p1(inp):
	orig = inp
	inp = reversed([x.splitlines() for x in inp.split('inp w\n')][1:])
	next_zs = {0}
	inputss = []
	for block in list(inp):
		zs = set()
		inputs = defaultdict(dict)
		for prev_z in range(26 ** 3):
			for n in range(1, 10):
				registers = {'w': n, 'x': 0, 'y': 0, 'z': prev_z}
				for line in block:
					mnem, a, b = line.split(' ')
					b = registers[b] if b in registers else int(b)
					registers[a] = {
						'add': lambda a, b: a + b,
						'mul': lambda a, b: a * b,
						'div': lambda a, b: a // b,
						'mod': lambda a, b: a % b,
						'eql': lambda a, b: 1 if a == b else 0,
					}[mnem](registers[a], b)
				if registers['z'] in next_zs:
					zs.add(prev_z)
					inputs[prev_z][n] = registers['z']
		inputss.append(inputs)
		next_zs = zs
	inputss = reversed(inputss)
	z = 0
	result = ''
	for inputs in inputss:
		n = max(inputs[z].keys())
		result += str(n)
		z = inputs[z][n]
	return int(result)

def p2(inp):
	orig = inp
	inp = reversed([x.splitlines() for x in inp.split('inp w\n')][1:])
	next_zs = {0}
	inputss = []
	for block in list(inp):
		zs = set()
		inputs = defaultdict(dict)
		for prev_z in range(26 ** 3):
			for n in range(1, 10):
				registers = {'w': n, 'x': 0, 'y': 0, 'z': prev_z}
				for line in block:
					mnem, a, b = line.split(' ')
					b = registers[b] if b in registers else int(b)
					registers[a] = {
						'add': lambda a, b: a + b,
						'mul': lambda a, b: a * b,
						'div': lambda a, b: a // b,
						'mod': lambda a, b: a % b,
						'eql': lambda a, b: 1 if a == b else 0,
					}[mnem](registers[a], b)
				if registers['z'] in next_zs:
					zs.add(prev_z)
					inputs[prev_z][n] = registers['z']
		inputss.append(inputs)
		next_zs = zs
	inputss = reversed(inputss)
	z = 0
	result = ''
	for inputs in inputss:
		n = min(inputs[z].keys())
		result += str(n)
		z = inputs[z][n]
	return int(result)

example = """inp w
add z w
add z -3
inp w
add z w
add z -7
"""

run(example, 91, p1,
	example, 37, p2,
	None, True)
