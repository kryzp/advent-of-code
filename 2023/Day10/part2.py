
import matplotlib.path

ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

def addp(p0, p1):
	return (p0[0] + p1[0], p0[1] + p1[1], p[0])

positions = []
for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == 'S':
			positions.append((x, y, 0, [(x, y)], set([(x, y)])))

loop = []

while positions:
	new_positions = []
	for p in positions:
		px, py, counter, record, seen = p
		here = ll[py][px]
		offsets = []
		if here == 'S':
			offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		elif here == '-':
			offsets = [(-1, 0), (1, 0)]
		elif here == '|':
			offsets = [(0, 1), (0, -1)]
		elif here == 'L':
			offsets = [(1, 0), (0, -1)]
		elif here == 'J':
			offsets = [(-1, 0), (0, -1)]
		elif here == '7':
			offsets = [(-1, 0), (0, 1)]
		elif here == 'F':
			offsets = [(1, 0), (0, 1)]
		for o in offsets:
			np = addp(p, o)
			npx, npy, cc = np
			if npx >= len(ll[0]) or npx < 0 or npy >= len(ll) or npy < 0:
				continue
			if ll[npy][npx] == 'S':
				if x <= counter + 1:
					x = counter + 1
					loop = record
			elif ll[npy][npx] != '.' and (npx, npy) not in seen:
				all_seen = False
				new_record = record + [(npx, npy)]
				new_seen = set(list(seen) + [(npx, npy)])
				new_positions.append((npx, npy, counter + 1, new_record, new_seen))
	positions = new_positions

area = 0

p = matplotlib.path.Path(loop)
for y in range(len(ll)):
	for x in range(len(ll[0])):
		if (x, y) in loop:
			continue
		if p.contains_point((x, y)):
			area += 1

print(area)
