from collections import deque
import math

ll = [x for x in open("input.txt").read().strip().split("\n")]

from_to = {}

conjugates = {}
flip_flops = {}

rx_parent = ""

for l in ll:
	spl = l.split(" -> ")
	to = spl[1].split(", ")

	t = spl[0][0]
	if spl[0] == "broadcaster":
		from_node = "broadcaster"
	else:
		from_node = spl[0][1:]

	from_to[from_node] = to

	if "rx" in to:
		rx_parent = from_node

	if t == "&":
		conjugates[from_node] = {}
	elif t == "%":
		flip_flops[from_node] = False

for from_node, to in from_to.items():
	for dest in to:
		if dest in conjugates:
			conjugates[dest][from_node] = False

button_presses = 0
button_presses_list = []
seen = set()

while len(button_presses_list) < len(conjugates[rx_parent]):
	button_presses += 1

	queue = deque()
	
	for dest in from_to["broadcaster"]:
		queue.append((0, "broadcaster", dest))

	while queue:
		curr_st, src, name = queue.popleft()

		if name == "rx":
			continue

		new_st = False
		
		if name in flip_flops:
			if curr_st:
				continue
			flip_flops[name] = not flip_flops[name]
			if flip_flops[name]:
				new_st = True
		elif name in conjugates:
			conjugates[name][src] = curr_st
			for n in conjugates[name].values():
				if n == 0:
					new_st = True
					break

		for dest in from_to[name]:
			queue.append((new_st, name, dest))

		for elem, elem_st in conjugates[rx_parent].items():
			if elem_st and elem not in seen:
				seen.add(elem)
				button_presses_list.append(button_presses)

print(math.lcm(*button_presses_list))
