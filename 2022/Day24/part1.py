
ll = [x for x in open("input.txt").read().strip().split("\n")]

DIRS = {
	'<': (-1,  0),
	'>': ( 1,  0),
	'v': ( 0,  1),
	'^': ( 0, -1)
}

def add_t(t0, t1):
	return tuple(map(sum, zip(t0, t1)))

START = (ll[0].index('.'), 0)
END = (ll[-1].index('.'), len(ll)-1)

blizzards = []
navigable = set()
not_navigable = set()

for y in range(len(ll)):
	l = ll[y]
	for x in range(len(l)):
		c = l[x]
		if c in DIRS or c == '.':
			navigable.add((x, y))
		if c in DIRS:
			blizzards.append((c, (x, y)))

print(len(ll), len(ll[0]))

def print_out():
	for y in range(len(ll)):
		for x in range(len(ll[0])):
			pp = (x, y)
			if pp == START:
				print('S', end='')
			elif pp == END:
				print('E', end='')
			elif pp in [x[1] for x in blizzards]:
				print([x[0] for x in blizzards if x[1] == pp][0], end='')
			elif x == 0 or x == len(ll[0])-1 or y == 0 or y == len(ll)-1:
				print('#', end='')
			else:
				print('.', end='')
		print()
	print()

def update(blizzards):
	result = []
	for b in blizzards:
		tp, pos = b
		dr = DIRS[tp]
		pos = add_t(pos, dr)
		if pos[0] <= 0:
			pos = (len(ll[0])-1-1, pos[1])
		if pos[0] >= len(ll[0])-1:
			pos = (1, pos[1])
		if pos[1] <= 0:
			pos = (pos[0], len(ll)-2)
		if pos[1] >= len(ll)-1:
			pos = (pos[0], 1)
		result.append((tp, pos))
	return result

possible_path = set()
possible_path.add(START)

def neighbours(pos):
	yield pos
	for dr in DIRS.values():
		yield add_t(pos, dr)

i = 0
finished = False
while not finished:
	# print_out()
	blizzards = update(blizzards)
	not_navigable = set(b[1] for b in blizzards)
	new_possible_path = set()
	for p in possible_path:
		for n in neighbours(p):
			if n == END:
				print("finished minute = " + str(i + 1))
				finished = True
				break
			if n in navigable and n not in not_navigable:
				new_possible_path.add(n)
		if finished:
			break
	possible_path = new_possible_path
	i += 1
