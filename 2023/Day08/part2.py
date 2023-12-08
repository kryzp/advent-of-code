import math

ll = [x for x in open("input.txt").read().strip().split("\n")]

inst = ll[0]
nodes = {}

for l in ll[2:]:
	spl = l.split(" = ")
	spl2 = spl[1].split(", ")
	nodes[spl[0]] = (spl2[0][1:], spl2[1][:-1])

currs = []
for name, lr in nodes.items():
	if name.endswith("A"):
		currs.append(name)

result = []
for curr in currs:
	n = 0
	while True:
		i = n % len(inst)
		if inst[i] == "L":
			curr = nodes[curr][0]
		else:
			curr = nodes[curr][1]
		n += 1
		if curr.endswith("Z"):
			break
	result.append(n)

print(math.lcm(*result))
