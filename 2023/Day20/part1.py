from collections import deque

ll = [x for x in open("input.txt").read().strip().split("\n")]

from_to = {}

conjugates = {}
flip_flops = {}

for l in ll:
	spl = l.split(" -> ")
	to = spl[1].split(", ")

	t = spl[0][0]
	if spl[0] == "broadcaster":
		from_to["broadcaster"] = to
	else:
		from_node = spl[0][1:]
		from_to[from_node] = to

	if t == "&":
		conjugates[from_node] = {}
	elif t == "%":
		flip_flops[from_node] = False

for from_node, to in from_to.items():
	for dest in to:
		if dest in conjugates:
			conjugates[dest][from_node] = False

total_high_pulses = 0
total_low_pulses = 0

for _ in range(1000):
	total_low_pulses += 1 + len(from_to["broadcaster"])

	queue = deque()
	
	for dest in from_to["broadcaster"]:
		queue.append((0, "broadcaster", dest))

	while queue:
		current_is_high, src, name = queue.popleft()

		if name == "rx":
			continue

		is_high = False
		
		if name in flip_flops:
			if current_is_high:
				continue
			flip_flops[name] = not flip_flops[name]
			if flip_flops[name]:
				is_high = True
		elif name in conjugates:
			conjugates[name][src] = current_is_high
			for n in conjugates[name].values():
				if n == 0:
					is_high = True
					break

		if is_high:
			total_high_pulses += len(from_to[name])
		else:
			total_low_pulses += len(from_to[name])

		for dest in from_to[name]:
			queue.append((is_high, name, dest))

print(total_low_pulses * total_high_pulses)
