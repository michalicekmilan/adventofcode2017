
def swap_programs(s, args):
	return swap_positions(s, (s.index(args[0]), s.index(args[1])))

def swap_positions(s, args):
	tmp = s[args[0]]
	s[args[0]] = s[args[1]]
	s[args[1]] = tmp
	return s

def rotate(s, r):
	return s[-r:] + s[:-r]

def dance(programs):
	for move in dance_moves:
		programs = move[0](programs, move[1])	
	return programs	


programs = [chr(c) for c in range(ord('a'), ord('a')+16)]
dance_moves = []

with open('input') as f:
	for move in f.readline().split(','):
		if move[0] == 's':
			dance_moves.append((rotate, int(move[1:])))
		elif move[0] == 'x':
			p1, p2 = move[1:].split('/')
			dance_moves.append((swap_positions, (int(p1), int(p2))))
		elif move[0] == 'p':
			p1, p2 = move[1:].split('/')
			dance_moves.append((swap_programs,(p1, p2)))
		else:
			raise

dances = []
while True:
	programs = dance(programs)
	p = "".join(programs)
	if p in dances:
		break
	dances.append(p);

print(dances[0])
print(dances[1000000000%len(dances)-1])
