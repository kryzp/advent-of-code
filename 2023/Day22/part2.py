from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n")]

bricks = []

for l in ll:
	spl = l.split("~")
	data1 = spl[0].split(",")
	data2 = spl[1].split(",")
	bricks.append((
		int(data1[0]), int(data1[1]), int(data1[2]),
		int(data2[0]), int(data2[1]), int(data2[2]),
	))

def positionsof(brick, zo):
	for x in range(brick[0], brick[3] + 1):
		for y in range(brick[1], brick[4] + 1):
			for z in range(brick[2], brick[5] + 1):
				yield (x, y, z + zo)

full = {}
fell = []

ordered = sorted(bricks, key=lambda x: x[2])

for brick in ordered:
	while True:
		moved = (
			brick[0], brick[1], brick[2] - 1,
			brick[3], brick[4], brick[5] - 1
		)
		if not any(pos in full for pos in positionsof(moved, 0)) and min(brick[2], brick[5]) > 1:
			brick = moved
		else:
			for pos in positionsof(brick, 0):
				full[pos] = brick
			fell.append(brick)
			break

above = defaultdict(set)
below = defaultdict(set)

for brick in fell:
	inthisbrick = set(positionsof(brick, 0))
	for pos in positionsof(brick, -1):
		if pos in full and pos not in inthisbrick:
			above[full[pos]].add(brick)
			below[brick].add(full[pos])

falling = set()

def falls(brick):
	global falling
	if brick in falling:
		return
	falling.add(brick)
	for parent in above[brick]:
		if not len(below[parent] - falling):
			falls(parent)

def n_disintegrated(disintegrated):
	global falling
	falling = set()
	falls(disintegrated)
	return len(falling) - 1

result = 0

for brick in fell:
	result += n_disintegrated(brick)

print(result)
