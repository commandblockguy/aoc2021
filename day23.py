from common import *
import heapq
from frozendict import frozendict

energies = {
	'A': 1,
	'B': 10,
	'C': 100,
	'D': 1000
}

cell_poses = {
	'A': 3,
	'B': 5,
	'C': 7,
	'D': 9
}

hall_y = 1

def visualize(state):
	bg = '''#############
#...........#
###.#.#.#.###
  #.#.#.#.#  
  #########  '''.splitlines()
	for y in range(5):
		print(''.join(state[x, y] if (x, y) in state else bg[y][x] for x in range(13)))

def sign(x):
	if x == 0: return 0
	if x > 0: return 1
	else: return -1

def moved_to(state, current_cost, old, new):
	c = state[old]
	state = dict(state.copy())
	state[new] = state.pop(old)
	dx = abs(new[0] - old[0])
	dy = abs(hall_y - old[1]) + abs(new[1] - hall_y)
	result = frozendict(state), current_cost + energies[c] * (dx + dy)
	return result

def possible_states(current, current_cost, cell_bottom):
	result = []
	for (x, y), c in current.items():
		# check there are no aphipods of the wrong type in the target cell
		if x != cell_poses[c] and sum(1 for ((x2, y2), c2) in current.items() if x2 == cell_poses[c] and c2 != c) == 0 and sum(1 for ((x2, y2), c2) in current.items() if x2 == x and y2 < y) == 0:
			target_y = cell_bottom - sum(1 for ((x2, y2), c2) in current.items() if x2 == cell_poses[c])
			for x2 in range(cell_poses[c], x, sign(x - cell_poses[c])):
				if (x2, hall_y) in current: break
			else:
				result.append(moved_to(current, current_cost, (x, y), (cell_poses[c], target_y)))
	if len(result): return result # move to correct position whenever possible
	for (x, y), c in current.items():
		if y != hall_y and sum(1 for ((x2, y2), c2) in current.items() if x2 == x and y2 < y) == 0 and (
			x != cell_poses[c] or sum(1 for ((x2, y2), c2) in current.items() if x2 == x and x2 != cell_poses[c2]) != 0
		):
			# move to hall
			for new_x in [1, 2, 4, 6, 8, 10, 11]:
				for x2 in range(new_x, x, sign(x - new_x)):
					if (x2, hall_y) in current: break
				else:
					result.append(moved_to(current, current_cost, (x, y), (new_x, hall_y)))
	return result

def p1(inp):
	amphipods = frozendict({(x, y): c for y, line in enumerate(inp) for x, c in enumerate(line) if c in cell_poses})
	unvisited = {amphipods: 0}
	visited = set()
	parents = {}
	while len(unvisited) > 0:
		current, cost = min(unvisited.items(), key=lambda x: x[1])
		unvisited.pop(current)
		visited.add(current)
		for (x, y), c in current.items():
			if y == hall_y or cell_poses[c] != x:
				break
		else:
			states = [(current, None)]
			temp = current
			while temp in parents:
				temp, newcost = parents[temp]
				states.append((temp, newcost))
			states = reversed(states)
			for state, vcost in states:
				visualize(state)
				print(vcost)
			return cost
		# print(len(unvisited), len(visited), cost)
		new_states = possible_states(current, cost, 3)
		for nstate, ncost in new_states:
			if nstate not in visited and (nstate not in unvisited or ncost < unvisited[nstate]):
				unvisited[nstate] = ncost
				parents[nstate] = current, ncost

def p2(inp):
	inp = inp[:3] + ['  #D#C#B#A#  ', '  #D#B#A#C#  '] + inp[3:]
	amphipods = frozendict({(x, y): c for y, line in enumerate(inp) for x, c in enumerate(line) if c in cell_poses})
	unvisited = {amphipods: 0}
	visited = set()
	parents = {}
	while len(unvisited) > 0:
		current, cost = min(unvisited.items(), key=lambda x: x[1])
		unvisited.pop(current)
		visited.add(current)
		for (x, y), c in current.items():
			if y == hall_y or cell_poses[c] != x:
				break
		else:
			states = [(current, None)]
			temp = current
			while temp in parents:
				temp, newcost = parents[temp]
				states.append((temp, newcost))
			states = reversed(states)
			for state, vcost in states:
				visualize(state)
				print(vcost)
			return cost
		# print(len(unvisited), len(visited), cost)
		new_states = possible_states(current, cost, 5)
		for nstate, ncost in new_states:
			if nstate not in visited and (nstate not in unvisited or ncost < unvisited[nstate]):
				unvisited[nstate] = ncost
				parents[nstate] = current, ncost

example = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

run(example, 12521, p1,
	example, 44169, p2,
	lines, True)
