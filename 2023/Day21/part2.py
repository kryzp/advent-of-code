from collections import deque

ll = [x for x in open("input.txt").read().strip().split("\n")]

SIZE = len(ll)

starting_position = None

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == 'S':
			starting_position = (x, y)

nodes = set([starting_position])

def rock_at(pos):
	px, py = pos
	px_tiled = px % len(ll[0])
	py_tiled = py % len(ll)
	return ll[py_tiled][px_tiled] == '#'

def add(p0, p1):
	return (p0[0] + p1[0], p0[1] + p1[1])

def valid_points_around(pos):
	n = 0
	for o in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		po = add(pos, o)
		if not rock_at(po):
			yield po

ITER = 26501365

def solve(n, data):
	a = (data[2] - data[1]) - (data[1] - data[0])
	b = (data[1] - data[0])
	c = (data[0])
	return a*n*(n - 1)//2 + b*n + c

prev_count = 0
data = []
i = 0

while True:
	new_nodes = set()
	for n in nodes:
		for p in valid_points_around(n):
			new_nodes.add(p)
	nodes = new_nodes
	if i % SIZE == ITER % SIZE:
		data.append(len(nodes))
		if len(data) >= 3:
			i += 1
			break
	i += 1

print(solve(ITER // SIZE, data))
