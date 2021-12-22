from common import *
import functools
import itertools

def gen_die():
	last = 0
	while True:
		roll = last + 1
		last = roll % 100
		yield roll

def p1(inp):
	poses = [int(l[-1]) for l in inp]
	die = gen_die()
	scores = [0, 0]
	total_rolls = 0
	while True:
		for player in range(2):
			rolls = [next(die), next(die), next(die)]
			total_rolls += 3
			new_pos = (poses[player] + sum(rolls) - 1) % 10 + 1
			poses[player] = new_pos
			scores[player] += new_pos
			if scores[player] >= 1000:
				return scores[int(not player)] * total_rolls

@functools.cache
def play(player, poses, scores):
	if scores[0] >= 21:
		return (1, 0)
	if scores[1] >= 21:
		return (0, 1)
	roll_combos = itertools.product(range(1, 4), repeat=3)
	if player:
		new_poses = [(poses[0], (poses[1] + sum(rolls) - 1) % 10 + 1) for rolls in roll_combos]
		new_scores = [(scores[0], (scores[1] + p)) for _, p in new_poses]
	else:
		new_poses = [((poses[0] + sum(rolls) - 1) % 10 + 1, poses[1]) for rolls in roll_combos]
		new_scores = [((scores[0] + p), scores[1]) for p, _ in new_poses]
	result = [play(1 - player, p, s) for p, s in zip(new_poses, new_scores)]
	# print(player, poses, scores)
	# print(new_poses, new_scores)
	# print(result, tuple(map(sum, zip(*result))))
	return tuple(map(sum, zip(*result)))

def p2(inp):
	poses = tuple(int(l[-1]) for l in inp)
	print(play(0, poses, (0, 0)))
	return max(play(0, poses, (0, 0)))

example = """Player 1 starting position: 4
Player 2 starting position: 8"""

run(example, 739785, p1,
	example, 444356092776315, p2,
	lines, True)
