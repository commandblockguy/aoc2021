from common import *

def p1(inp):
	gamma = 0
	for i in range(len(inp[0])):
		count = 0
		for num in inp:
			if num[i] == '1':
				count += 1
		if count >= len(inp) / 2:
			gamma += 2**(len(inp[0])-i-1)
	eps = gamma ^ (2**(len(inp[0])) - 1)
	return gamma * eps

def oxy(inp):
	for i in range(len(inp[0])):
		if len(inp) == 1:
			return int(inp[0],2)
		count = 0
		for num in inp:
			if num[i] == '1':
				count += 1
		if count >= len(inp) / 2:
			inp = [x for x in inp if x[i] == '1']
		else:
			inp = [x for x in inp if x[i] == '0']
	if len(inp) == 1:
		return int(inp[0],2)

def scrub(inp):
	for i in range(len(inp[0])):
		if len(inp) == 1:
			return int(inp[0],2)
		count = 0
		for num in inp:
			if num[i] == '1':
				count += 1
		if count < len(inp) / 2:
			inp = [x for x in inp if x[i] == '1']
		else:
			inp = [x for x in inp if x[i] == '0']
	if len(inp) == 1:
		return int(inp[0],2)

def p2(inp):
	return oxy(inp) * scrub(inp)

example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

run(example, 198, p1,
	example, 230, p2,
	lines, True)
