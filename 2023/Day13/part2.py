
ll = [x for x in open("input.txt").read().strip().split("\n\n")]

x = 0

def check_horizontal_reflection(p):
	for i in range(len(p)):
		if i + 1 == len(p):
			return 0
		above = p[i::-1]
		below = p[i+1:]
		npairs = 0
		for l1, l2 in zip(above, below):
			npairs += min(len(l1), len(l2))
		if sum(1 for l1, l2 in zip(above, below) for c1, c2 in zip(l1, l2) if c1 == c2) == npairs - 1:
			return i + 1

def check_vertical_reflection(p):
	trans = list(zip(*p))
	return check_horizontal_reflection(trans)

for l in ll:
	n1 = check_vertical_reflection(l.split("\n"))
	n2 = check_horizontal_reflection(l.split("\n"))
	x += n1 + n2*100

print(x)
