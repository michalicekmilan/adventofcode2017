n  = lambda x,y: (x+1, y)
ne = lambda x,y: (x+1,y+1)
se = lambda x,y: (x,y+1)
s  = lambda x,y: (x-1, y)
sw = lambda x,y: (x-1, y-1)
nw = lambda x,y: (x, y-1)

x = y = 0
distance = 0
furthest = 0

with open('input') as f:
	for move in f.readline().split(','):
		x, y = locals()[move](x,y)
		distance = max(abs(x),abs(y))
		if distance > furthest:
			furthest = distance

print(distance)
print(furthest)

	

