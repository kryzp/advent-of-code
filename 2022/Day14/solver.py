
ll = [x for x in open("input.txt").read().strip().split("\n")]

grid = []
grid_width = -1
grid_height = -1

ID_NONE = 0
ID_ROCK = 1

SAND_FALL_POINT = (500, 0)
current_sand_pos = [0, 0]
fallen_sand = []

minimum_point_x = 99999999
maximum_point_x = -1

minimum_point_y = 0 # sand fall point
maximum_point_y = -1

def sign(n):
	if n > 0:
		return 1
	if n < 0:
		return -1
	return 0

def print_grid():
	for y in range(grid_height):
		print(str(y) + "\t", end='')
		for x in range(grid_width):
			idtype = grid[y][x]
			ch = '?'
			if idtype == ID_NONE:
				ch = '.'
			elif idtype == ID_ROCK:
				ch = '#'
			if (x + minimum_point_x, y) == SAND_FALL_POINT:
				ch = '+'
			if (x, y) in fallen_sand:
				ch = '*'
			if (x, y) == tuple(current_sand_pos):
				ch = 'O'
			print(ch, end='')
		print()

def grid_draw_rock_line(rock_line):
	global grid
	for i in range(len(rock_line) - 1):
		p1 = rock_line[i]
		p2 = rock_line[i + 1]
		p1x, p1y = p1
		p2x, p2y = p2
		p1x -= minimum_point_x
		p2x -= minimum_point_x
		dist_x = p2x - p1x
		dist_y = p2y - p1y
		max_length = max(abs(dist_x), abs(dist_y)) + 1
		for t in range(max_length):
			if p1y == p2y:
				grid[p1y][p1x + (t * sign(dist_x))] = ID_ROCK
			elif p1x == p2x:
				grid[p1y + (t * sign(dist_y))][p1x] = ID_ROCK

def generate_grid():
	global grid
	grid = [[ID_NONE for _ in range(grid_width)] for _ in range(grid_height)]
	print("GRID W: " + str(grid_width))
	print("GRID H: " + str(grid_height))
	for line in all_rock_lines:
		grid_draw_rock_line(line)

def parse_coord_string(coord_str):
	return int(coord_str[0]), int(coord_str[1])

finished = False

def is_position_valid(point):
	global grid_width
	global grid_height
	global finished
	px, py = point
	if py >= grid_height:
		finished = True
		return False
	if point in fallen_sand:
		return False
	if grid[py][px] == ID_ROCK:
		return False
	return True

all_rock_lines = []

ll.append("0,167 -> 1000,167")

for l in ll:
	coord_strs = l.split(" -> ")
	rock_line = []
	for i in range(len(coord_strs)):
		x, y = parse_coord_string(coord_strs[i].split(","))
		minimum_point_x = min(x, minimum_point_x)
		maximum_point_x = max(x, maximum_point_x)
		minimum_point_y = min(y, minimum_point_y)
		maximum_point_y = max(y, maximum_point_y)
		rock_line.append((x, y))
	all_rock_lines.append(rock_line)

grid_width  = maximum_point_x - minimum_point_x + 1
grid_height = maximum_point_y - minimum_point_y + 1

generate_grid()

current_sand_pos = [SAND_FALL_POINT[0] - minimum_point_x, SAND_FALL_POINT[1] - minimum_point_y]

n = 0

def new_sand():
	global current_sand_pos
	global fallen_sand
	global n
	n += 1
	sx = current_sand_pos[0]
	sy = current_sand_pos[1]
	fallen_sand.append((sx, sy))
	current_sand_pos = [SAND_FALL_POINT[0] - minimum_point_x, SAND_FALL_POINT[1] - minimum_point_y]

def update_sand():
	global current_sand_pos
	cx, cy = current_sand_pos
	if is_position_valid((cx, cy+1)): # down
		current_sand_pos = [cx, cy+1]
		return
	if is_position_valid((cx-1, cy+1)): # left
		current_sand_pos = [cx-1, cy+1]
		return
	if is_position_valid((cx+1, cy+1)): # right
		current_sand_pos = [cx+1, cy+1]
		return
	# all checks failed
	new_sand()

prev_pos = [-1, -1]

while prev_pos[0] != current_sand_pos[0] or prev_pos[1] != current_sand_pos[1]:
	# print(n, i)
	prev_pos = [current_sand_pos[0], current_sand_pos[1]]
	update_sand()
	# print_grid()
	# print()

print_grid()

print("total tries = " + str(n))
