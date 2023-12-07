
ll = [x for x in open("input.txt").read().strip().split("\n\n")]
seeds = [int(n) for n in ll[0].split(": ")[1].split(" ")]

def check_rng(n, src, rng):
	return n >= src and n < (src + rng)

def map_seed_back(seed, src, dst, rng):
	if check_rng(seed, dst, rng):
		return seed - dst + src
	return seed

def do_mapping_back(seed, ranges):
	s = seed
	for mapping in ranges:
		dst, src, rng = mapping
		t = s
		s = map_seed_back(s, src, dst, rng)
		if s != t:
			return s
	return s

def is_seed_valid(seed, seed_ranges):
	for rng in seed_ranges:
		range_base, range_length = rng
		if check_rng(seed, range_base, range_length):
			return True
	return False

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

seed_ranges = []
for i in range(0, len(seeds), 2):
	a = seeds[i + 0]
	b = seeds[i + 1]
	seed_ranges.append((a, b))

# essentially my idea was just to go backwards in reverse starting
# at the end and moving up until i hit a valid seed, and since
# we move up starting at zero that must also be the minimum location :)

x = 0

while True:
	curr = x
	for ranges in mappings[::-1]:
		curr = do_mapping_back(curr, ranges)
	if is_seed_valid(curr, seed_ranges):
		break
	x += 1

print(x)
