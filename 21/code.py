import math

def to_grid(data):
	grid = []
	for r in data.split('/'):
		grid.append(tuple([x for x in r]))
	return grid

def print_grid(g):
	for r in g:
		print("".join(r))

def rotate_grid(g, count=1):
	for i in range(count):
		g = list(zip(*g[::-1]))
	return g

def flip_grid(g):
	return [tuple(reversed(r)) for r in g]

def divide_grid(g):
	grids = []
	for r in range(0, len(g), 2 if len(g)%2 == 0 else 3):
		for c in range(0, len(g), 2 if len(g)%2 == 0 else 3):
			if len(g)%2 == 0:
				grids.append([(g[r][c],g[r][c+1]), (g[r+1][c],g[r+1][c+1])])
			else:
				grids.append([(g[r][c],g[r][c+1], g[r][c+2]), 
				(g[r+1][c],g[r+1][c+1],g[r+1][c+2]), 
				(g[r+2][c],g[r+2][c+1],g[r+2][c+2])])
	return grids


def join_grid(g):
	k = int(math.sqrt(len(g)))
	l = len(g[0])
	joined = [[0 for x in range(k*l)] for y in range(k*l)]
	for i in range(k):
		for j in range(k):
			for r in range(l):
				for c in range(l):
					joined[(i*l)+r][(j*l)+c] = g[i*k+j][r][c]
	return joined


def matches(g, rule):
	if len(g) != len(rule):
		return False
	if g == rule: 
		return True
	for i in range(1, 4):
		r = rotate_grid(rule, i)
		if g == r or g == flip_grid(r):
			return True
	return False

def transform_grid(g, rules):
	for r in rules:
		if matches(g, to_grid(r)):
			return to_grid(rules.get(r))
	raise Exception("Rule not found: " + str(g))
	
def process(iters):	
	grid = to_grid(".#./..#/###")
	for i in range(iters):
		to_join = []
		for g in divide_grid(grid):
			to_join.append(transform_grid(g, rules))
		grid = join_grid(to_join)
		
	pixels = 0	
	for r in grid:
		pixels += ("".join(r)).count('#')
	return pixels	

rules = {}
with open('input') as f:
	for l in f.readlines():
		k, v = l.split(' => ')
		rules[k.strip()] = v.strip()	

print(process(5))
#print(process(18))
	



