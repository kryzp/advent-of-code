
ll = [x for x in open("input.txt").read().strip().split("\n")]

galaxies = []

for y in range(len(ll)):
	for x in range(len(ll[0])):
		if ll[y][x] == '#':
			galaxies.append((x, y))

def is_empty_col(x):
	for y in range(len(ll)):
		if ll[y][x] == '#':
			return False
	return True

def is_empty_row(y):
	for x in range(len(ll[0])):
		if ll[y][x] == '#':
			return False
	return True

n = 0
seen = set()

for galaxy in galaxies:
	for galaxy2 in galaxies:
		if galaxy == galaxy2 or (galaxy, galaxy2) in seen or (galaxy2, galaxy) in seen:
			continue
		dx = galaxy2[0] - galaxy[0]
		dy = galaxy2[1] - galaxy[1]
		dist = abs(dx) + abs(dy)
		for x in range(abs(dx) - 1):
			if is_empty_col(min(galaxy[0], galaxy2[0]) + x + 1):
				dist += 1
		for y in range(abs(dy) - 1):
			if is_empty_row(min(galaxy[1], galaxy2[1]) + y + 1):
				dist += 1
		n += dist
		seen.add((galaxy, galaxy2))

print(n)
