from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split('\n')]

n2 = 0
n3 = 0

for l in ll:
	d = defaultdict(lambda: 0)
	for c in l:
		d[c] += 1
	off = [0, 0]
	for c, v in d.items():
		if v == 2:
			off[0] = 1
		elif v == 3:
			off[1] = 1
	n2 += off[0]
	n3 += off[1]

print(n2 * n3)
