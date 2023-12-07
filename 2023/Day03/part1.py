
ll = [x for x in open("input.txt").read().strip().split("\n")]

DIGS = "1234567890"

res = 0
symbols = set()

for l in ll:
	for c in l:
		if c not in '.' + DIGS:
			symbols.add(c)

seen = set()

for y in range(1, len(ll) - 1):
	for x in range(1, len(ll[y]) - 1):
		for ox in range(-1, 2):
			for oy in range(-1, 2):
				if ox == 0 and oy == 0:
					continue
				px = x + ox
				py = y + oy
				if ll[y][x] in symbols and ll[py][px] in DIGS:
					tx = px
					strs = ""
					while ll[py][tx] in DIGS:
						tx -= 1
						if ll[py][tx] not in DIGS:
							tx += 1
							break
					if (tx, py) in seen:
						continue
					inittx = tx
					while ll[py][tx] in DIGS:
						strs += ll[py][tx]
						tx += 1
						if tx == len(ll[0]):
							tx -= 1
							break
						if ll[py][tx] not in DIGS:
							tx -= 1
							break
					res += int(strs)
					seen.add((inittx, py))

print(res)
