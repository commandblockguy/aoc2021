from common import run
import re

# okay this code is pretty bad even for AoC standards

def p1(inp):
	inp = re.sub(' +', ' ', inp)
	inp = re.sub('\n ', '\n', inp)
	nums = inp.split('\n\n')[0].split(',')
	cards = [[line.split(' ') for line in card.split('\n')] for card in inp.split('\n\n')[1:]]
	for num in nums:
		for i in range(len(cards)):
			for j in range(5):
				for k in range(5):
					if cards[i][j][k] == num:
						cards[i][j][k] = 0
			for j in range(5):
				for k in range(5):
					if cards[i][j][k] != 0: break
				else:
					count = 0
					for l in range(5):
						for m in range(5):
							count += int(cards[i][m][l])
					return count * int(num)



def p2(inp):
	inp = re.sub(' +', ' ', inp)
	inp = re.sub('\n ', '\n', inp)
	nums = inp.split('\n\n')[0].split(',')
	cards = [[line.split(' ') for line in card.split('\n')] for card in inp.split('\n\n')[1:]]
	cards_remaining = set(range(len(cards)))
	for num in nums:
		for i in range(len(cards)):
			for j in range(5):
				for k in range(5):
					if cards[i][j][k] == num:
						cards[i][j][k] = 0
			for j in range(5):
				for k in range(5):
					if cards[i][j][k] != 0: break
				else:
					count = 0
					for l in range(5):
						for m in range(5):
							count += int(cards[i][m][l])
					if i in cards_remaining: cards_remaining.remove(i)
					if len(cards_remaining) == 0:
						print(i, num)
						return count * int(num)
				for k in range(5):
					if cards[i][k][j] != 0: break
				else:
					count = 0
					for l in range(5):
						for m in range(5):
							count += int(cards[i][m][l])
					if i in cards_remaining: cards_remaining.remove(i)
					if len(cards_remaining) == 0:
						print(i, num)
						return count * int(num)

example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

run(example, 4512, p1,
	example, 1924, p2,
	None, True)
