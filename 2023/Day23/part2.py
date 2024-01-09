import sys

sys.setrecursionlimit(150000)

ll = [x for x in open("input.txt").read().strip().split("\n")]

ll.insert(0, "#" * len(ll[0]))
ll.append("#" * len(ll[0]))

DIRS = [
	(-1, 0),
	(1, 0),
	(0, 1),
	(0, -1)
]

blocks = set()

START_POS = (1, 1)
END_POS = (len(ll[0]) - 2, len(ll) - 2)

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == '#':
			blocks.add((x, y))

def is_valid_pos(pos, visited):
	px, py = pos
	return px >= 0 and px < len(ll[0]) and py >= 0 and py < len(ll) and (px, py) not in blocks and (px, py) not in visited

def add(t0, t1):
	return (t0[0] + t1[0], t0[1] + t1[1])

def explore(pos, visited, adj):
	if pos == END_POS:
		return sum(visited.values())

	max_length = None
	
	for n in adj[pos]:
		if n in visited:
			continue
		visited[n] = adj[pos][n]
		res = explore(n, visited, adj)
		if max_length is None or (res is not None and res > max_length):
			max_length = res
		del visited[n]

	return max_length

adj = {}

def in_range(i, j, max_i, max_j):
	return i >= 0 and j >= 0 and i < max_i and j < max_j

def neighbors_helper(max_i, max_j, candidates):
	if max_j is None and isinstance(max_i, list):
		max_j = len(max_i[0])
		max_i = len(max_i)
	return [(i, j) for i, j in candidates if in_range(i, j, max_i, max_j)]

def neighbors(i, j, max_i, max_j=None):
	return neighbors_helper(
		max_i, max_j, [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
	)

for i, row in enumerate(ll):
	for j, c in enumerate(row):
		if c != '#':
			adjacent = dict()
			for x, y in neighbors(i, j, ll):
				if ll[x][y] != '#':
					adjacent[(y, x)] = 1
			adj[(j, i)] = adjacent

keylist = list(adj.keys())

for key in keylist:
	neighbors = adj[key]
	if len(neighbors) == 2:
		left_neighbor, right_neighbor = neighbors.keys()
		del adj[left_neighbor][key]
		del adj[right_neighbor][key]
		adj[left_neighbor][right_neighbor] = max(adj[left_neighbor].get(right_neighbor, 0),  neighbors[left_neighbor] + neighbors[right_neighbor])
		adj[right_neighbor][left_neighbor] = adj[left_neighbor][right_neighbor]
		del adj[key]

result = explore(START_POS, {START_POS: 0}, adj)

print(result)
