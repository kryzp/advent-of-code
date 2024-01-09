from collections import deque

ll = [x for x in open("input.txt").read().strip().split("\n")]

starting_position = None

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == 'S':
			starting_position = (x, y)

nodes = set([starting_position])

def valid_points_around(pos):
	px, py = pos
	if px - 1 >= 0:
		if ll[py][px - 1] != '#':
			yield (px - 1, py)
	if px + 1 < len(ll[0]):
		if ll[py][px + 1] != '#':
			yield (px + 1, py)
	if py - 1 >= 0:
		if ll[py - 1][px] != '#':
			yield (px, py - 1)
	if py + 1 < len(ll):
		if ll[py + 1][px] != '#':
			yield (px, py + 1)

for _ in range(64):
	new_nodes = set()
	for n in nodes:
		for p in valid_points_around(n):
			new_nodes.add(p)
	nodes = new_nodes
	print(len(nodes))
