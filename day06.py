from common import *

def p1(inp):
	fish = [int(x) for x in inp.split(',')]
	for _ in range(80):
		for i in range(len(fish)):
			fish[i] -= 1
			if fish[i]== -1:
				fish[i] = 6
				fish.append(8)
	return len(fish)
	

def p2(inp):
	fish = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
	for x in inp.split(','):
		x = int(x)
		fish[x] += 1

	for _ in range(256):
		new_fish = {}
		for i in range(1,9):
			new_fish[i - 1] = fish[i]
		new_fish[6] += fish[0]
		new_fish[8] = fish[0]
		fish = new_fish
	return sum(fish.values())
example = """3,4,3,1,2"""

run(example, 5934, p1,
	example, 26984457539, p2,
	None, True)
