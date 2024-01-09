
ll = [x for x in open("input.txt").read().strip().split("\n\n")]

x = 0

def check_horizontal_reflection(p):
	for i in range(len(p)):
		if i + 1 == len(p):
			return 0
		if all(l1 == l2 for l1, l2 in zip(p[i::-1], p[(i+1):])):
			return i + 1

def check_vertical_reflection(p):
	return check_horizontal_reflection(list(zip(*p)))

for l in ll:
	n1 = check_vertical_reflection(l.split("\n"))
	n2 = check_horizontal_reflection(l.split("\n"))
	x += n1 + n2*100

print(x)
