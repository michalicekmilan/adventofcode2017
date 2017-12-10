import re

exp_re = re.compile("(\S*) (\S*) (\S*) if (\S*) (\S*) (\S*)")

registers = {}
max_reg_value = 0

with open('input') as f:
	for l in f.readlines():
		m = exp_re.match(l)
		
		condition = str(registers.get(m.group(4), 0)) + m.group(5) + m.group(6)
		if eval(condition):
			reg = m.group(1)
			op = m.group(2)
			value = int(m.group(3))
						
			regvalue = registers.get(reg, 0)
			registers[reg] = regvalue + value if op == "inc" else regvalue - value
			if registers[reg] > max_reg_value:
				max_reg_value = registers[reg]


print(max(registers.values()))
print(max_reg_value)
