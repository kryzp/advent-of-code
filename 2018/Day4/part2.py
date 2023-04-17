
from collections import defaultdict

ll = sorted([x for x in open("input.txt").read().strip().split("\n")])

guards = defaultdict(lambda: [0 for x in range(60)])

cur_guard = None
start = None

for l in ll:
	if l.endswith("begins shift"):
		cur_guard = l.split(" ")[3]
	elif l.endswith("wakes up"):
		end = int(l.split(" ")[1].split(":")[1][:-1])
		for x in range(start, end):
			guards[cur_guard][x] += 1
	elif l.endswith("falls asleep"):
		start = int(l.split(" ")[1].split(":")[1][:-1])

guard_id = sorted(guards.keys(), key=lambda x: max(guards[x]))[-1]
common_time = guards[guard_id].index(max(guards[guard_id]))

print(int(guard_id[1:]) * common_time)
