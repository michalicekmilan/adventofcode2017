L = lambda x: x+1
R = lambda x: x-1

A = [(1, R, 'B'), (0, L, 'F')]
B = [(0, R, 'C'), (0, R, 'D')]
C = [(1, L, 'D'), (1, R, 'E')]
D = [(0, L, 'E'), (0, L, 'D')]
E = [(0, R, 'A'), (1, R, 'C')]
F = [(1, L, 'A'), (1, R, 'A')]

tape = {0: 0}
position = 0
state = 'A'

for i in range(12794428):
	instructions = globals()[state][tape.get(position, 0)]
	tape[position] = instructions[0]
	position = instructions[1](position)
	state = instructions[2]

print(sum(tape.values()))	


