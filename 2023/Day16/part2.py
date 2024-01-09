
ll = [x for x in open("input.txt").read().strip().split("\n")]

def solve(start_pos_x, start_pos_y, start_dir):
	beams = [[start_pos_x, start_pos_y, start_dir]]
	seen = set()
	seen_pos = set()
	while beams:
		completed = []
		for b in beams:
			if b[0] < 0 or b[0] >= len(ll[0]) or b[1] < 0 or b[1] >= len(ll):
				completed.append(b)
				continue
			if (b[0], b[1], b[2][0], b[2][1]) in seen:
				completed.append(b)
				continue
			seen.add((b[0], b[1], b[2][0], b[2][1]))
			seen_pos.add((b[0], b[1]))
			here = ll[b[1]][b[0]]
			if here == ".":
				pass
			elif here == "|":
				if b[2] == (1, 0):
					b[2] = (0, 1)
					beams.append([b[0], b[1], (0, -1)])
				elif b[2] == (-1, 0):
					b[2] = (0, 1)
					beams.append([b[0], b[1], (0, -1)])
				elif b[2] == (0, 1):
					pass
				elif b[2] == (0, -1):
					pass
			elif here == "-":
				if b[2] == (1, 0):
					pass
				elif b[2] == (-1, 0):
					pass
				elif b[2] == (0, 1):
					b[2] = (1, 0)
					beams.append([b[0], b[1], (-1, 0)])
				elif b[2] == (0, -1):
					b[2] = (1, 0)
					beams.append([b[0], b[1], (-1, 0)])
			elif here == "\\":
				if b[2] == (1, 0):
					b[2] = (0, 1)
				elif b[2] == (-1, 0):
					b[2] = (0, -1)
				elif b[2] == (0, 1):
					b[2] = (1, 0)
				elif b[2] == (0, -1):
					b[2] = (-1, 0)
			elif here == "/":
				if b[2] == (1, 0):
					b[2] = (0, -1)
				elif b[2] == (-1, 0):
					b[2] = (0, 1)
				elif b[2] == (0, 1):
					b[2] = (-1, 0)
				elif b[2] == (0, -1):
					b[2] = (1, 0)
			b[0] += b[2][0]
			b[1] += b[2][1]
		for c in completed:
			beams.remove(c)
	return len(seen_pos)

result = 0

for x in range(len(ll[0])):
	for d in [(-1, 0), (1, 0), (0, 1)]:
		result = max(result, solve(x, 0, d))
	for d in [(-1, 0), (1,0 ), (0, -1)]:
		result = max(result, solve(x, len(ll), d))

for y in range(len(ll)):
	for d in [(1, 0), (0, -1), (0, 1)]:
		result = max(result, solve(0, y, d))
	for d in [(-1, 0), (0, -1), (0, 1)]:
		result = max(result, solve(len(ll[0]), y, d))

print(result)
