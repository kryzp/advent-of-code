
# literally just wait until it stagnates :thumbsub: :)

ll = [x for x in open("input.txt").read().strip().split("\n")]

beams = [
	[0, 0, (1, 0)]
]

seen = set()

while beams:
	completed = []
	for b in beams:
		seen.add((b[0], b[1]))
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
		if b[0] < 0 or b[0] >= len(ll[0]) or b[1] < 0 or b[1] >= len(ll):
			completed.append(b)
	for c in completed:
		beams.remove(c)
	print(len(seen))
