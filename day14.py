from common import *
import re
from collections import defaultdict
import functools, itertools

def p1(inp):
	template, rules = inp
	rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in rules.splitlines()}
	paircounts = defaultdict(int)
	counts = defaultdict(int)
	for i in range(len(template) - 1):
		paircounts[template[i:i+2]] += 1
		counts[template[i]] += 1
	counts[template[-1]] += 1
	for _ in range(10):
		print(paircounts)
		copy = paircounts.copy()
		for pair in copy:
			if copy[pair] > 0 and pair in rules:
				paircounts[pair[0] + rules[pair]] += copy[pair]
				paircounts[rules[pair] + pair[1]] += copy[pair]
				counts[rules[pair]] += copy[pair]
				paircounts[pair] -= copy[pair]
	counts = sorted(counts.values())
	print(counts)
	return counts[-1] - counts[0]


def p2(inp):
	template, rules = inp
	rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in rules.splitlines()}
	paircounts = defaultdict(int)
	counts = defaultdict(int)
	for i in range(len(template) - 1):
		paircounts[template[i:i+2]] += 1
		counts[template[i]] += 1
	counts[template[-1]] += 1
	for _ in range(40):
		copy = paircounts.copy()
		for pair in copy:
			if copy[pair] > 0 and pair in rules:
				paircounts[pair[0] + rules[pair]] += copy[pair]
				paircounts[rules[pair] + pair[1]] += copy[pair]
				counts[rules[pair]] += copy[pair]
				paircounts[pair] -= copy[pair]
	counts = sorted(counts.values())
	print(counts)
	return counts[-1] - counts[0]

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

run(example, 1588, p1,
	example, 2188189693529, p2,
	dbl_lines, True)
