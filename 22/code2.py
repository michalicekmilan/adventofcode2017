
U = lambda x, y: (x, y-1)
L = lambda x, y: (x-1, y)
D = lambda x, y: (x, y+1)
R = lambda x, y: (x+1, y)

RIGHTOF = {U:R, R:D, D:L, L:U}
LEFTOF = {U:L, L:D, D:R, R:U}
REVERSEOF = {U:D, D:U, L:R, R:L}

I = "INFECTED"
W = "WEAKENED"
F = "FLAGGED"

virus = [(0,0), U]
grid_data = {}
infected_count = 0

with open('input') as f:
	grid = []
	for l in f.readlines():
		grid.append([x for x in l.strip()])
	for i, r in enumerate(grid):
		for j, c in enumerate(r):
			if c == "#":
				grid_data[((j-len(grid)//2, i-len(grid)//2))] = I

for i in range(10000000):
	if virus[0] not in grid_data:
		virus[1] = LEFTOF[virus[1]]
		grid_data[virus[0]] = W
	elif grid_data[virus[0]] == W:
		grid_data[virus[0]] = I
		infected_count += 1
	elif grid_data[virus[0]] == I:
		virus[1] = RIGHTOF[virus[1]]
		grid_data[virus[0]] = F
	else:
		virus[1] = REVERSEOF[virus[1]]
		del grid_data[virus[0]]
	virus[0] = virus[1](virus[0][0], virus[0][1])

print(infected_count)





