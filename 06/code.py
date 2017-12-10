memory = [2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]

def redistribute(data):
	m = max(data)
	i = data.index(m)
	data[i] = 0
	for j in range(m):
		data[(i+j+1)%len(data)] += 1
	

def tostr(data):
	return "".join(map(str,data))


history = set()
cycles = 0
while tostr(memory) not in history:
	history.add(tostr(memory))
	cycles += 1
	redistribute(memory)
print(cycles)


last = tostr(memory)
redistribute(memory)
cycles = 1
while tostr(memory) != last:
	cycles += 1
	redistribute(memory)
print(cycles)

