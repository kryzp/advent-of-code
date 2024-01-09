
ll = [x for x in open("input.txt").read().strip().split("\n\n")]

workflows_raw = ll[0].split("\n")
elements_raw = ll[1].split("\n")

workflows = {}
elements = []

def check_accepted_by_workflow(element, workflow):
	for rule in workflows[workflow]:
		if rule in workflows:
			return check_accepted_by_workflow(element, rule)
		elif rule == "A":
			return True
		elif rule == "R":
			return False
		else:
			check, result = rule.split(":")
			passed = False
			if ">" in check:
				var, numstr = check.split(">")
				passed = element[var] > int(numstr)
			elif "<" in check:
				var, numstr = check.split("<")
				passed = element[var] < int(numstr)
			if passed:
				if result in workflows:
					return check_accepted_by_workflow(element, result)
				elif result == "A":
					return True
				elif result == "R":
					return False
	return True

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

for e in elements:
	if check_accepted_by_workflow(e, "in"):
		result += sum(x for x in e.values())

print(result)
