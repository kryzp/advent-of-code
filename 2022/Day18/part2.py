
cubes = set(tuple(int(y) for y in x.split(",")) for x in open("input.txt").read().strip().split("\n"))

MIN_BOUND = tuple(min(c[i]-1 for c in cubes) for i in range(3))
MAX_BOUND = tuple(max(c[i]+1 for c in cubes) for i in range(3))

SIDES = [
	(+1,  0,  0), (-1,  0,  0), # x
	( 0, +1,  0), ( 0, -1,  0), # y
	( 0,  0, +1), ( 0,  0, -1)  # z
]

def add(c0, c1):
	return tuple(map(sum, zip(c0, c1)))

def in_bounds(c):
	return all(MIN_BOUND[i] <= c[i] <= MAX_BOUND[i] for i in range(3))

total_area = 0
queue = [MIN_BOUND]
discovered = set()

while queue:
	c = queue.pop(0)
	if c in cubes:
		total_area += 1
		continue
	if c not in discovered:
		discovered.add(c)
		for s in SIDES:
			n = add(c, s)
			if in_bounds(n):
				queue.append(n)

print("total area = " + str(total_area))
