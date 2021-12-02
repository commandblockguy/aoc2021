from common import run

def p1(inp):
	count = 0
	for i in range(len(inp) - 1):
		if inp[i+1] > inp[i]:
			count += 1
	return count

def p2(inp):
	count = 0
	last = -10000000000000000
	for i in range(len(inp) - 3):
		new = sum(inp[i:i+3])
		if new > last:
			count += 1
		last = new
	return count

example = """199
200
208
210
200
207
240
269
260
263
"""

run(example, 7, p1,
	example, 5, p2, 'nums', True)
