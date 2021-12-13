from common import *
from collections import defaultdict

def find_paths(graph, header):
	result = [header]
	for n in graph[header[-1]]:
		if n[0].isupper() or n not in header:
			result = result + find_paths(graph, header + [n])
	return result

def p1(inp):
	graph = defaultdict(list)
	for x in inp:
		h,t = x.split('-')
		graph[h].append(t)
		graph[t].append(h)
	return sum(x[-1] == 'end' for x in find_paths(graph, ['start']))

def find_paths2(graph, header):
	result = [header]
	has_dup = len({x for x in header if x[0].islower()}) != len([x for x in header if x[0].islower()])
	for n in graph[header[-1]]:
		if (n == 'start' or n == 'end'):
			if n not in header:
				result = result + find_paths2(graph, header + [n])
		elif n[0].isupper() or n not in header or not has_dup:
			result = result + find_paths2(graph, header + [n])
	return result

def p2(inp):
	graph = defaultdict(list)
	for x in inp:
		h,t = x.split('-')
		graph[h].append(t)
		graph[t].append(h)
	return sum(x[-1] == 'end' for x in find_paths2(graph, ['start']))

example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

run(example, 10, p1,
	example, 36, p2,
	lines, True)
