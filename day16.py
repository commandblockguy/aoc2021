from common import *
from bitstring import BitArray
from math import prod

def parse_packets(data, max=None):
	count = 0
	offset = 0
	pkts = []
	while len(data) - offset > 6 and (max == None or count < max):
		pkt, size = parse_packet(data[offset:])
		count += 1
		offset += size
		pkts.append(pkt)
	return pkts, offset

def parse_packet(pkt):
	version = pkt[:3].uint
	type = pkt[3:6].uint
	if type == 4: # literal
		num = BitArray()
		pos = 6
		while pkt[pos]:
			num += pkt[pos+1:pos+5]
			pos += 5
		num += pkt[pos+1:pos+5]
		pos += 5
		num = num.uint
		return (version, type, num), pos
	else:
		if pkt[6]: # num packets
			num_pkts = pkt[7:7+11].uint
			pkts, size = parse_packets(pkt[7+11:], num_pkts)
			return (version, type, pkts), 7+11+size
		else: # length in bits
			num_bits = pkt[7:7+15].uint
			pkts, size = parse_packets(pkt[7+15:7+15+num_bits])
			return (version, type, pkts), 7+15+size
	print(pkt)

def count_versions(pkt):
	version, type, data = pkt
	if type != 4:
		return version + sum(count_versions(pkt) for pkt in data)
	else:
		return version

def p1(inp):
	inp = BitArray(hex=inp)
	pkts, _ = parse_packets(inp)
	return sum(count_versions(pkt) for pkt in pkts)

def eval_packet(pkt):
	version, type, data = pkt
	if type == 0: #sum
		return sum(eval_packet(pkt) for pkt in data)
	elif type == 1: #prod
		return prod(eval_packet(pkt) for pkt in data)
	elif type == 2: #min
		return min(eval_packet(pkt) for pkt in data)
	elif type == 3: #max
		return max(eval_packet(pkt) for pkt in data)
	elif type == 4: #literal
		return data
	elif type == 5: #gt
		return eval_packet(data[0]) > eval_packet(data[1])
	elif type == 6: #lt
		return eval_packet(data[0]) < eval_packet(data[1])
	elif type == 7: #equals
		return eval_packet(data[0]) == eval_packet(data[1])

def p2(inp):
	inp = BitArray(hex=inp)
	pkts, _ = parse_packets(inp)
	# breaks without this print
	print(pkts[0])
	return eval_packet(pkts[0])

example = """8A004A801A8002F478"""
example2 = """9C0141080250320F1802104A08"""

run(example, 16, p1,
	example2, 1, p2,
	None, True)
