from common import *

# recursion go brrrrrr

def add(a, b):
	return reduce([a, b])

def add_leftmost(pair, num):
	if isinstance(pair, int):
		return pair + num
	else:
		return [add_leftmost(pair[0], num), pair[1]]

def add_rightmost(pair, num):
	if isinstance(pair, int):
		return pair + num
	else:
		return [pair[0], add_rightmost(pair[1], num)]

def magnitude(pair):
	if isinstance(pair, int):
		return pair
	else:
		return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])

def explode(num, depth):
	if isinstance(num, int):
		return num, 0, 0, False
	if depth < 4:
		r, al, ar, m = explode(num[0], depth + 1)
		if m: return [r, add_leftmost(num[1], ar)], al, 0, m
		r, al, ar, m = explode(num[1], depth + 1)
		if m: return [add_rightmost(num[0], al), r], 0, ar, m
		return num, 0, 0, False
	else:
		return 0, num[0], num[1], True

def split(num):
	return [num // 2, num - num // 2]

def split_if_10(num):
	if isinstance(num, int):
		if num < 10:
			return num, False
		else:
			return split(num), True
	else:
		a, b = num
		a, ra = split_if_10(a)
		if ra:
			return [a, b], True
		b, rb = split_if_10(b)
		return [a, b], rb

def reduce(pair):
	pair, _, _, modified = explode(pair, 0)
	if modified:
		return reduce(pair)
	pair, modified = split_if_10(pair)
	if modified:
		return reduce(pair)
	else:
		return pair

def p1(inp):
	inp = [eval(x) for x in inp]
	result = inp[0]
	for x in inp[1:]:
		result = add(result, x)
	print(result)
	result = magnitude(result)
	return result

def p2(inp):
	inp = [eval(x) for x in inp]
	return max(magnitude(add(x, y)) for x in inp for y in inp if y != x)

example = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

run(example, 4140, p1,
	example, 3993, p2,
	lines, True)
