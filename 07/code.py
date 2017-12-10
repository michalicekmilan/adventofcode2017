class Program():

	def __init__(self, name, weight, discs):
		self.name = name
		self.weight = weight
		self.discs = discs
		self.parent = None
		self.children = []

	def isBalanced(self):
		return len(set([c.fullWeight() for c in self.children])) <= 1 

	def fullWeight(self):
		w = self.weight
		for c in self.children:
			w += c.fullWeight()
		return w	


def parseInput():
	programs = {}
	with open('input') as f:
		for l in f.readlines():
			sp = list(map(str.strip, l.split('->')))
			name = sp[0].split(' ')[0]
			weight = int(sp[0].split(' ')[1][1:-1])
			discs = []
			if len(sp) == 2:
				discs = map(str.strip,sp[1].split(","))
			programs[name] = (Program(name, weight, discs))
	return programs
	

programs = parseInput()
for p in programs.values():
	for d in p.discs:
		programs[d].parent = p
		p.children.append(programs[d])
		
for p in programs.values():
	if p.parent is None:
		print(p.name)
	
for p in programs.values():
	if not p.isBalanced():
		print(p.name, p.weight)
		for d in p.children:
			print(d.weight, d.fullWeight())


