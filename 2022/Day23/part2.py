from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

DIRS  = [(0, -1), (0, 1), (-1, 0), (1, 0)]
CHECK = [(1, 0), (1, 0), (0, 1), (0, 1)]
elves = []

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == '#':
			elves.append((x, y))

def add_pos(p0, p1):
	return tuple(map(sum, zip(p0, p1)))

def elf_around(p0, elves):
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if (dx, dy) != (0, 0) and add_pos(p0, (dx, dy)) in elves:
				return True
	return False

def do_round(elves, curr_idx):
	tester_set = set(elves)
	proposed = []
	for e in elves:
		if elf_around(e, tester_set):
			is_possible = False
			for j in range(4):
				j = (j + curr_idx) % 4
				dr = DIRS[j]
				adjacent_pos = add_pos(e, dr)
				is_possible = True
				for d in range(-1, 2):
					addition = (CHECK[j][0] * d, CHECK[j][1] * d)
					new_pos = add_pos(adjacent_pos, addition)
					if new_pos in tester_set:
						is_possible = False
						break
				if is_possible:
					proposed.append(adjacent_pos)
					break
			if not is_possible:
				proposed.append(e)
		else:
			proposed.append(e)
	new_elves = []
	for i in range(len(proposed)):
		if proposed.count(proposed[i]) > 1:
			new_elves.append(elves[i])
		else:
			new_elves.append(proposed[i])
	return new_elves

i = 0

while True:
	print("current round = " + str(i))
	new_elves = do_round(elves, i)
	if tuple(new_elves) == tuple(elves):
		print("round where nobody moved = " + str(i + 1))
		break
	elves = new_elves
	i += 1
