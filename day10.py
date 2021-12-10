from common import *
from statistics import median

chars = {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>',
}

points = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

def p1(inp):
	result = 0
	for line in inp:
		tail = ''
		for c in line:
			if c in chars:
				tail = chars[c] + tail
			else:
				if c == tail[0]:
					tail = tail[1:]
				else:
					result += points[c]
					break
	return result

points2 = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

def p2(inp):
	scores = []
	for line in inp:
		tail = ''
		for c in line:
			if c in chars:
				tail = chars[c] + tail
			else:
				if c == tail[0]:
					tail = tail[1:]
				else:
					break
		else:
			v = 0
			for c2 in tail:
				v *= 5
				v += points2[c2]
			scores.append(v)
	return median(scores)

example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

run(example, 26397, p1,
	example, 288957, p2,
	lines, True)
