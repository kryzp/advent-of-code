
ll = [x for x in open("input.txt").read().strip().split("\n")]

inst = ll[0]
nodes = {}

for l in ll[2:]:
	spl = l.split(" = ")
	spl2 = spl[1].split(", ")
	nodes[spl[0]] = (spl2[0][1:], spl2[1][:-1])

curr = "AAA"

n = 0
while True:
	i = n % len(inst)
	if inst[i] == "L":
		curr = nodes[curr][0]
	else:
		curr = nodes[curr][1]
	n += 1
	if curr == "ZZZ":
		break

print(n)
