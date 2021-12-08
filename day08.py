from common import *
from itertools import *

def p1(inp):
	count = 0
	for line in inp:
		signal, output = [x.strip() for x in line.split('|')]
		o = [set(x) for x in output.split(' ')]
		for x in o:
			if len(x) in [2, 4, 3, 7]:
				count += 1
	return count

numbers = {
	"abcefg": 0,
	"cf": 1,
	"acdeg": 2,
	"acdfg": 3,
	"bcdf": 4,
	"abdfg": 5,
	"abdefg": 6,
	"acf": 7,
	"abcdefg": 8,
	"abcdfg": 9
}

def p2(inp):
	result = 0
	for line in inp:
		signal, output = [x.strip() for x in line.split('|')]
		s = signal.split(' ')
		o = output.split(' ')
		for mapping in permutations("abcdefg"):
			sub_result = 0
			valid = True
			for n in s:
				mapped = ''.join(sorted([mapping[ord(c) - ord('a')] for c in n]))
				if mapped not in numbers:
					valid = False
					break
			for n in o:
				mapped = ''.join(sorted([mapping[ord(c) - ord('a')] for c in n]))
				if mapped not in numbers:
					valid = False
					break
				else:
					sub_result = sub_result * 10 + numbers[mapped]
			if valid:
				result += sub_result
				break
		else:
			print('none found')
	return result


example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

run(example, 26, p1,
	example, 61229, p2,
	lines, True)
