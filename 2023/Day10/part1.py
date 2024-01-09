
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

def addp(p0, p1):
	return (p0[0] + p1[0], p0[1] + p1[1])

positions = []
seen = set()
for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == 'S':
			positions.append((x, y, 0))
			seen.add((x, y))

while positions:
	new_positions = []
	for p in positions:
		px, py, counter = p
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
		all_seen = True
		for o in offsets:
			np = addp(p, o)
			npx, npy = np
			if npx >= len(ll[0]) or npx < 0 or npy >= len(ll) or npy < 0:
				continue
			if (npx, npy) in seen:
				continue
			elif ll[npy][npx] != '.':
				all_seen = False
				new_positions.append((npx, npy, counter + 1))
				seen.add((npx, npy))
		if all_seen:
			x = max(x, counter + 1)
	positions = new_positions

print(x)
