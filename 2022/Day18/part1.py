
cubes = set(
	tuple(int(y) for y in x.split(",")) for x in open("input.txt")
		.read()
		.strip()
		.split("\n")
)

def add(c0, c1):
	return (c0[0] + c1[0], c0[1] + c1[1], c0[2] + c1[2])

total_area = 0

for c in cubes:
	for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
		if add(c, d) not in cubes:
			total_area += 1

print("total area = " + str(total_area))
