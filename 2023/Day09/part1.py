
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

def solve(data):
	constant = True
	for i in range(len(data) - 1):
		if data[i] != data[i + 1]:
			constant = False
			break
	if constant:
		return data[-1]
	deltas = []
	for i in range(len(data) - 1):
		deltas.append(data[i + 1] - data[i])
	return data[-1] + solve(deltas)

for l in ll:
	data = [int(n) for n in l.split(" ")]
	x += solve(data)

print(x)
