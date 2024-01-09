
ll = [x for x in open("input.txt").read().strip().split("\n")]

def load_col(x, ll):
	i = 0
	base = len(ll)
	n = 0
	ret = 0
	while True:
		if ll[i][x] == 'O':
			ret += base - n
			n += 1
		elif ll[i][x] == '#':
			base = len(ll) - i - 1
			n = 0
		i += 1
		if i >= len(ll):
			break
	return ret

x = 0

for i in range(len(ll[0])):
	x += load_col(i, ll)

print(x)
