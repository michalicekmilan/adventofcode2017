
input = 361527

L = lambda x, y: (x-1, y)
R = lambda x, y: (x+1, y)
U = lambda x, y: (x, y-1)
D = lambda x, y: (x, y+1)
	
moves = {R:U, U:L, L:D, D:R}


def tostr(x, y):
	return str(x) + str(y)

def compute_spiral_value():
	return spiral.get(tostr(x-1, y-1), 0) \
		+ spiral.get(tostr(x, y-1), 0) \
		+ spiral.get(tostr(x+1, y-1), 0) \
		+ spiral.get(tostr(x-1, y), 0) \
		+ spiral.get(tostr(x+1, y), 0) \
		+ spiral.get(tostr(x-1, y+1), 0) \
		+ spiral.get(tostr(x, y+1), 0) \
		+ spiral.get(tostr(x+1, y+1), 0) 
		

def next_move():
	global spiral_size_length, local_size_length, move, x, y
	x, y = move(x, y)	
	spiral[tostr(x, y)] = compute_spiral_value()
	local_size_length -= 1
	if local_size_length == 0:
		move = moves[move]
		if move == R or move == L:
			spiral_size_length += 1
		local_size_length = spiral_size_length
	


move = R
x = y = 0
spiral_size_length = 1
local_size_length = 1
spiral = {tostr(0,0) : 1}			


part_one_running = True
part_two_running = True
spiral_length = 1

while part_one_running or part_two_running:
	if part_one_running and spiral_length == input:
		part_one_running = False
		print("PartOne", abs(x) + abs(y))
	if part_two_running and spiral.get(tostr(x, y), 0) > input:
		part_two_running = False
		print("PartTwo", spiral[tostr(x, y)])
	next_move()
	spiral_length += 1	





