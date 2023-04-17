
ll = [eval("(" + x + ")") for x in open("input.txt").read().strip().split("\n")]

def dist(x, y):
	return abs(x[0] - y[0]) + abs(x[1] - y[1])

minx = min(x[0] for x in ll)
miny = min(x[1] for x in ll)
maxx = max(x[0] for x in ll)
maxy = max(x[1] for x in ll)

plot = {}

for x in range(minx, maxx + 1):
	for y in range(miny, maxy + 1):
		cd = 9999
		cp = None
		for p in ll:
			dd = dist((x, y), p)
			if dd < cd:
				cd = dd
				cp = p
			elif dd == cd:
				cp = None
		plot[(x, y)] = cp

inf = set(v for k, v in plot.items() if k[0] in (minx, maxx) or k[1] in (miny, maxy))
vv = [x for x in plot.values() if x not in inf]

maxcount = 0
largest_id = max(vv, key=lambda x: vv.count(x))

for k in plot.keys():
	if plot[k] == largest_id:
		maxcount += 1

print(maxcount)
