import functools

input = "31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"

def get_list_range(lst, fr, to):
	r = []
	for i in range(fr, to):
		r.append(lst[i%len(lst)])
	return r

def set_list_range(lst, sublist, fr):
	for i in range(len(sublist)):
		lst[(fr+i)%len(lst)] = sublist[i]
	
def process(circular_list, lengths, current_position, skip_size):
	for length in lengths:
		sublist = get_list_range(circular_list, current_position, current_position+length)
		set_list_range(circular_list, sublist[::-1], current_position)
		current_position += length + skip_size
		skip_size += 1
	return current_position, skip_size

#Part One
circular_list  = [i for i in range(0,256)]
process(circular_list, map(int,input.split(',')), 0, 0)
print(circular_list[0]*circular_list[1])

#Part Two
circular_list  = [i for i in range(0,256)]
current_position = 0
skip_size = 0

for r in range(64): 
	current_position, skip_size = process(circular_list,
		map(int,list(map(ord,input))+"17,31,73,47,23".split(",")), 
		current_position, skip_size)

dense_hash = []
for i in (range(16)):
	dense_hash.append(functools.reduce(lambda j, k: int(j) ^ int(k), 
		circular_list[16*i:16*i+16])) 	
		
print("".join(map("{:02x}".format, dense_hash)))







