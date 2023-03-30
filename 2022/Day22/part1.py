
ll = [x for x in open("input.txt").read().split("\n")]

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

board = [list(x) for x in ll[:-2]]
maxlen = max(len(x) for x in board)

curr_facing = (1, 0)
curr_pos = (board[0].index("."), 0)

print(curr_pos)

for l in board:
	while len(l) < maxlen:
		l.append(" ")

instructions = ll[-1].replace("L", " L ").replace("R", " R ")

def add_pos(p0, p1):
	return tuple(map(sum, zip(p0, p1)))

def add_wrapped(p0, p1):
	new = add_pos(p0, p1)
	return (new[0] % len(board[0]), new[1] % len(board))

for move in instructions.split(" "):
	if move == "L":
		curr_facing = DIRECTIONS[(DIRECTIONS.index(curr_facing) + 3) % 4]
	elif move == "R":
		curr_facing = DIRECTIONS[(DIRECTIONS.index(curr_facing) + 1) % 4]
	else:
		dist = int(move)
		for i in range(dist):
			next_pos = add_wrapped(curr_pos, curr_facing)
			while board[next_pos[1]][next_pos[0]] == ' ':
				next_pos = add_wrapped(next_pos, curr_facing)
			if board[next_pos[1]][next_pos[0]] == '.':
				curr_pos = next_pos

print(1000*(1 + curr_pos[1]) + 4*(1 + curr_pos[0]) + DIRECTIONS.index(curr_facing))
