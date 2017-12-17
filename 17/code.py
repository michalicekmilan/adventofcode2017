input = 386

current_position = 0
buffer = [0]

for i in range(1, 2018):
	current_position = (current_position + input)%len(buffer) + 1
	buffer.insert(current_position, i)
	
print(buffer[current_position+1])	


current_position = 0
value_after_zero = None
for i in range(1, 50000001):
	current_position = (current_position + input)%i + 1
	if current_position == 1:
		value_after_zero = i

print(value_after_zero)		

