from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split('\n')]

for l1 in ll:
	for l2 in ll:
		if sum(x != y for x, y in zip(l1, l2)) == 1:
			print("".join(x for x, y in zip(l1, l2) if x == y))
