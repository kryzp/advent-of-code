
ll = [list(x) for x in open("input.txt").read().strip().split("\n")]

CYCLES = 1_000_000_000

def do_cycle(n):
	global ll
	complete = False
	while not complete:
		complete = True
		if n == 0: # N
			for y in range(len(ll) - 1):
				for x in range(len(ll[0])):
					if ll[y][x] == "." and ll[y + 1][x] == "O":
						ll[y][x] = "O"
						ll[y + 1][x] = "."
						complete = False
		if n == 1: # W
			for y in range(len(ll)):
				for x in range(len(ll[0]) - 1):
					if ll[y][x] == "." and ll[y][x + 1] == "O":
						ll[y][x] = "O"
						ll[y][x + 1] = "."
						complete = False
		if n == 2: # S
			for y in range(len(ll) - 1):
				for x in range(len(ll[0])):
					if ll[y][x] == "O" and ll[y + 1][x] == ".":
						ll[y][x] = "."
						ll[y + 1][x] = "O"
						complete = False
		if n == 3: # E
			for y in range(len(ll)):
				for x in range(len(ll[0]) - 1):
					if ll[y][x] == "O" and ll[y][x + 1] == ".":
						ll[y][x] = "."
						ll[y][x + 1] = "O"
						complete = False

seen = []
loop = 0

for c in range(CYCLES):
	val = hash(tuple(["".join(l) for l in ll]))
	if loop == 0 and val in seen:
		start = seen.index(val)
		length = len(seen) - start
		loop = ((CYCLES - start) % length) + len(seen)
	if len(seen) == loop and loop != 0:
		break
	seen.append(val)
	for i in range(4):
		do_cycle(i)

x = 0
llr = ll[::-1]

for i in range(len(llr)):
	x += (i + 1) * llr[i].count("O")

print(x)
