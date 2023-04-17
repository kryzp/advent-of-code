from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

overlap = defaultdict(lambda: 0)

for l in ll:
	coord = l.split(' ')[2]
	coord = coord[:(len(coord) - 1)]
	coord = [int(x) for x in coord.split(',')]
	dims = [int(x) for x in l.split(' ')[3].split('x')]
	for w in range(dims[0]):
		for h in range(dims[1]):
			overlap[(coord[0] + w, coord[1] + h)] += 1

print(len([o for o in overlap.values() if o > 1]))
