

def generator(factor, seed, div=1):
	value = seed
	while 1:
		 value = (value * factor) % 2147483647
		 if value % div != 0:
		 	continue
		 yield value		 


def judge(gA, gB, pairs):
	c = 0
	judge = 0
	while c < pairs:
		if next(gA) & 0xFFFF == next(gB) & 0xFFFF:
			judge += 1
		c += 1
	return judge


print(judge(generator(16807, 289), generator(48271, 629), 40*1000000))
print(judge(generator(16807, 289, 4), generator(48271, 629, 8), 5*1000000))
