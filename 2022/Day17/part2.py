
# me and the boys playing tetris in aoc22d17

shapes = ['-', '+', '/', '|', '*']
jet_pattern = open("input.txt").read()
curr_jet = 0
curr_shape = 0

rows = []
ROW_W = 7

def is_empty_row(r):
	return r == ([0] * ROW_W)

def calc_tower_height():
	global rows
	counter = 0
	for r in rows:
		if not is_empty_row(r):
			counter += 1
	return counter

def new_row(r):
	global rows
	rows.insert(0, r)

def start_new_block():
	global rows
	length = len(rows)
	for i in range(length, -1, -1):
		if len(rows) == 0:
			break
		if is_empty_row(rows[0]):
			rows.pop(0)
		else:
			break
	for i in range(3):
		rows.insert(0, [0] * ROW_W)
	sh = shapes[curr_shape]
	if sh == '-':
		new_row([0, 0, 1, 1, 1, 1, 0])
	elif sh == '+':
		new_row([0, 0, 0, 1, 0, 0, 0])
		new_row([0, 0, 1, 1, 1, 0, 0])
		new_row([0, 0, 0, 1, 0, 0, 0])
	elif sh == '/':
		new_row([0, 0, 1, 1, 1, 0, 0])
		new_row([0, 0, 0, 0, 1, 0, 0])
		new_row([0, 0, 0, 0, 1, 0, 0])
	elif sh == '|':
		new_row([0, 0, 1, 0, 0, 0, 0])
		new_row([0, 0, 1, 0, 0, 0, 0])
		new_row([0, 0, 1, 0, 0, 0, 0])
		new_row([0, 0, 1, 0, 0, 0, 0])
	elif sh == '*':
		new_row([0, 0, 1, 1, 0, 0, 0])
		new_row([0, 0, 1, 1, 0, 0, 0])

def out_of_bounds(pos, offset):
	offx, offy = offset
	sh = shapes[curr_shape]
	yy = offy + pos
	if pos < 0 or pos >= len(rows):
		return True
	if yy < 0 or yy >= len(rows):
		return True
	for i in range(ROW_W):
		xx = offx + i
		if rows[pos][i] == 1:
			if sh == '-':
				if xx < 0 or xx >= ROW_W:
					return True
				if xx + 3 >= ROW_W or yy > len(rows):
					return True
				if rows[yy][xx] == 2 or rows[yy][xx + 1] == 2 or rows[yy][xx + 2] == 2 or rows[yy][xx + 3] == 2:
					return True
			elif sh == '+':
				if xx - 1 < 0 or xx >= ROW_W:
					return True
				if xx + 1 >= ROW_W or yy + 3 > len(rows):
					return True
				if rows[yy][xx] == 2 or rows[yy + 1][xx - 1] == 2 or rows[yy + 1][xx] == 2 or rows[yy + 1][xx + 1] == 2 or rows[yy + 2][xx] == 2:
					return True
			elif sh == '/':
				if xx - 2 < 0 or xx >= ROW_W:
					return True
				if xx >= ROW_W or yy + 3 > len(rows):
					return True
				if rows[yy][xx] == 2 or rows[yy + 1][xx] == 2 or rows[yy + 2][xx] == 2 or rows[yy + 2][xx - 1] == 2 or rows[yy + 2][xx - 2] == 2:
					return True
			elif sh == '|':
				if xx < 0 or xx >= ROW_W:
					return True
				if xx >= ROW_W or yy + 4 > len(rows):
					return True
				if rows[yy][xx] == 2 or rows[yy + 1][xx] == 2 or rows[yy + 2][xx] == 2 or rows[yy + 3][xx] == 2:
					return True
			elif sh == '*':
				if xx < 0 or xx >= ROW_W:
					return True
				if xx + 1 >= ROW_W or yy + 2 > len(rows):
					return True
				if rows[yy][xx] == 2 or rows[yy][xx + 1] == 2 or rows[yy + 1][xx] == 2 or rows[yy + 1][xx + 1] == 2:
					return True
			break
	return False

def move_side(pos, amt, nrows):
	global rows
	srt = -1
	end = -1
	dt = -1
	if amt < 0:
		srt = 0
		end = ROW_W
		dt = 1
	elif amt > 0:
		srt = ROW_W - 1
		end = -1
		dt = -1
	for i in range(nrows):
		r = rows[pos+i]
		for j in range(srt, end, dt):
			if r[j] == 1:
				r[j + amt] = 1
				r[j] = 0

def move_down(pos, nrows):
	global rows
	for i in range(nrows - 1, -1, -1):
		r = rows[pos + i]
		to = rows[pos + i + 1]
		for j in range(len(r)):
			if r[j] == 1:
				to[j] = 1
				r[j] = 0

def try_move_block(pos, offset):
	global rows
	offx, offy = offset
	def mark_done(n):
		for i in range(n):
			rows[i+pos] = [2 if x == 1 else x for x in rows[i+pos]]
	sh = shapes[curr_shape]
	nrows = -1
	if sh == '-': nrows = 1
	elif sh == '+': nrows = 3
	elif sh == '/': nrows = 3
	elif sh == '|': nrows = 4
	elif sh == '*': nrows = 2
	if out_of_bounds(pos, offset):
		if offx == 0:
			mark_done(nrows)
		return False
	if offy == 0:
		move_side(pos, offx, nrows)
	elif offx == 0:
		move_down(pos, nrows)
	return True

def update_block():
	global curr_jet
	pos = 0
	while True:
		if jet_pattern == 5:
			rock_skipcks
		dir_char = jet_pattern[curr_jet]
		direction = -1 if dir_char == '<' else 1
		try_move_block(pos, (direction, 0))
		moved = try_move_block(pos, (0, 1))
		curr_jet = (curr_jet + 1) % len(jet_pattern)
		if not moved:
			break
		pos += 1
		if curr_jet == 0 and curr_shape == 0:
			print("E")

def print_out():
	for r in rows:
		for c in r:
			if c == 0:
				print(".", end='')
			elif c == 1:
				print("@", end='')
			elif c == 2:
				print("#", end='')
		print()

prev_height = 0
prev_shape = 0
prev_diff_height = -1

i = 0

hh_add = 0
target = 1_000_000_000_000

while i < target:
	if curr_jet == 5:
		hh = calc_tower_height()
		diff = hh - prev_height
		diff_sh = i - prev_shape
		prev_shape = i
		if diff == prev_diff_height:
			part_count = (target - i) // diff_sh
			hh_add = part_count * diff
			i += part_count * diff_sh
		prev_diff_height = diff
		prev_height = hh
	start_new_block()
	update_block()
	i += 1
	curr_shape = i % len(shapes)

print("tower height =", calc_tower_height() + hh_add)
