import sys

sys.setrecursionlimit(150000)

ll = [x for x in open("input.txt").read().strip().split("\n")]

DIRS = [
	(-1, 0),
	(1, 0),
	(0, 1),
	(0, -1)
]

DIR_MAP = {
	'<': (-1, 0),
	'>': (1, 0),
	'^': (0, -1),
	'v': (0, 1)
}

blocks = set()

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == '#':
			blocks.add((x, y))

def is_valid_pos(pos, visited):
	px, py = pos
	return px >= 0 and px < len(ll[0]) and py >= 0 and py < len(ll) and (px, py) not in blocks and (px, py) not in visited

def add(t0, t1):
	return (t0[0] + t1[0], t0[1] + t1[1])

def explore(pos, visited, length):
	max_length = length
	
	if pos in visited:
		return max_length

	visited.add(pos)

	for diff in DIRS:
		new_pos = add(pos, diff)
		if is_valid_pos(new_pos, visited):
			px, py = new_pos
			ch = ll[py][px]
			if ch == '.':
				max_length = max(max_length, explore(new_pos, visited, length + 1))
			else:
				slip_dir = DIR_MAP[ch]
				new_new_pos = add(new_pos, slip_dir)
				max_length = max(max_length, explore(new_new_pos, visited, length + 2))

	visited.remove(pos)
	return max_length

result = explore((1, 0), set(), 0)

print(result)
