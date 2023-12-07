from collections import defaultdict

ll = [x for x in open("input.txt").read().strip().split("\n\n")]
seeds = [int(n) for n in ll[0].split(": ")[1].split(" ")]

def check_rng(n, src, rng):
	return n >= src and n < (src + rng)

def map_seed(seed, src, dst, rng):
	if check_rng(seed, src, rng):
		return seed - src + dst
	return seed

def do_mapping(seed, data):
	s = seed
	for entry in data:
		dst, src, rng = entry
		t = s
		s = map_seed(s, src, dst, rng)
		if s != t:
			return s
	return s

mappings = []
for l in ll[1:]:
	spl = l.split("\n")
	res = []
	for entry in spl[1:]:
		spl2 = entry.split(" ")
		destr = int(spl2[0])
		srcr = int(spl2[1])
		rangel = int(spl2[2])
		res.append((destr, srcr, rangel))
	mappings.append(res)

x = 99999999999

for seed in seeds:
	curr = seed
	for mapping in mappings:
		curr = do_mapping(curr, mapping)
	x = min(curr, x)
			
print(x)
