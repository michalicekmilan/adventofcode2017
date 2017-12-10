
def divided(data):
	for i in data:
		for j in data:
			if i!=j and i%j == 0:
				return  int(i/j)

checksum1 = 0
checksum2 = 0

with open('input') as f:
	for l in f.readlines():
		linedata = list(map(int,l.split()))
		checksum1 += max(linedata) - min(linedata)
		checksum2 += divided(linedata)

print(checksum1)		
print(checksum2)
