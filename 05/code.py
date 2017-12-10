
def run(steps, step_function):
	counter = 0
	pointer = 0;
	while pointer>=0 and pointer < len(steps):
		counter += 1
		step = steps[pointer]
		steps[pointer] = step_function(step)
		pointer +=step
	return counter	


steps = []
with open('input') as f:
	steps = list(map(int, f.readlines()))	

print (run(list(steps), lambda s: s + 1))
print (run(list(steps), lambda s: s - 1 if s>=3 else s + 1))

