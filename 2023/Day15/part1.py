
ll = [x for x in open("input.txt").read().strip().split(",")]

def hashof(l):
	ret = 0
	for c in l:
		ret += ord(c)
		ret = (ret * 17) % 256
	return ret

print(sum(hashof(l) for l in ll))
