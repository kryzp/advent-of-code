
ll = [x for x in open("input.txt").read().split("\n")]

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
TILE_SIZE = 50

board = [list(x) for x in ll[:-2]]
maxlen = max(len(x) for x in board)

curr_facing = (1, 0)
curr_pos = (board[0].index("."), 0)

positions = []

for l in board:
	while len(l) < maxlen:
		l.append(" ")

instructions = ll[-1].replace("L", " L ").replace("R", " R ")

def add_pos(p0, p1):
	return tuple(map(sum, zip(p0, p1)))

def print_out():
	for y in range(len(board)):
		for x in range(len(board[y])):
			c = board[y][x]
			if (x, y) in [x[0] for x in positions]:
				idx = [x[0] for x in positions].index((x, y))
				dd = positions[idx][1]
				if dd == (1, 0):
					c = '>'
				elif dd == (-1, 0):
					c = '<'
				elif dd == (0, -1):
					c = '^'
				elif dd == (0, 1):
					c = 'v'
			print(c, end='')
		print()
	print("====================")

def add_wrapped(pos, dr):
	px, py = add_pos(pos, dr)
	# if dr == (1, 0):
	# 	if px in range(TILE_SIZE, TILE_SIZE*2) and py in range(TILE_SIZE, TILE_SIZE*2):
	# 		return (TILE_SIZE + py, TILE_SIZE - 1), (0, -1)
	# 	elif px in range(TILE_SIZE, TILE_SIZE*2) and py in range(TILE_SIZE*2, TILE_SIZE*3):
	# 		return (TILE_SIZE*3 - 1, py % TILE_SIZE), (-1, 0)
	# 	elif px in range(0, TILE_SIZE) and py in range(TILE_SIZE*3, TILE_SIZE*4):
	# 		return (TILE_SIZE + py, TILE_SIZE*3 - 1), (0, -1)
	# 	elif px in range(TILE_SIZE*2, TILE_SIZE*3) and py in range(0, TILE_SIZE):
	# 		return (TILE_SIZE*2 - 1, TILE_SIZE*2 + py), (-1, 0)
	return (px, py), dr

positions.append((curr_pos, curr_facing))

for move in instructions.split(" "):
	print_out()
	if move == "L":
		curr_facing = DIRECTIONS[(DIRECTIONS.index(curr_facing) + 3) % 4]
	elif move == "R":
		curr_facing = DIRECTIONS[(DIRECTIONS.index(curr_facing) + 1) % 4]
	else:
		dist = int(move)
		for i in range(dist):
			next_pos, new_dir = add_wrapped(curr_pos, curr_facing)
			curr_facing = new_dir
			positions.append((next_pos, curr_facing))
			while board[next_pos[1]][next_pos[0]] == ' ':
				next_pos, new_dir = add_wrapped(next_pos, curr_facing)
				curr_facing = new_dir
				positions.append((next_pos, curr_facing))
			if board[next_pos[1]][next_pos[0]] == '.':
				curr_pos = next_pos

print(1000*(1 + curr_pos[1]) + 4*(1 + curr_pos[0]) + DIRECTIONS.index(curr_facing))
