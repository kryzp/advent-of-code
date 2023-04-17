
ll = [x for x in open("input.txt").read().strip().split('\n')]

r = 0

for l in ll:
	r += int(l)

print(r)
