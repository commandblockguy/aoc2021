from common import *

def p1(inp):
	inp = [int(x) for x in inp.split(',')]
	return min(sum(abs(x - m) for x in inp) for m in range(max(inp)))

def cost(d):
	return d * (d + 1) // 2

def p2(inp):
	inp = [int(x) for x in inp.split(',')]
	return min(sum(cost(abs(x - m)) for x in inp) for m in range(max(inp)))

example = """16,1,2,0,4,2,7,1,2,14"""

run(example, 37, p1,
	example, 168, p2,
	None, True)
