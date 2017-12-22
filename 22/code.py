
U = lambda x, y: (x, y-1)
L = lambda x, y: (x-1, y)
D = lambda x, y: (x, y+1)
R = lambda x, y: (x+1, y)

RIGHTOF = {U:R, R:D, D:L, L:U}
LEFTOF = {U:L, L:D, D:R, R:U}

virus = [(0,0), U]
infected_count = 0
infected = set()

with open('input') as f:
	grid = []
	for l in f.readlines():
		grid.append([x for x in l.strip()])
	for i, r in enumerate(grid):
		for j, c in enumerate(r):
			if c == "#":
				infected.add((j-len(grid)//2, i-len(grid)//2))

for i in range(10000):
	virus[1] = RIGHTOF[virus[1]] if virus[0] in infected else LEFTOF[virus[1]]
	if virus[0] not in infected:
		infected_count += 1
		infected.add(virus[0])
	else:
		infected.remove(virus[0])
	virus[0] = virus[1](virus[0][0], virus[0][1])

print(infected_count)





