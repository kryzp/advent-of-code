
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

for l in ll:
	spl = l.split(': ')
	spl2 = spl[1].split(" | ")
	winning = set()
	for m in spl2[0].split(" "):
		if m != "":
			winning.add(int(m.strip()))
	mine = set()
	for p in spl2[1].split(" "):
		if p != "":
			mine.add(int(p.strip()))
	n = len(winning.intersection(mine))
	if n != 0:
		x += 2 ** (n - 1)

print(x)
