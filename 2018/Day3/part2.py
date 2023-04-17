from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

overlap = defaultdict(lambda: 0)
areas = []

for l in ll:
	idd = int(l.split(' ')[0][1:])
	coord = l.split(' ')[2]
	coord = coord[:(len(coord) - 1)]
	coord = [int(x) for x in coord.split(',')]
	dims = [int(x) for x in l.split(' ')[3].split('x')]
	a = set()
	for w in range(dims[0]):
		for h in range(dims[1]):
			a.add((coord[0] + w, coord[1] + h))
			overlap[(coord[0] + w, coord[1] + h)] += 1
	areas.append((idd, a))

for idd, a in areas:
	b = True
	for p in a:
		if overlap[p] != 1:
			b = False
			break
	if b:
		print(idd)
		break
