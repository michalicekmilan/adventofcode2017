
get_scanner_position = lambda pico, depth: abs((pico + (depth-1)) % ((depth-1) * 2) - (depth - 1));	

layers = {}
with open('input') as f:
	for l in f.readlines():
		id, depth  = l.split(':')
		layers[int(id)] = int(depth)

	
def get_severity():		 
	severity = 0
	for pico in range(max(layers)+1):
		if pico in layers and get_scanner_position(pico, layers[pico]) == 0:
				severity += pico * layers[pico]
	return severity			


def packet_passed(delay):		 
	for pico in range(delay, delay+max(layers)+1):
		layer = pico - delay
		if layer in layers and get_scanner_position(pico, layers[layer]) == 0:
				return False
	return True			

delay = 0
while not packet_passed(delay):
	delay += 1


print(get_severity())	
print(delay)	


