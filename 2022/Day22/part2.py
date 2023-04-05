
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
	print(curr_pos, curr_facing)
	for y in range(len(board)):
		for x in range(len(board[y])):
			c = board[y][x]
			if (x, y) in [p[0] for p in positions]:
				idx = [p[0] for p in positions].index((x, y))
				dr = positions[idx][1]
				if dr == (1, 0):
					c = '>'
				elif dr == (-1, 0):
					c = '<'
				elif dr == (0, -1):
					c = '^'
				elif dr == (0, 1):
					c = 'v'
			if curr_pos[0] == x and curr_pos[1] == y:
				c = '@'
			print(c, end='')
		print()
	print("====================")

# pain
def add_wrapped(pos, dr):
	px, py = add_pos(pos, dr)
	if dr == (1, 0):
		if px in range(TILE_SIZE * 3, TILE_SIZE * 4) and py in range(0, TILE_SIZE):
			return (TILE_SIZE*2 - 1, TILE_SIZE*3 - py - 1), (-1, 0)
		elif px in range(TILE_SIZE * 2, TILE_SIZE * 3) and py in range(TILE_SIZE, TILE_SIZE * 2):
			return (TILE_SIZE + py, TILE_SIZE - 1), (0, -1)
		elif px in range(TILE_SIZE * 2, TILE_SIZE * 3) and py in range(TILE_SIZE * 2, TILE_SIZE * 3):
			return (TILE_SIZE*3 - 1, TILE_SIZE - (py - TILE_SIZE * 2) - 1), (-1, 0)
		elif px in range(TILE_SIZE, TILE_SIZE * 2) and py in range(TILE_SIZE * 3, TILE_SIZE * 4):
			return (TILE_SIZE + (py - TILE_SIZE*3), TILE_SIZE*3 - 1), (0, -1)
	elif dr == (-1, 0):
		if px in range(0, TILE_SIZE) and py in range(0, TILE_SIZE):
			return (0, TILE_SIZE*3 - py - 1), (1, 0)
		elif px in range(0, TILE_SIZE) and py in range(TILE_SIZE, TILE_SIZE * 2):
			return (py - TILE_SIZE, TILE_SIZE * 2), (0, 1)
		elif px in range(-TILE_SIZE, 0) and py in range(TILE_SIZE * 2, TILE_SIZE * 3):
			return (TILE_SIZE, TILE_SIZE - (py - TILE_SIZE*2) - 1), (1, 0)
		elif px in range(-TILE_SIZE, 0) and py in range(TILE_SIZE * 3, TILE_SIZE * 4):
			return (TILE_SIZE + (py - TILE_SIZE*3), 0), (0, 1)
	elif dr == (0, 1):
		if px in range(TILE_SIZE * 2, TILE_SIZE * 3) and py in range(TILE_SIZE, TILE_SIZE * 2):
			return (TILE_SIZE*2 - 1, px - TILE_SIZE), (-1, 0)
		elif px in range(TILE_SIZE, TILE_SIZE * 2) and py in range(TILE_SIZE * 3, TILE_SIZE * 4):
			return (TILE_SIZE - 1, TILE_SIZE*3 + (px - TILE_SIZE)), (-1, 0)
		elif px in range(0, TILE_SIZE) and py in range(TILE_SIZE * 4, TILE_SIZE * 5):
			return (TILE_SIZE*2 + px, 0), (0, 1)
	elif dr == (0, -1):
		if px in range(0, TILE_SIZE) and py in range(TILE_SIZE, TILE_SIZE * 2):
			return (TILE_SIZE, px + TILE_SIZE), (1, 0)
		elif px in range(TILE_SIZE, TILE_SIZE * 2) and py in range(-TILE_SIZE, 0):
			return (0, px + TILE_SIZE*2), (1, 0)
		elif px in range(TILE_SIZE * 2, TILE_SIZE * 3) and py in range(-TILE_SIZE, 0):
			return (px - TILE_SIZE*2, TILE_SIZE*4 - 1), (0, -1)
	return (px, py), dr

positions.append((curr_pos, curr_facing))

for move in instructions.split(" "):
	if move == "L":
		curr_facing = DIRECTIONS[(DIRECTIONS.index(curr_facing) + 3) % 4]
	elif move == "R":
		curr_facing = DIRECTIONS[(DIRECTIONS.index(curr_facing) + 1) % 4]
	else:
		for i in range(int(move)):
			next_pos, new_dir = add_wrapped(curr_pos, curr_facing)
			if board[next_pos[1]][next_pos[0]] == '.':
				curr_facing = new_dir
				curr_pos = next_pos
				positions.append((curr_pos, curr_facing))
		#print_out()

print_out()

res = (1000 * (curr_pos[1] + 1)) + (4 * (1 + curr_pos[0])) + DIRECTIONS.index(curr_facing)
print(res)
print(res > 16354 and res < 114132 and res not in [126109, 21334, 136292, 53263, 63300, 113122, 190080, 105310, 43258, 29333])
