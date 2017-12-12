
programs = {}

with open('input') as f:
	for l in f.readlines():
		pid, pipes = l.split(' <-> ')
		programs[int(pid)] = map(int, pipes.split(','))


def compose_group(pid, members = None):
	if members == None:
		members = [] 
	members.append(pid)
	for p in programs[pid]:
		if p not in members:
			compose_group(p, members)
	return members	


pids = list(programs)
groups = []

while pids:
	g = compose_group(pids[0])
	groups.append(g)
	pids = [p for p in pids if p not in g]

print(len(groups[0]))	
print(len(groups))	







