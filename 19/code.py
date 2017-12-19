import collections

Packet = collections.namedtuple('Packet', 'x y direction letters')

D = lambda x,y: (x, y+1)
U = lambda x,y: (x, y-1)
R = lambda x,y: (x+1, y)
L = lambda x,y: (x-1, y)


def step(diagram, packet):
	x, y = packet.direction(packet.x, packet.y)
	c = diagram[y][x]
	if c == ' ':
		return Packet(x, y, None, packet.letters)
	
	if c != '+':
		if c in ('|', '-'):
			return Packet(x, y, packet.direction, packet.letters)
		else:
			return Packet(x, y, packet.direction, packet.letters + c)
	
	directions = [L, R] if packet.direction in [U, D] else [U, D]
	for d in directions:
		nx, ny = d(x,y)
		if diagram[ny][nx] != ' ':
			return Packet(x, y, d, packet.letters)


diagram = []

with open('input') as f:
	for l in f.readlines():
		diagram.append([x for x in l[:-1]])

packet = Packet(diagram[0].index('|'), 0, D, '')
steps = 0

while packet.direction != None:
	packet = step(diagram, packet)
	steps += 1


print(packet.letters)	 
print(steps)	 



