
with open('input') as f:
	stream = f.readline()

in_garbage = False
ignore_next = False
garbage_chars = 0

groups = 0
level = 0
score = 0

for c in stream:
	if ignore_next:
		ignore_next = False
		continue
	elif c == '<' :
		if in_garbage:
			garbage_chars += 1
		in_garbage = True
		continue
	elif c == '>':
		in_garbage = False
		continue
	elif c == '!':
		ignore_next = True
		continue
	
	if in_garbage:
		garbage_chars += 1
		continue	
	
	if c == '{':
		groups += 1
		level += 1
		score += level
	elif c == '}':
		level -= 1
			 		 	
print(score)
print(garbage_chars)
