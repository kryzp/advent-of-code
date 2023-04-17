
ll = [x for x in open("input.txt").read().strip().split('\n')]

r = 0
seen = set()

i = 0
while True:
	l = ll[i]
	r += int(l)
	if r in seen:
		break
	seen.add(r)
	i = (i + 1) % len(ll)

print(r)
