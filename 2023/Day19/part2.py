
ll = [x for x in open("input.txt").read().strip().split("\n\n")]

workflows_raw = ll[0].split("\n")
elements_raw = ll[1].split("\n")

workflows = {}
elements = []

IDXS = "xmas"

def overlap_ranges(char, comparison, ranges, val):
	result = []
	for rng in ranges:
		rng = list(rng)
		lo, hi = rng[IDXS.index(char)]
		if comparison: # >
			lo = max(lo, val + 1)
		else: # <
			hi = min(hi, val - 1)
		if lo > hi:
			continue
		rng[IDXS.index(char)] = (lo, hi)
		result.append(tuple(rng))
	return result

def check_accepted_by_workflow(workflow):
	rule = workflow[0]
	if rule in workflows:
		return check_accepted_by_workflow(workflows[rule])
	elif rule == "A":
		return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
	elif rule == "R":
		return []
	check, result = rule.split(":")
	comparison = ">" in check
	char = ''
	val = -1
	ival = -1
	if comparison:
		char = check.split(">")[0]
		val = int(check.split(">")[1])
		ival = val + 1
	else:
		char = check.split("<")[0]
		val = int(check.split("<")[1])
		ival = val - 1
	if_passed = overlap_ranges(char, comparison, check_accepted_by_workflow([result]), val)
	if_not_passed = overlap_ranges(char, not comparison, check_accepted_by_workflow(workflow[1:]), ival)
	return if_passed + if_not_passed

for l in workflows_raw:
	spl = l.split("{")
	name = spl[0]
	rules = spl[1][:-1].split(",")
	workflows[name] = rules

for l in elements_raw:
	spl = l[1:-1].split(",")
	elem = {}
	for component in spl:
		spl2 = component.split("=")
		elem[spl2[0]] = int(spl2[1])
	elements.append(elem)

result = 0

for rng in check_accepted_by_workflow(workflows["in"]):
	comb = 1
	for lo, hi in rng:
		comb *= hi - lo + 1
	result += comb

print(result)
