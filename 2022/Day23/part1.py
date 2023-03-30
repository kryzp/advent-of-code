from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

DIRS  = [(0, -1), (0, 1), (-1, 0), (1, 0)]
CHECK = [(1, 0), (1, 0), (0, 1), (0, 1)]
elves = []

def add_pos(p0, p1):
	return tuple(map(sum, zip(p0, p1)))

def elf_around(p0):
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if add_pos(p0, (dx, dy)) in elves:
				return True
	return False

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == '#':
			elves.append((x, y))

def print_out():
	mny = min(x[1] for x in elves)
	mxy = max(x[1] for x in elves)
	mnx = min(x[0] for x in elves)
	mxx = max(x[0] for x in elves)
	print(elves)
	for y in range(mny, mxy + 1):
		for x in range(mnx, mxx + 1):
			if (x, y) in elves:
				print('#', end='')
			else:
				print('.', end='')
		print()
	print()
	print()

def do_round(curr_idx):
	global elves
	proposed = []
	for e in elves:
		if elf_around(e):
			is_possible = False
			for j in range(4):
				true_index = (j + curr_idx) % 4
				dr = DIRS[true_index]
				adjacent_pos = add_pos(e, dr)
				is_possible = True
				for d in range(-1, 2):
					addition = (CHECK[true_index][0] * d, CHECK[true_index][1] * d)
					new_pos = add_pos(adjacent_pos, addition)
					if new_pos in set(elves):
						is_possible = False
						break
				if is_possible:
					proposed.append(adjacent_pos)
					break
			if not is_possible:
				proposed.append(e)
	for i in range(len(proposed)):
		if proposed.count(proposed[i]) <= 1:
			elves[i] = proposed[i]

#print_out()
for i in range(10):
	do_round(i)
	#print_out()

mny = min(x[1] for x in elves)
mxy = max(x[1] for x in elves)
mnx = min(x[0] for x in elves)
mxx = max(x[0] for x in elves)
ww = mxx - mnx + 1
hh = mxy - mny + 1

print("empty ground tiles = " + str((ww * hh) - len(elves)))
